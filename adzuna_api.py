"""Integração com a API de salários da Adzuna (seção "Mercado em Tempo Real").

Escopo intencionalmente fixo (6 cargos x 3 países = 18 combinações) para manter
o consumo de chamadas previsível e dentro da cota gratuita da Adzuna
(1.000 chamadas/mês). Ver README.md para detalhes.
"""

import os

import requests
import streamlit as st

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

ADZUNA_APP_ID = os.environ.get("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.environ.get("ADZUNA_APP_KEY")

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
    """Erro ao consultar a API da Adzuna (credenciais, quota, indisponibilidade, etc)."""


@st.cache_data(ttl=86400)
def buscar_historico_salarial(cargo: str, pais_codigo: str) -> dict:
    """Busca o histórico salarial (últimos 12 meses) de um cargo em um país na Adzuna.

    Resultado fica em cache por 24h (ttl=86400) para limitar o número de chamadas
    reais à API, independentemente de quantos visitantes acessem o dashboard.
    """
    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        raise AdzunaAPIError("Credenciais da API Adzuna não configuradas.")

    url = ADZUNA_HISTORY_URL.format(pais_codigo=pais_codigo)
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": cargo,
        "months": 12,
        "content-type": "application/json",
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
    except requests.exceptions.RequestException as erro:
        # TODO: debug temporário — remover depois de diagnosticar falhas da API
        resposta_erro = getattr(erro, "response", None)
        if resposta_erro is not None:
            print(f"[DEBUG Adzuna] status={resposta_erro.status_code} body={resposta_erro.text}")
        else:
            print(f"[DEBUG Adzuna] sem resposta HTTP (erro de conexão/timeout): {erro}")
        raise AdzunaAPIError(f"Falha ao consultar a API da Adzuna: {erro}") from erro
    except ValueError as erro:
        # TODO: debug temporário — remover depois de diagnosticar falhas da API
        print(f"[DEBUG Adzuna] status={resposta.status_code} body={resposta.text}")
        raise AdzunaAPIError("Resposta inválida da API da Adzuna.") from erro

    valores_mensais = list(dados.get("month", {}).values())
    if not valores_mensais:
        raise AdzunaAPIError("Nenhum dado de salário retornado para essa combinação.")

    return {
        "media": sum(valores_mensais) / len(valores_mensais),
        "minimo": min(valores_mensais),
        "maximo": max(valores_mensais),
    }
