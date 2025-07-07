import item
from InquirerPy import inquirer
from ficha import Personagem
from interface import personagem_escolhido
from os import system

lista_de_nomes_de_itens = [i.nome for i in item.lista_itens]

class Equipamento:
    def __init__(self):
        self.itens = { 'cabeca' : {
            'equipado' : False,
            'item' : ''
        },
        'corpo' : {
            'equipado' : False,
            'item' : ''
        },
        'pes' : {
            'equipado' : False,
            'item' : ''
        },
        'maos' : {
            'equipado' : False,
            'item' : ''
        } 
        }

equipamento = Equipamento()

def equips(a):
    print('-'*35)
    try:
        print('|' + f'Cabeça : {a.cabeca['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Não há itens equipados na Cabeça!'.center(33) + '|')
    try:
        print('|' + f'Corpo : {a.corpo['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Não há itens equipados no Corpo!'.center(33) + '|')
    try:
        print('|' + f'Pés : {a.pes['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Não há itens equipados nos Pés!'.center(33) + '|')
    try:
        print('|' + f'Mãos : {a.maos['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Não há itens equipados nas Mãos!'.center(33) + '|')
    print('-'*35)

def interface_inv(personagem):
    system('clear')
    equips(equipamento)
    opcoes = [
        {'name':'Cabeça', 'value':'cabeca'},
        {'name':'Corpo', 'value':'cabeca'}
    ]
    a = inquirer.select(message='Qual equipamento você deseja alterar ?', choices=opcoes).execute()
    print(a)

if __name__ == '__main__':
    item.load_itens()
    p = Personagem()
    p.inventario.append(item.lista_itens[4])
    p.inventario.append(item.lista_itens[5])
    p.inventario.append(item.lista_itens[6])
    p.inventario.append(item.lista_itens[7])
    p.inventario.append(item.lista_itens[8])
    p.inventario.append(item.lista_itens[9])
    interface_inv(p)