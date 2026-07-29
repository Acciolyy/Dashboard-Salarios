# 📊 Dashboard de Análise de Salários na Área de Dados

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tech-salary-insights.streamlit.app/)

**🚀 [Acesse o Dashboard ao Vivo](https://tech-salary-insights.streamlit.app/) 🚀**

*Dashboard interativo para análise de salários em Data Science, Engineering e Analytics*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.44.1-FF4B4B.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.3-150458.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.24.1-3F4F75.svg)](https://plotly.com/)

</div>

---

## 👨‍💻 Sobre o Desenvolvedor

Olá! Meu nome é **Thiago Viriato Accioly** e sou estudante de **Engenharia de Software na Universidade de Brasília (UnB)**. 

Desenvolvi este projeto com o objetivo de aplicar e aprofundar meus conhecimentos em análise de dados, visualização interativa e desenvolvimento de aplicações web. Como futuro engenheiro de software, entendo a importância de transformar dados brutos em insights acionáveis através de interfaces intuitivas e acessíveis. Este dashboard representa minha visão sobre como a tecnologia pode democratizar o acesso à informação salarial, promovendo transparência no mercado de trabalho e auxiliando profissionais em suas decisões de carreira.

Este projeto também demonstra minhas habilidades em:
- **Manipulação e análise de grandes volumes de dados**
- **Criação de dashboards interativos e responsivos**
- **Desenvolvimento de aplicações web com Python**
- **Visualização de dados com bibliotecas modernas**
- **Boas práticas de desenvolvimento e versionamento de código**

---

## 🎯 O que é este projeto?

Este é um **dashboard interativo de análise salarial** desenvolvido em Python, focado especificamente no mercado de trabalho da área de dados (Data Science, Data Engineering, Data Analysis, BI, entre outros). O projeto oferece uma interface web moderna e intuitiva que permite aos usuários explorarem tendências salariais, compararem diferentes posições e obterem insights valiosos sobre o mercado de trabalho tech.

O dashboard processa um dataset com **mais de 133 mil registros** contendo informações detalhadas sobre salários, tipos de contrato, localização geográfica, níveis de senioridade e modalidades de trabalho (remoto, presencial, híbrido).

### 🌐 Demo Online

O dashboard está **disponível online** e pode ser acessado diretamente pelo navegador, sem necessidade de instalação:

**👉 [https://tech-salary-insights.streamlit.app/](https://tech-salary-insights.streamlit.app/)**

Explore os dados, aplique filtros personalizados e descubra insights sobre salários na área de dados em tempo real!

---

## 🚀 Funcionalidades

### 📈 Análises Visuais Interativas

1. **Métricas Gerais (KPIs)**
   - Salário médio anual em USD
   - Salário máximo registrado
   - Total de registros na base filtrada
   - Cargo mais frequente

2. **Top 10 Cargos por Salário Médio**
   - Gráfico de barras horizontal comparando as posições mais bem remuneradas
   - Ordenação automática por média salarial

3. **Distribuição de Salários**
   - Histograma mostrando a concentração de salários em diferentes faixas
   - Visualização clara da distribuição salarial no mercado

4. **Proporção de Tipos de Trabalho**
   - Gráfico de pizza (donut) exibindo a distribuição entre trabalho remoto, presencial e híbrido
   - Percentuais precisos de cada modalidade

5. **Mapa Global de Salários**
   - Mapa coroplético mundial mostrando a média salarial por país
   - Escala de cores indicando regiões com melhores remunerações

### 🌐 Mercado em Tempo Real

Seção independente da análise histórica acima, que consulta a **API da Adzuna** para trazer uma referência salarial mais recente:

- **Dois seletores fixos**: cargo (6 opções) e país (3 opções) — sem busca livre por texto
- **Cargos disponíveis**: Data Scientist, Software Engineer, Data Engineer, Data Analyst, Engineer e Machine Learning Engineer (os 6 cargos com maior volume de registros no dataset histórico)
- **Países disponíveis**: Brasil, Estados Unidos e Reino Unido
- **Dados exibidos**: salário médio anual e faixa (mínimo–máximo) do cargo/país selecionados, na moeda local
- **Cache de 24h**: os resultados ficam em cache (`ttl=86400`) para limitar o número de chamadas reais à API, independentemente da quantidade de visitantes
- **Falha graciosa**: se a API estiver indisponível, com quota excedida ou credenciais inválidas, a seção exibe um aviso amigável em vez de quebrar o dashboard

> ⚠️ **Por que o escopo é fixo (6 cargos x 3 países)?** A Adzuna oferece um plano gratuito limitado a **1.000 chamadas/mês**. Ao restringir as opções a 18 combinações possíveis e cachear cada uma por 24h, o consumo máximo teórico fica em `18 combinações × 30 dias ≈ 540 chamadas/mês`, bem abaixo do limite — mesmo em cenários de alto tráfego. Um campo de busca livre por cargo/país tornaria o consumo imprevisível e poderia estourar a cota gratuita.

**Configuração necessária**: esta seção requer credenciais da Adzuna (`ADZUNA_APP_ID` e `ADZUNA_APP_KEY`) via variáveis de ambiente — veja a seção [Configurando a API da Adzuna](#-configurando-a-api-da-adzuna-opcional) abaixo. Sem elas, a seção exibe o aviso de indisponibilidade e o restante do dashboard continua funcionando normalmente.

### 🔍 Sistema de Filtros Avançado

O dashboard oferece um sistema robusto de filtros na barra lateral, permitindo análises personalizadas:

- **Ano**: Filtre por anos específicos ou compare múltiplos períodos
- **Senioridade**: Junior, Pleno, Senior ou Executivo
- **Tipo de Contrato**: Full-time, Part-time, Freelance, etc.
- **Tamanho da Empresa**: Pequena, Média ou Grande
- **Cargo**: Filtre por posições específicas (Data Engineer, Data Scientist, BI Developer, etc.)

### 📊 Visualização de Dados Detalhados

Tabela completa e interativa com todos os dados filtrados, permitindo:
- Ordenação por qualquer coluna
- Busca textual
- Scroll horizontal e vertical
- Exportação dos dados

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

### Linguagem de Programação
- **Python 3.8**: Linguagem principal do projeto

### Bibliotecas e Frameworks

#### 📊 Análise e Manipulação de Dados
- **Pandas (v2.2.3)**: Biblioteca poderosa para manipulação e análise de dados estruturados
  - Processamento de datasets grandes
  - Operações de filtragem, agrupamento e agregação
  - Limpeza e transformação de dados

#### 🎨 Visualização de Dados
- **Plotly (v5.24.1)**: Biblioteca de visualização interativa
  - Gráficos de barras, histogramas e gráficos de pizza
  - Mapas coropléticos interativos
  - Visualizações responsivas e personalizáveis
  - Suporte a zoom, pan e tooltips interativos

#### 🌐 Framework Web
- **Streamlit (v1.44.1)**: Framework para criação de aplicações web de dados
  - Interface intuitiva sem necessidade de HTML/CSS/JavaScript
  - Sistema de widgets interativos (selectbox, multiselect, sliders)
  - Layout responsivo e moderno
  - Atualização automática da interface
  - Cache de dados (`st.cache_data`) para limitar chamadas à API externa

#### 🔌 Integração com API Externa
- **Requests (v2.32.3)**: Cliente HTTP para consumir a API de salários da Adzuna
- **python-dotenv (v1.0.1)**: Carregamento de credenciais a partir de um arquivo `.env` local (opcional, apenas para desenvolvimento)

### 🗃️ Dados

#### Dataset histórico (estático)
- **Dataset**: CSV com 133.341 registros
- **Fonte de Dados**: Dados processados e disponibilizados via GitHub
- **Campos**: ano, senioridade, contrato, cargo, salário, moeda, USD, residência, tipo de trabalho, empresa, tamanho da empresa, código ISO do país

#### Mercado em tempo real
- **Fonte de Dados**: [API de histórico salarial da Adzuna](https://developer.adzuna.com/)
- **Escopo**: 6 cargos x 3 países fixos (18 combinações), sem busca livre — ver [seção Mercado em Tempo Real](#-mercado-em-tempo-real)
- **Cache**: 24 horas por combinação (`@st.cache_data(ttl=86400)`)

### 🔧 Ferramentas de Desenvolvimento
- **Git**: Controle de versão
- **GitHub**: Hospedagem do código e dos dados
- **Python Virtual Environment**: Isolamento de dependências
- **PowerShell**: Terminal para execução local

---

## 💼 Valor para Empresas

### 🎯 Aplicações Práticas em Contexto Corporativo

Este dashboard pode agregar valor significativo para empresas de diversas formas:

#### 1. **Departamento de Recursos Humanos (RH)**
- **Benchmarking Salarial**: Comparar a remuneração oferecida com o mercado
- **Estratégia de Retenção**: Identificar se os salários estão competitivos
- **Planejamento de Budget**: Estimar custos para novas contratações
- **Análise de Equidade Salarial**: Garantir justiça nas remunerações

#### 2. **Recrutamento e Talent Acquisition**
- **Propostas Competitivas**: Criar ofertas salariais atrativas baseadas em dados reais
- **Segmentação por Senioridade**: Entender faixas salariais para cada nível
- **Análise Geográfica**: Ajustar salários conforme localização do candidato
- **Modalidade de Trabalho**: Compreender o impacto do trabalho remoto nos salários

#### 3. **Gestão Estratégica e C-Level**
- **Decisões Baseadas em Dados**: Insights para planejamento financeiro
- **Expansão Internacional**: Análise de custos de pessoal por país
- **Competitividade de Mercado**: Posicionamento da empresa no setor
- **Forecast de Despesas**: Projeção de custos com pessoal

#### 4. **Desenvolvimento de Carreira**
- **Planos de Carreira Transparentes**: Mostrar aos colaboradores perspectivas de crescimento
- **Gestão de Expectativas**: Alinhar expectativas salariais com a realidade do mercado
- **Programas de Desenvolvimento**: Identificar gaps de remuneração por skill

---

## 🔧 Problemas que Este Dashboard Resolve

### ❌ Problemas Identificados

1. **Falta de Transparência Salarial**
   - Dificuldade em acessar informações confiáveis sobre salários
   - Assimetria de informação entre empregadores e candidatos

2. **Decisões Baseadas em "Achismos"**
   - RH fazendo ofertas sem base em dados concretos
   - Risco de perder talentos por propostas não competitivas

3. **Dificuldade em Análises Comparativas**
   - Complexidade para comparar salários entre países, senioridades e cargos
   - Dados dispersos em múltiplas fontes

4. **Falta de Insights Visuais**
   - Planilhas complexas difíceis de interpretar
   - Necessidade de conhecimento técnico para análises

5. **Desatualização de Informações**
   - Pesquisas salariais caras e desatualizadas
   - Falta de dados em tempo real

### ✅ Soluções Oferecidas

1. **Democratização de Dados**
   - Interface acessível para qualquer pessoa
   - Não requer conhecimento técnico avançado

2. **Análises em Tempo Real**
   - Filtros dinâmicos e interativos
   - Respostas instantâneas às consultas

3. **Visualizações Intuitivas**
   - Gráficos modernos e fáceis de interpretar
   - Múltiplas perspectivas dos mesmos dados

4. **Benchmarking Facilitado**
   - Comparações rápidas entre cargos, países e senioridades
   - KPIs claros e objetivos

5. **Base para Decisões Estratégicas**
   - Dados confiáveis para negociações salariais
   - Insights para planejamento de carreira

---

## 📦 Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/Acciolyy/Dashboard-Salarios.git
cd Dashboard-Salarios
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv .venv
```

3. **Ative o ambiente virtual**

Windows (PowerShell):
```powershell
.venv\Scripts\Activate.ps1
```

Linux/Mac:
```bash
source .venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **(Opcional) Configure as credenciais da API Adzuna**

Necessário apenas para a seção "🌐 Mercado em Tempo Real". Sem isso, o restante do dashboard funciona normalmente e essa seção exibe um aviso de indisponibilidade.

```bash
cp .env.example .env
```

Edite o `.env` e preencha com suas credenciais gratuitas obtidas em [developer.adzuna.com](https://developer.adzuna.com/):
```
ADZUNA_APP_ID=seu_app_id
ADZUNA_APP_KEY=sua_app_key
```

> As credenciais nunca devem ser commitadas: o `.env` está no `.gitignore` e apenas o `.env.example` (sem valores) é versionado.

6. **Execute o dashboard**
```bash
streamlit run app.py
```

7. **Acesse no navegador**
O Streamlit abrirá automaticamente seu navegador padrão. Caso não abra, acesse:
```
http://localhost:8501
```

### 🌐 Ou acesse a versão online

Prefere não instalar? Acesse a versão deployada:
**[https://tech-salary-insights.streamlit.app/](https://tech-salary-insights.streamlit.app/)**

---

## 📂 Estrutura do Projeto

```
Dashboard-Salarios/
│
├── app.py                          # Aplicação principal Streamlit (análise histórica + seção de mercado)
├── adzuna_api.py                   # Integração com a API da Adzuna (cache 24h, escopo fixo)
├── requirements.txt                # Dependências do projeto
├── dados-imersao-final.csv         # Dataset com 133k+ registros
├── .env.example                    # Modelo de variáveis de ambiente (sem valores reais)
├── README.md                       # Documentação do projeto
├── .gitignore                      # Arquivos ignorados pelo Git
│
└── .venv/                          # Ambiente virtual Python (não versionado)
```

### 📝 Descrição dos Arquivos

- **`app.py`**: Código principal da aplicação Streamlit com toda a lógica do dashboard
- **`adzuna_api.py`**: Cliente da API da Adzuna usado pela seção "Mercado em Tempo Real" — lê `ADZUNA_APP_ID`/`ADZUNA_APP_KEY` de variáveis de ambiente, nunca hardcoded, e cacheia resultados por 24h
- **`requirements.txt`**: Lista de dependências Python necessárias (pandas, streamlit, plotly, requests, python-dotenv)
- **`dados-imersao-final.csv`**: Dataset completo com 133.341 registros salariais
- **`.env.example`**: Modelo do arquivo `.env` com as chaves esperadas (`ADZUNA_APP_ID`, `ADZUNA_APP_KEY`), sem valores reais
- **`README.md`**: Documentação completa do projeto
- **`.gitignore`**: Arquivo de configuração do Git para ignorar arquivos desnecessários (inclui `.env`)
- **`.venv/`**: Ambiente virtual Python (não incluído no repositório)

---

## 🔮 Melhorias Futuras

### Funcionalidades Técnicas
- [x] Integração com API de dados salariais em tempo real (Adzuna)
- [ ] Sistema de autenticação para empresas
- [ ] Exportação de relatórios em PDF/Excel
- [ ] Análise preditiva com Machine Learning
- [ ] Dashboard de comparação temporal (evolução salarial ao longo dos anos)
- [ ] Filtros geográficos avançados (cidade, região, continente)

### Análises Adicionais
- [ ] Correlação entre tamanho da empresa e salário
- [ ] Análise de benefícios além do salário base
- [ ] Satisfação profissional vs. remuneração
- [ ] Taxa de crescimento salarial por cargo
- [ ] Habilidades mais valorizadas por faixa salarial

### Experiência do Usuário
- [ ] Modo escuro/claro
- [ ] Internacionalização (múltiplos idiomas)
- [ ] Comparações lado a lado
- [ ] Sistema de favoritos e histórico de pesquisas
- [ ] Alertas personalizados de mudanças salariais

---

## 📊 Estatísticas do Dataset

- **Total de Registros**: 133.341
- **Anos Cobertos**: 2020-2025
- **Países Representados**: 50+ países
- **Cargos Únicos**: 100+ posições diferentes
- **Moedas**: Múltiplas moedas convertidas para USD

---

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma Branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a Branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request



---



## 🙏 Agradecimentos

- Comunidade Python pela excelente documentação
- Desenvolvedores do Streamlit, Pandas e Plotly
- Comunidade de Data Science pela cultura de compartilhamento de dados


---

## 📚 Referências

- [Documentação Streamlit](https://docs.streamlit.io/)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Documentação Plotly](https://plotly.com/python/)
- [Python Official Documentation](https://docs.python.org/3/)

---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório! ⭐**

**🚀 [Acesse o Dashboard Online](https://tech-salary-insights.streamlit.app/) 🚀**

Desenvolvido com 💙 por **Thiago Viriato Accioly**

</div>
