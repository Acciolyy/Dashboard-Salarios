"""Carregamento e filtragem do dataset histórico de salários."""

import logging
from pathlib import Path

import pandas as pd
import streamlit as st

logger = logging.getLogger(__name__)

# Lê o CSV versionado junto do app; se não for possível, tenta a cópia remota.
CSV_LOCAL = Path(__file__).parent / "dados-imersao-final.csv"
CSV_REMOTO = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"


@st.cache_data
def carregar_dados() -> pd.DataFrame:
    try:
        return pd.read_csv(CSV_LOCAL)
    except (OSError, pd.errors.ParserError, pd.errors.EmptyDataError) as erro:
        logger.warning("Falha ao ler %s (%s); usando a cópia remota.", CSV_LOCAL, erro)
        return pd.read_csv(CSV_REMOTO)


def filtro_ou_tudo(coluna: pd.Series, selecionados: list) -> pd.Series:
    """Filtro vazio (nenhuma opção marcada) é tratado como "sem filtro" (mostra tudo)."""
    if not selecionados:
        return pd.Series(True, index=coluna.index)
    return coluna.isin(selecionados)


def filtrar(df: pd.DataFrame, anos, senioridades, contratos, tamanhos, cargos) -> pd.DataFrame:
    """Aplica os filtros da barra lateral.

    O dashboard só exibe dados depois que pelo menos um filtro é selecionado —
    sem nenhum filtro, devolve um DataFrame vazio em vez do dataset inteiro.
    """
    if not any([anos, senioridades, contratos, tamanhos, cargos]):
        return df.iloc[0:0]
    return df[
        filtro_ou_tudo(df['ano'], anos) &
        filtro_ou_tudo(df['senioridade'], senioridades) &
        filtro_ou_tudo(df['contrato'], contratos) &
        filtro_ou_tudo(df['tamanho_empresa'], tamanhos) &
        filtro_ou_tudo(df['cargo'], cargos)
    ]
