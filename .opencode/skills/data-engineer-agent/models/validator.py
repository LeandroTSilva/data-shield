import pandas as pd
import numpy as np

def check_inconsistencies(df):
    # Criamos uma cópia para não alterar o dado original nesta fase de checagem
    df_analise = df.copy()
    
    # 1. Desmascara nulos textuais comuns em sistemas legados
    nulos_falsos = [r'^\s*$', r'(?i)^null$', r'(?i)^nan$', r'(?i)^none$']
    for expressao in nulos_falsos:
        df_analise = df_analise.replace(expressao, np.nan, regex=True)
        
    report = {
        "total_rows": int(df_analise.shape[0]),
        "total_columns": int(df_analise.shape[1]),
        "null_values": df_analise.isnull().sum().to_dict(),
        "duplicate_rows": int(df_analise.duplicated().sum()),
        "zeros_suspeitos": {}
    }
    
    # 2. Mapeia colunas numéricas que possuem o valor ZERO (pode ser uma anomalia)
    for col in df_analise.select_dtypes(include=[np.number]).columns:
        qtd_zeros = int((df_analise[col] == 0).sum())
        if qtd_zeros > 0:
            report["zeros_suspeitos"][col] = qtd_zeros
            
    # Filtra o dicionário para exibir apenas colunas que realmente possuem nulos
    report["null_values"] = {k: int(v) for k, v in report["null_values"].items() if v > 0}
    
    return report