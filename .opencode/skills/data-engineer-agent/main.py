import os
import sys

# --- MONKEYPATCH FOR OPENPYXL COMPATIBILITY ---
try:
    from openpyxl.descriptors.serialisable import Serialisable
    from openpyxl.descriptors.base import Typed
    from openpyxl.styles.borders import Side

    # Patch 1: Coerce string borders to Side objects
    original_set = Typed.__set__
    def patched_set(self, instance, value):
        if self.expected_type is Side and isinstance(value, str):
            try:
                value = Side(style=value)
            except Exception:
                value = Side()
        return original_set(self, instance, value)
    Typed.__set__ = patched_set

    # Patch 2: Map 'builtInId' to 'builtinId' to avoid TypeError
    original_from_tree = Serialisable.from_tree.__func__
    @classmethod
    def patched_from_tree(cls, node):
        if 'builtInId' in node.attrib:
            node.attrib['builtinId'] = node.attrib.pop('builtInId')
        return original_from_tree(cls, node)
    Serialisable.from_tree = patched_from_tree
except Exception:
    pass
# ----------------------------------------------

# Garante que o Python encontre os módulos locais do MVC
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import reader, validator, transformer
from views import presenter

def main():
    # Caminhos baseados na raiz do projeto
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../docs"))
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../output"))
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(input_dir) or os.listdir(input_dir) == []:
        print('{"erro": "A pasta \'docs\' está vazia ou não existe."}')
        return

    # Varre a pasta docs procurando arquivos válidos
    for file_name in os.listdir(input_dir):
        if file_name.startswith('.') or os.path.isdir(os.path.join(input_dir, file_name)):
            continue
            
        input_path = os.path.join(input_dir, file_name)
        
        try:
            # 1. MODEL: Lê o dado bruto
            df_raw = reader.load_file(input_path)
            
            # 2. MODEL: Analisa inconsistências antes de limpar
            inconsistencies = validator.check_inconsistencies(df_raw)
            
            # 3. MODEL: Trata e padroniza os dados
            df_clean = transformer.standardize_data(df_raw)
            
            # 4. Salva o resultado limpo na pasta Output
            output_file_name = f"clean_{file_name}"
            output_path = os.path.join(output_dir, output_file_name)
            
            # Salva mantendo a extensão original (simplificado para CSV/Excel)
            if file_name.endswith('.csv'):
                df_clean.to_csv(output_path, index=False)
            else:
                df_clean.to_excel(output_path, index=False)
                
            # 5. VIEW: Exibe o relatório estruturado para o OpenCode
            report = presenter.render_pipeline_report(file_name, inconsistencies, output_path)
            print(report)
            
        except Exception as e:
            print(f'{{"erro": "Falha ao processar {file_name}. Motivo: {str(e)}"}}')

if __name__ == "__main__":
    main()