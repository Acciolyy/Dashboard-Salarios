"""Gráficos Plotly do dashboard histórico."""

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure


def top_cargos(df: pd.DataFrame) -> Figure:
    top = df.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
    fig = px.bar(
        top,
        x='usd',
        y='cargo',
        orientation='h',
        title="Top 10 cargos por salário médio",
        labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
    )
    fig.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
    return fig


def distribuicao_salarios(df: pd.DataFrame) -> Figure:
    fig = px.histogram(
        df,
        x='usd',
        nbins=30,
        title="Distribuição de salários anuais",
        labels={'usd': 'Faixa salarial (USD)', 'count': ''}
    )
    fig.update_layout(title_x=0.1)
    return fig


def tipos_trabalho(df: pd.DataFrame) -> Figure:
    contagem = df['remoto'].value_counts().reset_index()
    contagem.columns = ['tipo_trabalho', 'quantidade']
    fig = px.pie(
        contagem,
        names='tipo_trabalho',
        values='quantidade',
        title='Proporção dos tipos de trabalho',
        hole=0.5
    )
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title_x=0.1)
    return fig


def salario_por_pais(df: pd.DataFrame) -> Figure:
    media_pais = df.groupby('residencia_iso3')['usd'].mean().reset_index()
    fig = px.choropleth(
        media_pais,
        locations='residencia_iso3',
        color='usd',
        color_continuous_scale='rdylgn',
        title='Salário médio por país',
        labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
    )
    fig.update_layout(title_x=0.1)
    return fig
