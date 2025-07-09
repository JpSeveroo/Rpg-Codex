import item
from utills import digitar
from rich.text import Text
from rich.console import Console
from InquirerPy import inquirer
from ficha import Personagem
import os

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
escolhido = ''

def equips(personagem):
    print('-'*35 + ' '*10 + '-'*35)

    try:
        print('|' + f'Cabeça: {personagem.equipamento.itens['Cabeça']['item'].nome}'.ljust(33) + '|' + ' '*10 + '|' + f'Acrobacia: {personagem.pericias['acrobacia']}'.center(33) + '|')
    except:
        print('|' + 'Cabeça: '.ljust(33) + '|'+ ' '*10 + '|' + f'Acrobacia: {personagem.pericias['acrobacia']}'.center(33) + '|')

    print('|' + '-'*33 + '|'+ ' '*10 + '|' + f'Blefar: {personagem.pericias['blefar']}'.center(33) + '|')

    try:
        print('|' + f'Corpo: {personagem.equipamento.itens['Corpo']['item'].nome}'.ljust(33) + '|'+ ' '*10 + '|' + f'Mira: {personagem.pericias['mira']}'.center(33) + '|')
    except:
        print('|' + 'Corpo: '.ljust(33) + '|'+ ' '*10 + '|' + f'Mira: {personagem.pericias['mira']}'.center(33) + '|')

    print('|' + '-'*33 + '|'+ ' '*10 + '|' + f'Diplomacia: {personagem.pericias['diplomacia']}'.center(33) + '|')

    try:
        print('|' + f'Pés: {personagem.equipamento.itens['Pés']['item'].nome}'.ljust(33) + '|'+ ' '*10 + '|' + f'Furtividade: {personagem.pericias['furtividade']}'.center(33) + '|')
    except:
        print('|' + 'Pés: '.ljust(33) + '|'+ ' '*10 + '|' + f'Furtividade: {personagem.pericias['furtividade']}'.center(33) + '|')

    print('|' + '-'*33 + '|'+ ' '*10 + '|' + f'Percepção: {personagem.pericias['percepcao']}'.center(33) + '|')

    try:
        print('|' + f'Mãos: {personagem.equipamento.itens['Mãos']['item'].nome}'.ljust(33) + '|'+ ' '*10 + '|' + f'Mãos Rápidas: {personagem.pericias['maos rapidas']}'.center(33) + '|')
    except:
        print('|' + 'Mãos: '.ljust(33) + '|'+ ' '*10 + '|' + f'Mãos Rápidas: {personagem.pericias['maos rapidas']}'.center(33) + '|')

    print('|' + '-'*33 + '|'+ ' '*10 + '|' + f'Mano a Mano: {personagem.pericias['mano a mano']}'.center(33) + '|')

    print('|' + f'Vida: {personagem.vida_atual}'.center(33) + '|'+ ' '*10 + '|' + f'Resistência: {personagem.pericias['resistencia']}'.center(33) + '|')

    print('|' + f'Mana: {personagem.status['mana']}'.center(33) + '|'+ ' '*10 + '-'*35)

    print('-'*35)

def interface_inv(personagem):
    global escolhido
    escolhido = ''
    os.system('cls' if os.name == 'nt' else 'clear')
    equips(personagem)
    personagem.equipamento = equipamento
    disponiveis = []
    a = inquirer.select(message='Qual equipamento você deseja alterar ?', choices=['Cabeça', 'Corpo', 'Pés', 'Mãos', 'Utilizaveis', 'Sair']).execute()
    for i in personagem.inventario :
        if i.categoria == a :
            disponiveis.append(i)
    escolhido = a
    opcoes = {
        'Cabeça': equip_itens,
        'Corpo' : equip_itens,
        'Pés' : equip_itens,
        'Mãos' : equip_itens,
        'Utilizaveis' : utilizaveis,
        'Sair' : sair
    }
    a = opcoes.get(a)
    if a:
        a(personagem, disponiveis)

def equip_itens(personagem, disponiveis):
    global escolhido
    if equipamento.itens[escolhido]['equipado'] == False:
        if len(disponiveis) == 0 :
            print('Não há nenhum equipamento disponivel para essa parte')
            input('Pressione enter para voltar...')
            interface_inv(personagem)
            return
        nomes_itens = []
        for i in range(len(disponiveis)):
            nomes_itens.append(disponiveis[i].nome)
        b = inquirer.select(message=f'Qual o item que você deseja equipar na(o) {escolhido}: ', choices=nomes_itens).execute()
        equipamento.itens[escolhido]['item'] = disponiveis[nomes_itens.index(b)]
        equipando(personagem, disponiveis[nomes_itens.index(b)], escolhido)
        interface_inv(personagem)
    else:
        print(f'Não é possivel equipar um item na(o) {escolhido}')
        c = inquirer.confirm(message='Você deseja desequipar ?').execute()
        if c == True:
            desequipando(personagem, equipamento.itens[escolhido]['item'], escolhido)
            interface_inv(personagem)
        if c == False:
            interface_inv(personagem)

def sair(personagem, disponiveis):
    return personagem, disponiveis

def utilizaveis(personagem, disponiveis):
    nomes_itens = []
    for i in range(len(disponiveis)):
        nomes_itens.append(disponiveis[i].nome)
    if not nomes_itens :
        print('Não há nenhum utilizavel disponivel')
        input('Pressione enter para voltar...')
        interface_inv(personagem)
        return
    b = inquirer.select(message=f'Qual o item que você deseja utilizar: ', choices=nomes_itens).execute()
    print(disponiveis[nomes_itens.index(b)].nome)
    if disponiveis[nomes_itens.index(b)].efeitos[0][0] == 'vida_atual':
        if personagem.status['hp'] - personagem.vida_atual >= 25:
            personagem.vida_atual += disponiveis[nomes_itens.index(b)].efeitos[0][1]
        else:
            personagem.vida_atual += personagem.status['hp'] - personagem.vida_atual
        personagem.inventario[personagem.inventario.index(disponiveis[nomes_itens.index(b)])].qtd -= 1
        if disponiveis[nomes_itens.index(b)].qtd == 0:
            personagem.inventario.remove(disponiveis[nomes_itens.index(b)])
        interface_inv(personagem)
    elif disponiveis[nomes_itens.index(b)].efeitos[0][0] == 'mana':
        if 50 - personagem.status['mana'] >= 25:
            personagem.status['mana'] += disponiveis[nomes_itens.index(b)].efeitos[0][1]
        else:
            personagem.vida_atual += 50 - personagem.status['mana']
        personagem.inventario[personagem.inventario.index(disponiveis[nomes_itens.index(b)])].qtd -= 1
        if disponiveis[nomes_itens.index(b)].qtd == 0:
            personagem.inventario.remove(disponiveis[nomes_itens.index(b)])
        interface_inv(personagem)
    elif disponiveis[nomes_itens.index(b)].efeitos[0][0] == 'analise':
        print('teste')
        display(disponiveis[nomes_itens.index(b)].descricao)
        interface_inv(personagem)

def display(fonte):
    console = Console()
    texto = Text()
    for item in fonte.split('.'):
        texto.append(item)
    console.print(texto)
    input('Pressione enter para continuar')

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
    p.inventario[0].qtd = 2
    p.inventario.append(item.lista_itens[1])
    p.inventario[1].qtd = 2
    p.inventario.append(item.lista_itens[4])
    p.inventario.append(item.lista_itens[5])
    p.inventario.append(item.lista_itens[6])
    p.inventario.append(item.lista_itens[7])
    p.inventario.append(item.lista_itens[8])
    p.inventario.append(item.lista_itens[9])
    p.inventario.append(item.lista_itens[24])
    p.vida_atual = 50
    p.status['mana'] = 0
    interface_inv(p)
    