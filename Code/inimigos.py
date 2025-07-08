import json
import os
import utills

lista_inimigos = []

class Inimigos:
    def __init__(self):
        self.nome = ''
        self.dano = 0
        self.vida = 0
        self.fraquezas = []

def add_ene():
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input('Nome: ')
    dmg = int(input('Dano: '))
    health = int(input('Vida: '))
    weak = int(input('Numero de fraquezas: '))
    lista_fraquezas = []
    for _ in range(weak):
        fraq = input('digite uma fraqueza: ')
        lista_fraquezas.append(fraq)
    inimigo = Inimigos()
    inimigo.nome = name
    inimigo.dano = dmg
    inimigo.vida = health
    inimigo.fraquezas = lista_fraquezas
    lista_inimigos.append(inimigo)

def edit_ene():
    mostrar_ene()
    ene = int(input('Qual item você deseja editar : ')) - 1
    lista_de_fraquezas = []
    lista_inimigos[ene].nome = input('Qual o novo nome : ')
    for _ in range(b):
        lista = []
        b = input('Efeito: ')
        lista.append(b)
        c = int(input('Modificador: '))
        lista.append(c)
        lista_de_fraquezas.append(lista)
    lista_inimigos[ene].efeitos = lista_de_fraquezas
    lista_inimigos[ene].descricao = input('Nova descrição: ')
    lista_inimigos[ene].categoria = input('Qual a categoria do item : (cabeca, corpo, pes, maos)')

def excluir_ene():
    ...

def mostrar_ene():
    os.system('cls' if os.name == 'nt' else 'clear')

    if not lista_inimigos:
        print('Não tem inimigo ainda')
        return
    print('Lista de Inimigos')
    for i,inimigo in enumerate(lista_inimigos, 1):
        print(f'Inimigo {i}')
        print(f'Nome: {inimigo.nome}; Dano: {inimigo.dano}; Vida: {inimigo.vida}; Fraquezas: {', '.join(inimigo.fraquezas)}')
        print()

def write():
    lista = []
    for i in lista_inimigos:
        a = i.__dict__
        lista.append(a)
    utills.salvar_infos('lista_itens', lista)

def interface():
    write()
    print('1- Adicionar um item')
    print('2- Editar um item')
    print('3- Excluir um item')
    print('4- Listar os itens')
    print('5- Finalizar')
    a = int(input('Qual das opções você deseja ? '))
    opcoes = {
        1: add_ene,
        2: edit_ene,
        3: excluir_ene,
        4: mostrar_ene,
    }
    a = opcoes.get(a)
    if a:
        a()