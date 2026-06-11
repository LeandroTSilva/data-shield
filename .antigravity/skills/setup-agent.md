# Comando do Sistema: /setup

## Ativação Rápida
- **Gatilho:** /setup

## Comportamento Esperado
Quando o usuário enviar a mensagem `/setup`, você deve ignorar qualquer outra conversa paralela e iniciar o pipeline de configuração do workspace imediatamente.

## Passos Autônomos:
1. Chame a ferramenta `code_execution` para rodar o comando `python setup.py`.
2. Capture o log gerado pelo terminal.
3. Se o status for de sucesso, responda no chat com uma mensagem curta e amigável: *"Ambiente configurado com sucesso! As pastas `docs` e `output` estão prontas para uso."*
4. Se o script apontar falta de requisitos (como Python desatualizado), formate o aviso em um card visual para o usuário.