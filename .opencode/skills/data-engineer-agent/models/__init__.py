"""
Pacote de Modelos (Model) - Data Quality Pipeline
Centraliza as operações de entrada, validação e transformação de dados.
"""

# pyrefly: ignore [missing-import]
from .reader import load_file
# pyrefly: ignore [missing-import]
from .validator import check_inconsistencies
# pyrefly: ignore [missing-import]
from .transformer import standardize_data

# Define explicitamente o que o pacote exporta ao usar "from models import *"
__all__ = [
    "load_file",
    "check_inconsistencies",
    "standardize_data"
]