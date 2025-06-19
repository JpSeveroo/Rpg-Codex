import json
import os

def salvar_infos(path, data):
    a = str(path) + '.json'
    try:
        with open(a, 'w') as arquivo:
            json.dump(data, arquivo, indent=4)
    except json.JSONDecodeError:
        print('Não foi possivel salvar as infos')

def load_infos(path):
    a = str(path) + '.json'
    if os.path.exists(a):
        try:
            with open(a, 'r') as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print('Não foi possivel ler o arquivo')

if __name__ == '__main__':
    a = load_infos('usuarios')
    print(a)