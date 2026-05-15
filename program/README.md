# AGV Inteligente

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini%20API-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)

### 🎥 Demonstração do Projeto
**[Assista ao Pitch e Demonstração da Solução (2-3 min)]((https://drive.google.com/file/d/1cPYRB2n3pLNuduaNdMXXr3Xz6w_wzBKD/view?usp=sharing))**

### 🚀 Link do Protótipo
** [[PROTÓTIPO NO GOOGLE AI STUDIO]](https://aistudio.google.com/apps/990b8fe9-1fc5-48c1-b262-4a4c0661d2f4?showPreview=true&showAssistant=true)

---

### 1. Identificação do Grupo
* **Instituição:** Faculdade Engenheiro Salvador Arena (FSA)
* **Curso:** Engenharia de Controle e Automação
* **Grupo:** [Inserir Identificação do Grupo]
* **Integrantes:**
    * Bruno Eduardo Mendes da Silva - RA: [062220019]
    * Rafael Bognar Soares da Silva - RA: [062220040]
    * João Victor Soares Rodrigues de Andrade - RA: [061230042]
    * Willian Balieiro Calvo - RA: [062220036]

---

### 2. Área Problema Selecionada
Selecione a trilha tecnológica do projeto (marque com um [x]):
* [ ] **Saúde 4.0:** Robótica Assistiva (Controladores Inteligentes/Fuzzy)
* [ ] **Smart Grid:** Eficiência Energética e Descarbonização
* [ ] **Agtech:** Automação de Precisão e Visão Computacional
* [X] **Logística Autônoma:** Coordenação de AGVs e Otimização de Rotas

### 3. Diagnóstico e Definição do Agente
* **Contexto:** Inserido na Indústria 4.0 e na automação logística industrial, o sistema opera em um ambiente de armazém inteligente onde múltiplos AGVs (Veículos Guiados Automatizados) circulam simultaneamente por corredores compartilhados com 5 cruzamentos críticos. O projeto foi desenvolvido como trabalho acadêmico de Engenharia de Controle e Automação, integrando uma Rede Neural Artificial (RNA/MLP) com uma camada de controle inteligente e o modelo de linguagem Gemini para análise e conclusão dos resultados.
* **Problema:** 
Em cenários de alta densidade de tráfego (100 AGVs simultâneos), a ausência de um sistema de coordenação inteligente nos cruzamentos gera conflitos iminentes de colisão — situações em que dois ou mais AGVs chegam ao mesmo ponto em uma janela de tempo crítica (≤ 0,25 s). Algoritmos de controle binários tradicionais (parar/prosseguir) resolvem o risco de colisão, mas introduzem atrasos acumulativos que comprometem a eficiência operacional e os prazos de entrega (JIT). O problema central é, portanto, equilibrar segurança e fluidez de forma adaptativa, considerando variáveis dinâmicas como urgência de entrega, distância ao destino e prioridade da carga.
* **Impacto:** A solução transforma as variáveis brutas de cada AGV (tempo restante, distância, prioridade) em decisões de controle preditivas via RNA, resultando em: detecção e mitigação de 76 conflitos sem nenhuma colisão; redução do tempo médio de entrega de 2,25 para 1,92 unidades após a compensação de velocidade (14,6% mais rápido que o cenário original); eficiência de controle de 69,74%; e geração automática de relatórios técnicos via Gemini. O sistema demonstra que inteligência computacional aplicada à logística elimina gargalos de forma preditiva, aumentando OEE, reduzindo desgaste mecânico e garantindo previsibilidade nas operações industriais.


#### Modelagem PEAS
| Componente | Descrição |
| :--- | :--- |
| **Performance (P)** |Taxa de conflitos evitados nos cruzamentos; tempo médio de entrega após compensação (meta: abaixo do tempo base); eficiência de controle (%) do sistema; número de AGVs que recuperaram velocidade após ceder passagem; acurácia da RNA na previsão de urgência (MAE, RMSE, R²) |
| **Ambiente (E)** | Armazém industrial simulado com 5 cruzamentos e corredores A–E; 100 AGVs operando simultaneamente com atributos dinâmicos (tempo restante, distância ao destino, prioridade de entrega); janela de tempo crítica de 0,25 s para detecção de conflito; dados gerados sinteticamente via NumPy com distribuição aleatória realista|
| **Atuadores (A)** | Ajuste de velocidade do AGV (redução temporária ao ceder passagem; compensação pós-cruzamento com limite de 90 km/h); definição do estado do semáforo virtual (VERDE / AMARELO / VERMELHO) por AGV; geração de alertas de conflito por cruzamento; exportação de histórico operacional em CSV; geração de conclusão técnica textual via Gemini |
| **Sensores (S)** | Tempo restante para entrega (min); distância até o destino (m); prioridade da entrega (0–100); cruzamento de destino e corredor do AGV; tempo estimado de chegada ao cruzamento (calculado por distância/velocidade); urgência prevista pela RNA (% contínuo entre 0–100) |

---

### 4. Arquitetura Lógica e Aprendizado
O **[AGV Inteligente]** opera através de uma arquitetura híbrida que garante segurança técnica e clareza para o usuário:

1.  **Módulo Preditivo (Etapa 3):** Utiliza uma Utiliza uma Rede Neural Artificial do tipo MLPRegressor (camadas ocultas 64→32, ativação ReLU, solver Adam) treinada com 5.000 amostras sintéticas para prever continuamente o índice de urgência de cada AGV (0–100%) a partir de três entradas: tempo restante para entrega, distância ao destino e prioridade da carga. A urgência prevista é a variável central que governa todas as decisões subsequentes do sistema..
2.  **Módulo de Controle (Etapa 2):** Um Com base na urgência prevista pela RNA, um sistema de regras classifica cada AGV em três estados operacionais — VERDE (urgência < 40%), AMARELO (40–70%) e VERMELHO (≥ 70%) — definindo prioridade de passagem, velocidade recomendada e distância segura. Ao detectar dois ou mais AGVs no mesmo cruzamento dentro de uma janela temporal crítica de 0,25 s, o módulo determina qual AGV cede passagem (menor urgência) e aplica redução de velocidade temporária, seguida de compensação automática pós-cruzamento (velocidade base + 15 km/h, limitada a 90 km/h)..
3.  **Camada Interpretativa:** Após a execução completa da simulação, a API do Gemini recebe um resumo estruturado dos resultados operacionais — total de AGVs, conflitos detectados, métricas de tempo e eficiência de controle — e gera dois outputs em linguagem natural: uma análise técnica dos conflitos por cruzamento e uma conclusão acadêmica completa explicando o funcionamento do sistema, o papel da RNA, a lógica de prevenção de colisões e os benefícios para a logística industrial.
---

### 5. Justificativa da Abordagem
Para o desenvolvimento do núcleo de inteligência deste projeto, foi selecionada a abordagem de **[Redes Neurais Artificiais (RNA) OU Algoritmos Evolutivos]**.

**Por que esta abordagem foi escolhida?**
* **Natureza do Problema:** O problema de coordenação de AGVs em cruzamentos simultâneos exige uma solução que lide com padrões não-lineares entre urgência, velocidade e risco de colisão, onde métodos estatísticos tradicionais — como regressão linear ou tabelas de decisão fixas — não conseguem capturar a variabilidade dinâmica do ambiente de forma confiável.
* **Capacidade de [Generalização/Otimização]:**A RNA foi escolhida pela sua alta capacidade de aprender correlações complexas entre as três variáveis de entrada (tempo restante, distância e prioridade) e o índice contínuo de urgência. Com 5.000 amostras de treinamento, o modelo aprende a generalizar para combinações de parâmetros nunca vistas, tornando o controle adaptativo e robusto a cenários imprevistos.
    * *[Se Evolutiva]:* A abordagem evolutiva foi escolhida para encontrar a configuração ótima de distribuição de recursos, onde o objetivo é minimizar o custo e a emissão de CO2 simultaneamente.
* **Escalabilidade:** O modelo permite a integração de novas variáveis de entrada — como nível de bateria do AGV, peso da carga ou condições do corredor — sem a necessidade de reestruturação completa da lógica de controle, bastando retreinar a RNA com os novos atributos.

---

### 6. Evidências Visuais e Desempenho
*Arquivos armazenados na pasta `/assets/images`.*

Arquivos armazenados na pasta /assets/images.
Imagem : Urgência dos AGVs por Estado de Semáforo
Gráfico de barras colorido (verde/amarelo/vermelho) exibindo o índice de urgência previsto pela RNA para cada um dos 100 AGVs, evidenciando a distribuição dos estados operacionais e a separação das faixas de decisão.

Imagem : Tempo Médio Estimado de Entrega — Original vs. Após Redução vs. Após Compensação
Gráfico de barras comparativo demonstrando a evolução do tempo médio de entrega nas três fases do controle: tempo base (2,25), após redução por conflito (2,82) e após compensação de velocidade (1,92), comprovando a eficácia do sistema em superar o desempenho original.

Imagem : Conflitos Detectados por Cruzamento
Gráfico de barras com a distribuição dos 76 conflitos detectados entre os 5 cruzamentos (Cruzamento_01 a Cruzamento_05), permitindo identificar os pontos de maior densidade de tráfego no armazém simulado.
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
2. **Importante:** Cadastre sua chave de API do Gemini no painel Secrets do Colab com o nome FESA_API_KEY para habilitar a camada interpretativa.

## 🤖 9. Apêndice de IA

Relato sobre o suporte de ferramentas de Inteligência Artificial Generativa no desenvolvimento:

* **Ferramentas:** Gemini (google-genai), ChatGPT, Claude.
* **Aplicação:** Apoio na estruturação do pipeline de simulação, revisão textual do README, sugestão de métricas de avaliação da RNA (MAE, RMSE, R²), organização do fluxo de ETL e geração automatizada da conclusão técnica acadêmica a partir dos resultados numéricos do sistema.
* **Validação:** Todos os resultados, métricas de desempenho e interpretações foram conferidos e validados tecnicamente pelo grupo, incluindo a verificação manual dos conflitos detectados, tempos médios calculados e eficiência de controle reportada.
---
© 2026 - Projeto de Inteligência Artificial - Faculdade Engenheiro Salvador Arena
