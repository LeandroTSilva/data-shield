import pandas as pd
import os

def parse_raw_dataframe(df):
    header_idx = None
    for idx, row in df.iterrows():
        row_strs = [str(val).strip().lower() for val in row if pd.notna(val)]
        if any(keyword in row_strs for keyword in ["cadastro", "nome", "tip.", "tipo"]):
            header_idx = idx
            break
            
    if header_idx is not None:
        header_row = df.iloc[header_idx]
        df.columns = header_row
        df = df.iloc[header_idx + 1:].reset_index(drop=True)
        
        # Filtra colunas válidas (descarta vazias, nulas ou Unnamed)
        valid_cols = []
        for col in df.columns:
            if pd.isna(col) or str(col).strip() == "" or str(col).startswith("Unnamed:"):
                continue
            valid_cols.append(col)
        df = df[valid_cols]
        
        # Remove linhas de rodapé/metadados mantendo apenas as que têm identificador numérico na primeira coluna
        if len(df.columns) > 0:
            first_col = df.columns[0]
            is_numeric = pd.to_numeric(df[first_col], errors='coerce').notna()
            df = df[is_numeric].reset_index(drop=True)
            
    return df

def load_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.csv':
        df = pd.read_csv(file_path, header=None)
        return parse_raw_dataframe(df)
    elif ext in ['.xlsx', '.xls']:
        df = pd.read_excel(file_path, header=None)
        return parse_raw_dataframe(df)
    elif ext == '.json':
        df = pd.read_json(file_path)
        if all(isinstance(c, int) for c in df.columns):
            return parse_raw_dataframe(df)
        return df
    else:
        raise ValueError(f"Formato {ext} não suportado.")