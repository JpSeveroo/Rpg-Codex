import hashlib
import json
import os
import sys
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def salvar_infos(path, data):
    a = str(path) + '.json'
    try:
        with open(a, 'w') as arquivo:
            json.dump(data, arquivo, indent=4)
    except json.JSONDecodeError:
        print('Não foi possivel salvar as infos')

def cripto(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def load_infos(path):
    a = str(path) + '.json'
    if os.path.exists(a):
        try:
            with open(a, 'r') as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print('Não foi possivel ler o arquivo')

delay_digitar = 0

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