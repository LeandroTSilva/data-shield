import json

def render_pipeline_report(file_name, validation_report, output_path):
    response = {
        "arquivo_original": file_name,
        "status": "Sucesso",
        "metricas": {
            "linhas_processadas": validation_report["total_rows"],
            "colunas_detectadas": validation_report["total_columns"],
            "duplicadas_removidas": validation_report["duplicate_rows"]
        },
        "inconsistencias_encontradas": validation_report["null_values"],
        "local_salvamento": output_path
    }
    return json.dumps(response, ensure_ascii=False, indent=4)