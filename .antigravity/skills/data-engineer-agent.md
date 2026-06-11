# Skill: Engenheiro de Dados Autônomo

## Contexto do Espaço de Trabalho
Este projeto possui um pipeline de dados baseado no padrão MVC localizado em `./.opencode/skills/data-engineer-agent/main.py`. Ele monitora a pasta `./docs` e gera arquivos limpos em `./output`.

## Instruções de Ativação
Sempre que o usuário pedir para "limpar dados", "rodar o pipeline", "analisar a pasta docs" ou "gerar relatórios de qualidade de dados", você deve agir de forma autônoma.

## Fluxo de Execução do Agente Antigravity
1. Utilize a sua ferramenta de execução de código (`code_execution` ou terminal Bash) para rodar o comando:
   `python ./.opencode/skills/data-engineer-agent/main.py`
2. O script retornará um log estruturado em JSON com as inconsistências encontradas.
3. **Gere um Artefato (Artifact):** Em vez de apenas jogar o texto no chat, crie um Artefato rico do Antigravity contendo a tabela de dados faltantes, duplicados eliminados e o link direto para o arquivo final gerado na pasta `output`.

# Comando do Workspace: /start

## Ativação
- **Gatilho:** /start ou "iniciar processamento"

## Comportamento Esperado (VS Code / Antigravity IDE)
O usuário utiliza este comando após ter arrastado manualmente os arquivos brutos para a pasta `./docs/`.

## Fluxo de Trabalho:
1. Assim que o usuário digitar `/start`, verifique via terminal se a pasta `./docs/` contém arquivos.
2. Se a pasta estiver vazia, avise amigavelmente: *"Alerta: Não encontrei arquivos na pasta `docs/`. Por favor, arraste seus arquivos para lá antes de digitar `/start`."*
3. Se houver arquivos, execute o pipeline imediatamente rodando:
   `python ./.opencode/skills/data-engineer-agent/main.py`
4. Pegue o relatório gerado e exiba-o no chat em formato de tabela ou através de um Artefato (Artifact) do Antigravity.