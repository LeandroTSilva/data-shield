---
name: env-setup
description: Skill para preparar o ambiente. Ative imediatamente se o usuário digitar "/setup", "configurar ambiente" ou "instalar dependências".
---

# Skill de Configuração do Sistema (/setup)

Você é o assistente de infraestrutura do projeto. Sempre que o usuário digitar `/setup`, você deve executar o script de automação para preparar o ambiente.

## Instruções de Execução:
1. Abra o terminal integrado do OpenCode.
2. Execute o comando: `python setup.py`
3. Monitore a saída do terminal.
4. Quando o script terminar, exiba na tela do chat o bloco final de sucesso ou as orientações de erro que o próprio script gerou, garantindo que o usuário saiba que terminou.

## Restrições:
- Não tente instalar pacotes manualmente usando comandos soltos; confie apenas no `setup.py`.