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
        fraq = input('Digite uma fraqueza: ')
        lista_fraquezas.append(fraq)
    inimigo = Inimigos()
    inimigo.nome = name
    inimigo.dano = dmg
    inimigo.vida = health
    inimigo.fraquezas = lista_fraquezas
    lista_inimigos.append(inimigo)

def edit_ene():
    mostrar_ene()
    ene = int(input('Qual inimigo você deseja editar : ')) - 1
    lista_de_fraquezas = []
    lista_inimigos[ene].nome = input('Qual o novo nome : ')
    fraq = int(input('Numero de fraquezas: '))
    for _ in range(fraq):
        fraqs = input('Digite uma fraqueza: ')
        lista_de_fraquezas.append(fraqs)
    lista_inimigos[ene].fraquezas = lista_de_fraquezas
    lista_inimigos[ene].vida = int(input('Nova vida: '))
    lista_inimigos[ene].dano = int(input('Novo dano: '))

def excluir_ene():
    mostrar_ene()
    idx = int(input("Qual inimigo você deseja excluir: ")) - 1
    if 0 <= idx < len(lista_inimigos):
        del lista_inimigos[idx]
        print("Inimigo excluído com sucesso.")
    else:
        print("Índice inválido.")
    

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
    utills.salvar_infos('lista_inimigos', lista)

def interface():
    write()
    print('1- Adicionar um inimigo')
    print('2- Editar um inimigo')
    print('3- Excluir um inimigo')
    print('4- Listar os inimigos')
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