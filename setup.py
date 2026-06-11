import os
import sys
import subprocess

def imprimir_sucesso(texto):
    print(f"✅ {texto}")

def imprimir_alerta(texto):
    print(f"⚠️ {texto}")

def imprimir_erro(texto):
    print(f"❌ {texto}")

def verificar_sistema():
    print("--- 🔍 VERIFICANDO REQUISITOS DO SISTEMA ---")
    
    # 1. Verifica a versão do Python (Recomendado >= 3.8)
    versao_atual = sys.version_info
    if versao_atual.major < 3 or (versao_atual.major == 3 and versao_atual.minor < 8):
        imprimir_erro(f"Ops! Sua versão do Python é a {versao_atual.major}.{versao_atual.minor}.")
        print("\n💡 Como resolver:")
        print("Este pipeline precisa do Python 3.8 ou superior para funcionar bem.")
        print("Por favor, atualize o Python em https://www.python.org/downloads/ antes de continuar.\n")
        sys.exit(1)
    else:
        imprimir_sucesso(f"Versão do Python adequada: {versao_atual.major}.{versao_atual.minor}")

def preparar_pastas():
    print("\n--- 📁 ESTRUTURANDO AS PASTAS DO PROJETO ---")
    pastas = ["docs", "output"]
    
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            imprimir_sucesso(f"Pasta '{pasta}/' criada com sucesso.")
        else:
            imprimir_alerta(f"Pasta '{pasta}/' já existia. Mantida intacta.")

def instalar_dependencias():
    print("\n--- 📦 INSTALANDO BIBLIOTECAS (PANDAS & OPENPYXL) ---")
    
    if not os.path.exists("requirements.txt"):
        imprimir_erro("Arquivo 'requirements.txt' não foi encontrado na raiz do projeto!")
        print("\n💡 Como resolver:")
        print("Crie um arquivo de texto chamado 'requirements.txt' na mesma pasta deste script e escreva dentro dele:")
        print("pandas>=2.0.0")
        print("openpyxl>=3.1.0\n")
        sys.exit(1)
        
    try:
        print("Instalando dependências via pip... Isso pode levar alguns segundos.")
        # Executa o pip install de forma silenciosa e controlada
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        imprimir_sucesso("Todas as bibliotecas foram instaladas com sucesso!")
    except Exception as e:
        imprimir_erro("Falha ao instalar as bibliotecas automaticamente.")
        print("\n💡 Como resolver:")
        print("Tente instalar manualmente abrindo o seu terminal e digitando o comando:")
        print("pip install -r requirements.txt")
        print(f"\nErro técnico para geeks: {e}\n")
        sys.exit(1)

def instrucoes_finais():
    print("\n" + "="*50)
    print("🎉 TUDO PRONTO! SEU AMBIENTE ESTÁ PRONTINHO PARA USO!")
    print("="*50)
    print("\nPróximos passos para usar o seu Agente:")
    print("1. Jogue seus arquivos sujos (CSV, Excel ou JSON) dentro da pasta 'docs/'.")
    print("2. Abra o OpenCode Desktop ou o Google Antigravity neste projeto.")
    print("3. Peça para a IA: 'Execute o pipeline de dados para mim'.")
    print("\nSe preferir rodar direto pelo terminal do VS Code ou sistema, use o comando:")
    print("python ./.opencode/skills/data-engineer-agent/main.py\n")

if __name__ == "__main__":
    try:
        verificar_sistema()
        preparar_pastas()
        instalar_dependencias()
        instrucoes_finais()
    except KeyboardInterrupt:
        print("\n\n❌ Configuração cancelada pelo usuário.")