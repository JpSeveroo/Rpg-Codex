import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def limpar_tela():
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True, check=False)
    
def salvar_infos(path, data):
    a = Path(str(path) + '.json')
    try:
        with a.open("w") as arquivo:
            json.dump(data, arquivo, indent=4)
    except json.JSONDecodeError:
        print('Não foi possivel salvar as infos')

def cripto(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def load_infos(path):
    a = Path(str(path) + '.json')
    if a.exists:
        try:
            with a.open("r") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print('Não foi possivel ler o arquivo')

delay_digitar = 0.01

def digitar(texto):
    for caractere in str(texto):
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay_digitar)
    print()

def tempo_digitar(novo_delay):
    global delay_digitar
    delay_digitar = novo_delay

if __name__ == '__main__':
    a = load_infos('usuarios')
    print(a)