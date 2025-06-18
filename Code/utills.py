import json
import os

def salvar_personagem(personagem, nome_personagem):
    a = personagem
    b = str(nome_personagem) + '.json'
    try:    
        with open(b, 'w') as arquivo:
            json.dump(a, arquivo, 'utf-8')
    except json.JSONDecodeError:
        print('Não foi possivel salvar o personagem')
        return