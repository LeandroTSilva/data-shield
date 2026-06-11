import pandas as pd
import numpy as np

def standardize_data(df):
    df = df.copy()
    
    # 1. Remove duplicados estruturais
    df = df.drop_duplicates().reset_index(drop=True)
    
    # 2. Uniformiza todos os tipos de nulos textuais para o padrão NaN do numpy
    nulos_falsos = [r'^\s*$', r'(?i)^null$', r'(?i)^nan$', r'(?i)^none$']
    for expressao in nulos_falsos:
        df = df.replace(expressao, np.nan, regex=True)
        
    # 3. Tratamento cirúrgico por tipo de coluna (Foco em Analytics)
    for col in df.columns:
        
        # Caso A: Colunas de Texto / Categóricas
        if df[col].dtype == 'object' or str(df[col].dtype) == 'string':
            df[col] = df[col].astype(str).str.strip()
            # Se o cast forçou textos a virarem 'nan', desfaz para NaN real
            df[col] = df[col].replace(r'(?i)^nan$', np.nan, regex=True)
            # Para análise de dados, nulos em texto viram uma categoria explícita
            df[col] = df[col].fillna("NÃO INFORMADO")
            
        # Caso B: Colunas Numéricas (Int/Float)
        elif pd.api.types.is_numeric_dtype(df[col]):
            # Regra de Negócio para Zeros: Se a coluna for de identificação, idade ou valores monetários,
            # um '0' geralmente indica dado faltante. Vamos convertê-lo em NaN para não quebrar médias.
            col_lower = str(col).lower()
            termos_criticos = ['id', 'idade', 'preco', 'preço', 'valor', 'total', 'salario', 'salário']
            
            if any(termo in col_lower for termo in termos_criticos):
                df[col] = df[col].replace(0, np.nan)
            
            # NOTA: Mantemos números ausentes como NaN/None. Ferramentas como PowerBI e bibliotecas
            # de IA do Python ignoram o NaN ao calcular médias, o que mantém sua análise precisa.

        # Caso C: Colunas de Data
        if 'data' in str(col).lower() or 'date' in str(col).lower():
            try:
                # errors='coerce' transforma datas inválidas ou vazias em NaT (Not a Time) automaticamente
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except:
                pass
                
    return df