# 📊 Dashboard de Análise de Salários na Área de Dados

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

### 🗃️ Dados
- **Dataset**: CSV com 133.341 registros
- **Fonte de Dados**: Dados processados e disponibilizados via GitHub
- **Campos**: ano, senioridade, contrato, cargo, salário, moeda, USD, residência, tipo de trabalho, empresa, tamanho da empresa, código ISO do país

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

5. **Execute o dashboard**
```bash
streamlit run app.py
```

6. **Acesse no navegador**
O Streamlit abrirá automaticamente seu navegador padrão. Caso não abra, acesse:
```
http://localhost:8501
```

---

## 📂 Estrutura do Projeto

```
Dashboard-Salarios/
│
├── app.py                          # Aplicação principal Streamlit
├── requirements.txt                # Dependências do projeto
├── dados-imersao-final.csv         # Dataset com 133k+ registros
├── README.md                       # Documentação do projeto
├── .gitignore                      # Arquivos ignorados pelo Git
│
└── .venv/                          # Ambiente virtual Python (não versionado)
```

### 📝 Descrição dos Arquivos

- **`app.py`**: Código principal da aplicação Streamlit com toda a lógica do dashboard
- **`requirements.txt`**: Lista de dependências Python necessárias (pandas, streamlit, plotly)
- **`dados-imersao-final.csv`**: Dataset completo com 133.341 registros salariais
- **`README.md`**: Documentação completa do projeto
- **`.gitignore`**: Arquivo de configuração do Git para ignorar arquivos desnecessários
- **`.venv/`**: Ambiente virtual Python (não incluído no repositório)

---

## 🔮 Melhorias Futuras

### Funcionalidades Técnicas
- [ ] Integração com APIs de dados salariais em tempo real
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

Desenvolvido por Thiago Viriato Accioly

</div>
