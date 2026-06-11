# Data Quality Pipeline 🚀

Um pipeline robusto e inteligente de Engenharia de Dados focado em **Data Quality (Higienização, Validação e Padronização)**. O projeto foi arquitetado sob o padrão **MVC (Model-View-Controller)** em Python puro, garantindo portabilidade absoluta e isolamento de escopo.

O grande diferencial deste repositório é o suporte nativo a agentes de IA, permitindo que o pipeline seja orquestrado via comandos de linguagem natural (*Slash Commands*) dentro do **OpenCode Desktop** e do **Google Antigravity**, além de automações por atalhos no **VS Code**.

---

## 🛠️ Funcionalidades Principais

* **Arquitetura MVC:** Separação clara entre ingestão/transformação de dados (`Models`), relatórios de execução (`Views`) e o orquestrador do pipeline (`Controller`).
* **Tratamento Avançado de Nulos & Anomalias:** Identificação e tratamento inteligente de nulos "falsos" (strings como `NaN`, `null`, `None`), campos de texto vazios e detecção de zeros (`0`) suspeitos em colunas críticas (IDs, Idades, Valores Monetários).
* **Padronização para Analytics:** Formatação automática de strings (remoção de espaços, ajuste de caixa) e conversão segura de campos de data para formatos aceitos por ferramentas de BI (Power BI, Tableau) e Machine Learning.
* **Compatibilidade Multiplataforma (AI Ready):** Mapeamento de Skills customizadas para que assistentes baseados em LLMs gerenciem o pipeline de forma autônoma.

---

## 📁 Estrutura do Projeto

```text
data-quality-pipeline/
├── .antigravity/           # Configurações de agente para o Google Antigravity
├── .opencode/              # Manifesto de habilidades (Skills) para o OpenCode Desktop
├── .vscode/                # Tasks de automação para execução rápida no VS Code
├── docs/                   # INGESTÃO: Pasta para os arquivos brutos (CSV, XLSX, JSON)
├── output/                 # CURADORIA: Pasta para os arquivos limpos e prontos para análise
├── models/                 # Camada interna de lógica e regras de Data Quality
├── views/                  # Camada de logs estruturados em JSON para o terminal e IAs
├── main.py                 # Controlador geral do pipeline
└── setup.py                # Script automatizado de verificação de ambiente e dependências
