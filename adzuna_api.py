"""Integração com a API de salários da Adzuna (seção "Mercado em Tempo Real").

Escopo intencionalmente fixo (6 cargos x 3 países = 18 combinações) para manter
o consumo de chamadas previsível e dentro da cota gratuita da Adzuna
(1.000 chamadas/mês). Ver README.md para detalhes.
"""

import logging
import os
import time

import requests
import streamlit as st

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

ADZUNA_APP_ID = os.environ.get("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.environ.get("ADZUNA_APP_KEY")

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = 10  # segundos
FALHA_TTL = 300  # segundos em que uma falha é lembrada antes de chamar a API de novo

ADZUNA_HISTORY_URL = "https://api.adzuna.com/v1/api/jobs/{pais_codigo}/history"

# Os 6 cargos com maior volume de registros no dataset histórico (dados-imersao-final.csv)
CARGOS_DISPONIVEIS = [
    "Data Scientist",
    "Software Engineer",
    "Data Engineer",
    "Data Analyst",
    "Engineer",
    "Machine Learning Engineer",
]

# Países fixos (nome exibido -> código ISO usado pela Adzuna), com símbolo de moeda local
PAISES_DISPONIVEIS = {
    "Brasil": {"codigo": "br", "moeda": "R$"},
    "Estados Unidos": {"codigo": "us", "moeda": "US$"},
    "Reino Unido": {"codigo": "gb", "moeda": "£"},
}


class AdzunaAPIError(Exception):
    """Erro ao consultar a API da Adzuna.

    A mensagem é segura para exibir ao usuário (nunca contém URL nem credenciais);
    os detalhes técnicos vão para o log do servidor.
    """


def _mensagem_para_status(status: int) -> str:
    if status in (401, 403):
        return "Credenciais da Adzuna inválidas ou sem permissão."
    if status == 429:
        return "Limite de consultas da Adzuna atingido. Tente novamente mais tarde."
    return "A Adzuna está indisponível no momento."


@st.cache_data(ttl=86400)
def buscar_historico_salarial(cargo: str, pais_codigo: str) -> dict:
    """Busca o histórico salarial (últimos 12 meses) de um cargo em um país na Adzuna.

    Resultado fica em cache por 24h (ttl=86400) para limitar o número de chamadas
    reais à API, independentemente de quantos visitantes acessem o dashboard.
    """
    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        logger.error("ADZUNA_APP_ID/ADZUNA_APP_KEY ausentes do ambiente.")
        raise AdzunaAPIError("Credenciais da Adzuna não configuradas.")

    url = ADZUNA_HISTORY_URL.format(pais_codigo=pais_codigo)
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": cargo,
        "months": 12,
        "content-type": "application/json",
    }

    # Os logs não incluem a exceção original: sua mensagem contém a URL com app_key.
    try:
        resposta = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.exceptions.Timeout:
        logger.error("Timeout (%ss) consultando Adzuna: cargo=%r pais=%r", REQUEST_TIMEOUT, cargo, pais_codigo)
        raise AdzunaAPIError("A Adzuna demorou demais para responder.") from None
    except requests.exceptions.HTTPError as erro:
        status = erro.response.status_code
        logger.error("HTTP %s da Adzuna: cargo=%r pais=%r body=%s", status, cargo, pais_codigo, erro.response.text)
        raise AdzunaAPIError(_mensagem_para_status(status)) from None
    except requests.exceptions.RequestException as erro:
        logger.error("Erro de conexão com a Adzuna (%s): cargo=%r pais=%r", type(erro).__name__, cargo, pais_codigo)
        raise AdzunaAPIError("Não foi possível conectar à Adzuna.") from None
    except ValueError:
        logger.error("JSON inválido da Adzuna: cargo=%r pais=%r body=%s", cargo, pais_codigo, resposta.text)
        raise AdzunaAPIError("Resposta inválida da Adzuna.") from None

    valores_mensais = list(dados.get("month", {}).values())
    if not valores_mensais:
        logger.error("Campo 'month' vazio: cargo=%r pais=%r resposta=%s", cargo, pais_codigo, dados)
        raise AdzunaAPIError("A Adzuna não retornou dados para essa combinação.")

    return {
        "media": sum(valores_mensais) / len(valores_mensais),
        "minimo": min(valores_mensais),
        "maximo": max(valores_mensais),
    }


# Falhas recentes por (cargo, pais): o st.cache_data não guarda exceções, então sem isto
# cada clique após uma falha gastaria cota da API. Vale por processo, não por sessão.
_falhas_recentes: dict[tuple[str, str], tuple[float, str]] = {}


def consultar_historico_salarial(cargo: str, pais_codigo: str) -> dict:
    """Como `buscar_historico_salarial`, mas lembra falhas por `FALHA_TTL` segundos."""
    chave = (cargo, pais_codigo)
    falha = _falhas_recentes.get(chave)
    if falha and time.monotonic() - falha[0] < FALHA_TTL:
        raise AdzunaAPIError(falha[1])

    try:
        resultado = buscar_historico_salarial(cargo, pais_codigo)
    except AdzunaAPIError as erro:
        _falhas_recentes[chave] = (time.monotonic(), str(erro))
        raise
    _falhas_recentes.pop(chave, None)
    return resultado
