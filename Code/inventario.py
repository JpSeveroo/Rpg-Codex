import item
from InquirerPy import inquirer
from ficha import Personagem
from os import system

lista_de_nomes_de_itens = [i.nome for i in item.lista_itens]

class Equipamento:
    def __init__(self):
        self.itens = { 
        'Cabeça' : {
            'equipado' : False,
            'item' : ''
        },
        'Corpo' : {
            'equipado' : False,
            'item' : ''
        },
        'Pés' : {
            'equipado' : False,
            'item' : ''
        },
        'Mãos' : {
            'equipado' : False,
            'item' : ''
        } 
        }

equipamento = Equipamento()

def equips(a):
    print('-'*35)
    try:
        print('|' + f'Cabeça: {a.itens['Cabeça']['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Cabeça: '.center(33) + '|')
    try:
        print('|' + f'Corpo: {a.itens['Corpo']['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Corpo: '.center(33) + '|')
    try:
        print('|' + f'Pés: {a.itens['Pés']['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Pés: '.center(33) + '|')
    try:
        print('|' + f'Mãos: {a.itens['Mãos']['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Mãos: '.center(33) + '|')
    print('-'*35)

def interface_inv(personagem):
    system('clear')
    equips(equipamento)
    personagem.equipamento = equipamento
    a = inquirer.select(message='Qual equipamento você deseja alterar ?', choices=['Cabeça', 'Corpo', 'Pés', 'Mãos', 'Sair']).execute()
    if a != 'Sair':
        disponiveis = []
        for i in personagem.inventario :
            if i.categoria == a :
                disponiveis.append(i)
        if len(disponiveis) == 0 :
            print('Não há nenhum equipamento disponivel para essa parte')
            input('Pressione enter para voltar...')
            interface_inv(personagem)
        nomes_itens = []
        for i in range(len(disponiveis)):
            nomes_itens.append(disponiveis[i].nome)
        b = inquirer.select(message=f'Qual o item que você deseja equipar na(o) {a}: ', choices=nomes_itens).execute()
        equipamento.itens[a]['item'] = disponiveis[nomes_itens.index(b)]
        interface_inv(personagem)
    else:
        pass

if __name__ == '__main__':
    p = Personagem()
    p.inventario.append(item.lista_itens[4])
    p.inventario.append(item.lista_itens[5])
    p.inventario.append(item.lista_itens[6])
    p.inventario.append(item.lista_itens[7])
    p.inventario.append(item.lista_itens[8])
    p.inventario.append(item.lista_itens[9])
    interface_inv(p)