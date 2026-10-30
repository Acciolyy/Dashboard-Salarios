import logging

import streamlit as st

import graficos
from dados import carregar_dados, filtrar
from mercado import renderizar_mercado

logger = logging.getLogger(__name__)

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

try:
    df = carregar_dados()
except Exception:
    logger.exception("Não foi possível carregar o dataset (local nem remoto).")
    st.error("❌ Não foi possível carregar os dados no momento. Tente novamente mais tarde.")
    st.stop()

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")

anos_selecionados = st.sidebar.multiselect("Ano", sorted(df['ano'].unique()))
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", sorted(df['senioridade'].unique()))
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", sorted(df['contrato'].unique()))
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", sorted(df['tamanho_empresa'].unique()))
cargos_selecionados = st.sidebar.multiselect("Cargo", sorted(df['cargo'].unique()))

filtros_aplicados = any([
    anos_selecionados,
    senioridades_selecionadas,
    contratos_selecionados,
    tamanhos_selecionados,
    cargos_selecionados,
])
df_filtrado = filtrar(
    df,
    anos_selecionados,
    senioridades_selecionadas,
    contratos_selecionados,
    tamanhos_selecionados,
    cargos_selecionados,
)

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

if not filtros_aplicados:
    st.info("👈 Selecione ao menos um filtro na barra lateral para visualizar os dados.")
else:
    # --- Métricas Principais (KPIs) ---
    st.subheader("Métricas gerais (Salário anual em USD)")

    if not df_filtrado.empty:
        salario_medio = df_filtrado['usd'].mean()
        salario_maximo = df_filtrado['usd'].max()
        total_registros = df_filtrado.shape[0]
        cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
    else:
        salario_medio = 0
        salario_maximo = 0
        total_registros = 0
        cargo_mais_frequente = ""

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Salário médio", f"${salario_medio:,.0f}")
    col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
    col3.metric("Total de registros", f"{total_registros:,}")
    col4.metric("Cargo mais frequente", cargo_mais_frequente)

    st.markdown("---")

    # --- Análises Visuais com Plotly ---
    st.subheader("Gráficos")

    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        if not df_filtrado.empty:
            if df_filtrado['cargo'].nunique() >= 2:
                st.plotly_chart(graficos.top_cargos(df_filtrado), use_container_width=True)
            else:
                st.info("ℹ️ Selecione 2 ou mais cargos no filtro para comparar os salários médios entre diferentes posições.")
        else:
            st.warning("Nenhum dado para exibir no gráfico de cargos.")

    with col_graf2:
        if not df_filtrado.empty:
            st.plotly_chart(graficos.distribuicao_salarios(df_filtrado), use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico de distribuição.")

    col_graf3, col_graf4 = st.columns(2)

    with col_graf3:
        if not df_filtrado.empty:
            st.plotly_chart(graficos.tipos_trabalho(df_filtrado), use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

    with col_graf4:
        if not df_filtrado.empty:
            st.plotly_chart(graficos.salario_por_pais(df_filtrado), use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico de países.")

    # --- Tabela de Dados Detalhados ---
    st.subheader("Dados Detalhados")
    st.dataframe(df_filtrado)

st.markdown("---")

# --- Mercado em Tempo Real (API Adzuna) ---
renderizar_mercado()
