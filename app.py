import streamlit as st
import pandas as pd
import plotly.express as px

from adzuna_api import (
    CARGOS_DISPONIVEIS,
    PAISES_DISPONIVEIS,
    AdzunaAPIError,
    buscar_historico_salarial,
)

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide",
)

# --- Carregamento dos dados, são os dados que fiz no colab ---
@st.cache_data
def carregar_dados() -> pd.DataFrame:
    return pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")


df = carregar_dados()

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")

# Filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis)

# Filtro de Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis)

# Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis)

# Filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis)

# Filtro por Cargo
cargos_disponiveis = sorted(df['cargo'].unique())
cargos_selecionados = st.sidebar.multiselect("Cargo", cargos_disponiveis)

# --- Filtragem do DataFrame, é onde aplica os filtros nos dados ---
# O dataframe principal é filtrado com base nas seleções feitas na barra lateral.
# Filtro vazio (nenhuma opção marcada) é tratado como "sem filtro aplicado" (mostra tudo).
def filtro_ou_tudo(coluna: pd.Series, selecionados: list) -> pd.Series:
    if not selecionados:
        return pd.Series(True, index=coluna.index)
    return coluna.isin(selecionados)


# O dashboard só exibe dados depois que pelo menos um filtro é selecionado —
# evita mostrar o dataset inteiro sem filtro nenhum aplicado.
filtros_aplicados = any([
    anos_selecionados,
    senioridades_selecionadas,
    contratos_selecionados,
    tamanhos_selecionados,
    cargos_selecionados,
])

if filtros_aplicados:
    df_filtrado = df[
        filtro_ou_tudo(df['ano'], anos_selecionados) &
        filtro_ou_tudo(df['senioridade'], senioridades_selecionadas) &
        filtro_ou_tudo(df['contrato'], contratos_selecionados) &
        filtro_ou_tudo(df['tamanho_empresa'], tamanhos_selecionados) &
        filtro_ou_tudo(df['cargo'], cargos_selecionados)
    ]
else:
    df_filtrado = df.iloc[0:0]

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
            cargos_unicos = df_filtrado['cargo'].nunique()
            if cargos_unicos >= 2:
                top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
                grafico_cargos = px.bar(
                    top_cargos,
                    x='usd',
                    y='cargo',
                    orientation='h',
                    title="Top 10 cargos por salário médio",
                    labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
                )
                grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
                st.plotly_chart(grafico_cargos, use_container_width=True)
            else:
                st.info("ℹ️ Selecione 2 ou mais cargos no filtro para comparar os salários médios entre diferentes posições.")
        else:
            st.warning("Nenhum dado para exibir no gráfico de cargos.")

    with col_graf2:
        if not df_filtrado.empty:
            grafico_hist = px.histogram(
                df_filtrado,
                x='usd',
                nbins=30,
                title="Distribuição de salários anuais",
                labels={'usd': 'Faixa salarial (USD)', 'count': ''}
            )
            grafico_hist.update_layout(title_x=0.1)
            st.plotly_chart(grafico_hist, use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico de distribuição.")

    col_graf3, col_graf4 = st.columns(2)

    with col_graf3:
        if not df_filtrado.empty:
            remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
            remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
            grafico_remoto = px.pie(
                remoto_contagem,
                names='tipo_trabalho',
                values='quantidade',
                title='Proporção dos tipos de trabalho',
                hole=0.5
            )
            grafico_remoto.update_traces(textinfo='percent+label')
            grafico_remoto.update_layout(title_x=0.1)
            st.plotly_chart(grafico_remoto, use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

    with col_graf4:
        if not df_filtrado.empty:
            media_pais = df_filtrado.groupby('residencia_iso3')['usd'].mean().reset_index()
            grafico_paises = px.choropleth(media_pais,
                locations='residencia_iso3',
                color='usd',
                color_continuous_scale='rdylgn',
                title='Salário médio por país',
                labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
            grafico_paises.update_layout(title_x=0.1)
            st.plotly_chart(grafico_paises, use_container_width=True)
        else:
            st.warning("Nenhum dado para exibir no gráfico de países.")

    # --- Tabela de Dados Detalhados ---
    st.subheader("Dados Detalhados")
    st.dataframe(df_filtrado)

st.markdown("---")

# --- Mercado em Tempo Real (API Adzuna) ---
# Seção independente da análise histórica acima: consulta a API da Adzuna
# para um conjunto fixo de 6 cargos x 3 países (18 combinações), com
# resultado em cache por 24h. Ver README.md para detalhes do escopo fixo.
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

# A chamada a buscar_historico_salarial só deve ocorrer quando o usuário clicar
# em "Consultar" — nunca automaticamente no carregamento da página ou em reruns
# (ex.: causados pelo file watcher ou por outros widgets da sidebar).
if "mercado_resultado" not in st.session_state:
    st.session_state.mercado_resultado = None
if "mercado_erro" not in st.session_state:
    st.session_state.mercado_erro = False

if st.button("🔎 Consultar"):
    try:
        st.session_state.mercado_resultado = {
            **buscar_historico_salarial(cargo_mercado, pais_info["codigo"]),
            "moeda": pais_info["moeda"],
        }
        st.session_state.mercado_erro = False
    except AdzunaAPIError:
        st.session_state.mercado_resultado = None
        st.session_state.mercado_erro = True

if st.session_state.mercado_resultado:
    resultado_mercado = st.session_state.mercado_resultado
    moeda = resultado_mercado["moeda"]

    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Salário médio anual", f"{moeda} {resultado_mercado['media']:,.0f}")
    col_m2.metric(
        "Faixa (mín - máx)",
        f"{moeda} {resultado_mercado['minimo']:,.0f} - {moeda} {resultado_mercado['maximo']:,.0f}",
    )
    st.caption("🕒 Dado em cache, atualizado a cada 24h — não reflete tempo real por visita.")
elif st.session_state.mercado_erro:
    st.warning(
        "⚠️ Dados de mercado em tempo real temporariamente indisponíveis."
    )
else:
    st.info("Selecione um cargo e um país e clique em **Consultar** para ver os dados de mercado.")