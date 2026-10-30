"""Seção "Mercado em Tempo Real" (API da Adzuna) do dashboard."""

import streamlit as st

from adzuna_api import (
    CARGOS_DISPONIVEIS,
    PAISES_DISPONIVEIS,
    AdzunaAPIError,
    consultar_historico_salarial,
)


def renderizar_mercado() -> None:
    # Seção independente da análise histórica: consulta a API da Adzuna para um
    # conjunto fixo de 6 cargos x 3 países (18 combinações), com resultado em
    # cache por 24h. Ver README.md para detalhes do escopo fixo.
    st.subheader("🌐 Mercado em Tempo Real")
    st.markdown(
        "Consulte a média salarial recente informada pela [Adzuna](https://www.adzuna.com/), "
        "um agregador de vagas de emprego, para um conjunto pré-definido de cargos e países."
    )

    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        cargo_mercado = st.selectbox("Cargo", CARGOS_DISPONIVEIS)
    with col_sel2:
        pais_mercado = st.selectbox("País", list(PAISES_DISPONIVEIS.keys()))

    pais_info = PAISES_DISPONIVEIS[pais_mercado]

    # A chamada só deve ocorrer quando o usuário clicar em "Consultar" — nunca
    # automaticamente no carregamento da página ou em reruns (ex.: causados pelo
    # file watcher ou por outros widgets da sidebar).
    if "mercado_resultado" not in st.session_state:
        st.session_state.mercado_resultado = None
    if "mercado_erro" not in st.session_state:
        st.session_state.mercado_erro = None

    if st.button("🔎 Consultar"):
        try:
            st.session_state.mercado_resultado = {
                **consultar_historico_salarial(cargo_mercado, pais_info["codigo"]),
                "moeda": pais_info["moeda"],
            }
            st.session_state.mercado_erro = None
        except AdzunaAPIError as erro:
            st.session_state.mercado_resultado = None
            st.session_state.mercado_erro = str(erro)

    if st.session_state.mercado_resultado:
        resultado = st.session_state.mercado_resultado
        moeda = resultado["moeda"]

        col_m1, col_m2 = st.columns(2)
        col_m1.metric("Salário médio anual", f"{moeda} {resultado['media']:,.0f}")
        col_m2.metric(
            "Faixa (mín - máx)",
            f"{moeda} {resultado['minimo']:,.0f} - {moeda} {resultado['maximo']:,.0f}",
        )
        st.caption("🕒 Dado em cache, atualizado a cada 24h — não reflete tempo real por visita.")
    elif st.session_state.mercado_erro:
        st.warning(f"⚠️ Dados de mercado indisponíveis: {st.session_state.mercado_erro}")
    else:
        st.info("Selecione um cargo e um país e clique em **Consultar** para ver os dados de mercado.")
