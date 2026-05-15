# [AGV Inteligente]

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini%20API-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)

### 🎥 Demonstração do Projeto
**[Assista ao Pitch e Demonstração da Solução (2-3 min)](INSERIR_LINK_DO_VIDEO_AQUI)**

### 🚀 Link do Protótipo
** [[PROTÓTIPO NO GOOGLE AI STUDIO]](https://aistudio.google.com/apps/990b8fe9-1fc5-48c1-b262-4a4c0661d2f4?showPreview=true&showAssistant=true)

---

### 1. Identificação do Grupo
* **Instituição:** Faculdade Engenheiro Salvador Arena (FSA)
* **Curso:** Engenharia de Controle e Automação
* **Grupo:** [Inserir Identificação do Grupo]
* **Integrantes:**
    * [Nome Completo 1] - RA: [000000000]
    * [Nome Completo 2] - RA: [000000000]
    * [Nome Completo 3] - RA: [000000000]
    * [Nome Completo 4] - RA: [000000000]

---

### 2. Área Problema Selecionada
Selecione a trilha tecnológica do projeto (marque com um [x]):
* [ ] **Saúde 4.0:** Robótica Assistiva (Controladores Inteligentes/Fuzzy)
* [ ] **Smart Grid:** Eficiência Energética e Descarbonização
* [ ] **Agtech:** Automação de Precisão e Visão Computacional
* [X] **Logística Autônoma:** Coordenação de AGVs e Otimização de Rotas

### 3. Diagnóstico e Definição do Agente
* **Contexto:** [Descrever o contexto em que o sistema está inserido. Ex: Inserido na Saúde Digital, o sistema analisa dados fisiológicos...]
* **Problema:** [Descrever a dor ou lacuna resolvida. Ex: Riscos de hipo ou hiperglicemia devido à dificuldade de interpretar...]
* **Impacto:** [Descrever os ganhos com a solução. Ex: Transformação de dados brutos em alertas preditivos...]

#### Modelagem PEAS
| Componente | Descrição |
| :--- | :--- |
| **Performance (P)** | [Ex: Precisão na classificação, detecção de variações bruscas...] |
| **Ambiente (E)** | [Ex: Dados simulados de glicose e histórico de eventos...] |
| **Atuadores (A)** | [Ex: Alertas do sistema, recomendações via dashboard...] |
| **Sensores (S)** | [Ex: Dados de glicose (mg/dL), marcação temporal...] |

---

### 4. Arquitetura Lógica e Aprendizado
O **[Nome do Projeto]** opera através de uma arquitetura híbrida que garante segurança técnica e clareza para o usuário:

1.  **Módulo Preditivo (Etapa 3):** Utiliza uma **[Ex: Rede Neural Artificial (RNA) do tipo MLPRegressor]** para [explicar o objetivo preditivo].
2.  **Módulo de Controle (Etapa 2):** Um **[Ex: Sistema Especialista / Lógica Fuzzy]** classifica o risco com base [explicar os parâmetros].
3.  **Camada Interpretativa:** A **API do Gemini** recebe os outputs técnicos e gera uma explicação humanizada, sugerindo ajustes baseados no contexto do usuário.

---

### 5. Justificativa da Abordagem
Para o desenvolvimento do núcleo de inteligência deste projeto, foi selecionada a abordagem de **[Redes Neurais Artificiais (RNA) OU Algoritmos Evolutivos]**.

**Por que esta abordagem foi escolhida?**
* **Natureza do Problema:** O problema de [Citar o problema, ex: previsão de demanda de carga / otimização de despacho] exige uma solução que lide com [ex: padrões não-lineares / grande espaço de busca de soluções], onde métodos estatísticos tradicionais teriam baixo desempenho.
* **Capacidade de [Generalização/Otimização]:** * *[Se RNA]:* A RNA foi escolhida pela sua alta capacidade de aprender com dados históricos e identificar correlações complexas entre variáveis climáticas e consumo energético.
    * *[Se Evolutiva]:* A abordagem evolutiva foi escolhida para encontrar a configuração ótima de distribuição de recursos, onde o objetivo é minimizar o custo e a emissão de CO2 simultaneamente.
* **Escalabilidade:** O modelo permite a integração de novas variáveis de entrada (sensores) sem a necessidade de reestruturação completa da lógica de controle.

---

### 6. Evidências Visuais e Desempenho
*Arquivos armazenados na pasta `/assets/images`.*

**Imagem 1: [Ex: Curva de Loss da Rede Neural (Treinamento)]**
[Breve descrição do que o gráfico demonstra]
![Descrição da Imagem 1](assets/images/imagem1.png)

**Imagem 2: [Ex: Validação Cruzada e Métricas / Log do Gemini]**
[Breve descrição dos resultados ou do log de execução]
![Descrição da Imagem 2](assets/images/imagem2.png)

---

### 7. Estrutura do Repositório
* `/assets/images`: Prints de gráficos, logs e diagramas.
* `/data`: Datasets ou arquivos de entrada (se aplicável).
* `/notebooks`: Notebook `.ipynb` principal (executável do início ao fim).
* `requirements.txt`: Lista de dependências (scikit-learn, google-generativeai, pandas, etc).
* `README.md`: Esta documentação.

---

### 8. Instruções para Execução
1. Clone o repositório: `git clone https://github.com/willianbalieiroc/AGV-Inteligente/tree/main/program`
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
1. Abra o arquivo na pasta `/notebooks` via Google Colab.
2. **Importante:** Insira sua `GOOGLE_API_KEY` na célula de configuração da API do Gemini para habilitar a camada interpretativa.
3. Execute todas as células sequencialmente.

## 🤖 9. Apêndice de IA

Relato sobre o suporte de ferramentas de Inteligência Artificial Generativa no desenvolvimento:

* **Ferramentas:** [Ex: Gemini, ChatGPT].
* **Aplicação:** Apoio na estruturação do código, revisão textual, sugestão de métricas e organização do pipeline de ETL.
* **Validação:** Todos os resultados, métricas de desempenho e interpretações estatísticas foram conferidos e validados tecnicamente pelo grupo.

---
© 2026 - Projeto de Inteligência Artificial - Faculdade Engenheiro Salvador Arena
