import item
from InquirerPy import inquirer
from ficha import Personagem
from interface import personagem_escolhido
from os import system

lista_de_nomes_de_itens = [i.nome for i in item.lista_itens]

class Equipamento:
    def __init__(self):
        self.cabeca = {
            'equipado' : False,
            'item' : ''
        }
        self.corpo = {
            'equipado' : False,
            'item' : ''
        }
        self.pes = {
            'equipado' : False,
            'item' : ''
        }
        self.maos = {
            'equipado' : False,
            'item' : ''
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
    lista_nomes = []
    for a in personagem.inventario :
        lista_nomes.append(a.nome)
    a = inquirer.select(message='Selecione um item ', choices=lista_nomes).execute()
    a = lista_de_nomes_de_itens.index(a)
    b = inquirer.select(message='Selecione onde você deseja equipar', choices=['Cabeça', 'Corpo', 'Pés', 'Mãos']).execute()
    if b == 'Cabeça':
        equipamento.cabeca['item'] = item.lista_itens[a]
        equipamento.cabeca['equipado'] = True
        interface_inv(personagem)
    elif b == 'Corpo':
        equipamento.corpo['item'] = item.lista_itens[a]
        equipamento.corpo['equipado'] = True
        interface_inv(personagem)
    elif b == 'Pés':
        equipamento.pes['item'] = item.lista_itens[a]
        equipamento.pes['equipado'] = True
        interface_inv(personagem)
    elif b == 'Mãos':
        equipamento.maos['item'] = item.lista_itens[a]
        equipamento.maos['equipado'] = True
        interface_inv(personagem)

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