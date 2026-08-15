#!/usr/bin/env python3
"""Coleta dados eleitorais públicos (TSE / Brasil.io)."""

import os
from pathlib import Path
import requests
import pandas as pd

DATA_DIR = Path("data/raw/eleicoes")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Exemplo: resultados municipais TSE (ajuste ano/cargo conforme necessário)
TSE_BASE = "https://cdn.tse.jus.br/estatistica/sead/odonto"

def baixar_arquivo(url: str, destino: Path) -> bool:
    print(f"Baixando: {url}")
    r = requests.get(url, timeout=60)
    if r.status_code != 200:
        print(f"  Falha ({r.status_code})")
        return False
    destino.write_bytes(r.content)
    print(f"  OK → {destino}")
    return True

def coletar_araripina(ano: int = 2024):
    """Exemplo de filtro local após download."""
    # Após baixar CSVs do TSE, filtrar por SG_UE / NM_UE = Araripina
    # Código da UE de Araripina-PE: consultar tabela de municípios TSE
    pass

def main():
    print("=== Coleta de dados eleitorais ===")
    # 1. Baixar arquivos oficiais do TSE (candidatos / votos)
    # 2. Filtrar município (Araripina)
    # 3. Salvar em data/raw/eleicoes/
    # 4. (Opcional) Gerar resumo em Markdown
    print("Coleta finalizada.")

if __name__ == "__main__":
    main()
