
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

delay_digitar = 0.01


def limpar_tela() -> None:
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True, check=False)


def _caminho_arquivo(nome: str) -> Path:
    return DATA_DIR / f"{nome}.json"


def salvar_infos(nome: str, dados: object) -> None:
    arquivo = _caminho_arquivo(nome)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with arquivo.open("w", encoding="utf-8") as destino:
        json.dump(dados, destino, ensure_ascii=False, indent=4)


def load_infos(nome: str) -> Any | None:
    arquivo = _caminho_arquivo(nome)

    if not arquivo.is_file():
        return None

    try:
        with arquivo.open("r", encoding="utf-8") as origem:
            return json.load(origem)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Erro ao carregar {arquivo.name}: {exc}")
        return None


def cripto(texto: str) -> str:
    return hashlib.md5(texto.encode()).hexdigest()


def digitar(texto: str) -> None:
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay_digitar)

    print()


def tempo_digitar(novo_delay: float) -> None:
    global delay_digitar
    delay_digitar = novo_delay
