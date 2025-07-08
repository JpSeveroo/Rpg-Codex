import item
from InquirerPy import inquirer
from ficha import Personagem
import os

#código corrigido

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

def equips(personagem):
    print('-'*35)
    try:
        print('|' + f'Cabeça: {personagem.equipamento.itens['Cabeça']['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Cabeça: '.center(33) + '|')
    try:
        print('|' + f'Corpo: {personagem.equipamento.itens['Corpo']['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Corpo: '.center(33) + '|')
    try:
        print('|' + f'Pés: {personagem.equipamento.itens['Pés']['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Pés: '.center(33) + '|')
    try:
        print('|' + f'Mãos: {personagem.equipamento.itens['Mãos']['item'].nome}'.center(33) + '|')
    except:
        print('|' + 'Mãos: '.center(33) + '|')
    print('|' + f'Vida: {personagem.vida_atual}'.center(33) + '|')
    print('|' + f'Mana: {personagem.status['mana']}'.center(33) + '|')
    print('-'*35)

def interface_inv(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    equips(personagem)
    personagem.equipamento = equipamento
    a = inquirer.select(message='Qual equipamento você deseja alterar ?', choices=['Cabeça', 'Corpo', 'Pés', 'Mãos', 'Utilizaveis', 'Sair']).execute()
    disponiveis = []
    for i in personagem.inventario :
        if i.categoria == a :
            disponiveis.append(i)
    if a == 'Utilizaveis':
        if len(disponiveis) == 0 :
            print('Não há nenhum utilizavel disponivel')
            input('Pressione enter para voltar...')
            interface_inv(personagem)
        nomes_itens = []
        for i in range(len(disponiveis)):
            nomes_itens.append(disponiveis[i].nome)
        b = inquirer.select(message=f'Qual o item que você deseja utilizar: ', choices=nomes_itens).execute()
        if personagem.inventario[nomes_itens.index(b)].efeitos[0][0] == 'vida_atual':
            personagem.vida_atual += personagem.inventario[nomes_itens.index(b)].efeitos[0][1]
            input()
            interface_inv(personagem)
        elif personagem.inventario[nomes_itens.index(b)].efeitos[0][0] == 'mana':
            personagem.status['mana'] += personagem.inventario[nomes_itens.index(b)].efeitos[0][1]
            interface_inv(personagem)
    elif a != 'Sair':
        if equipamento.itens[a]['equipado'] == False:
            if len(disponiveis) == 0 :
                print('Não há nenhum equipamento disponivel para essa parte')
                input('Pressione enter para voltar...')
                interface_inv(personagem)
            nomes_itens = []
            for i in range(len(disponiveis)):
                nomes_itens.append(disponiveis[i].nome)
            b = inquirer.select(message=f'Qual o item que você deseja equipar na(o) {a}: ', choices=nomes_itens).execute()
            equipamento.itens[a]['item'] = disponiveis[nomes_itens.index(b)]
            equipando(personagem, disponiveis[nomes_itens.index(b)], a)
            interface_inv(personagem)
        else:
            print(f'Não é possivel equipar um item na(o) {a}')
            c = inquirer.confirm(message='Você deseja desequipar ?').execute()
            if c == True:
                desequipando(personagem, equipamento.itens[a]['item'], a)
                interface_inv(personagem)
            if c == False:
                interface_inv(personagem)

def equipando(personagem, item, parte):
    for i in item.efeitos:
        personagem.pericias[i[0]] += i[1]
        equipamento.itens[parte]['equipado'] = True

def desequipando(personagem, item, parte):
    for i in item.efeitos:
        personagem.pericias[i[0]] -= i[1]
        equipamento.itens[parte]['equipado'] = False
        equipamento.itens[parte]['item'] = ''

if __name__ == '__main__':
    p = Personagem()
    p.inventario.append(item.lista_itens[0])
    p.inventario.append(item.lista_itens[4])
    p.inventario.append(item.lista_itens[5])
    p.inventario.append(item.lista_itens[6])
    p.inventario.append(item.lista_itens[7])
    p.inventario.append(item.lista_itens[8])
    p.inventario.append(item.lista_itens[9])
    interface_inv(p)