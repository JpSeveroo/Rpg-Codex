import utills
from os import system

lista_itens = []

class item :
    def __init__(self):
        self.nome = ''
        self.efeitos = []
        self.descricao = ''

def add_item():
    system('clear')
    a = input('Nome: ')
    b = int(input('Digite o número de efeitos '))
    lista_de_efeitos = []
    for _ in range(b):
        lista = []
        b = input('Efeito: ')
        lista.append(b)
        c = int(input('Modificador: '))
        lista.append(c)
        lista_de_efeitos.append(lista)
    c = input('Descrição: ')
    objeto = item()
    objeto.nome = a
    objeto.efeitos = lista_de_efeitos
    objeto.descricao = c
    lista_itens.append(objeto)

def mostrar():
    for i in lista_itens:
        print(i.nome)
        print(i.efeitos)
        print(i.descricao)
        print()

def load_itens():
    try:
        lista = utills.load_infos('lista_itens')
        for i in lista:
            a = item()
            a.nome = i['nome']
            a.efeitos = i['efeitos']
            a.descricao = i['descricao']
            lista_itens.append(a)
    except:
        pass

def write():
    lista = []
    for i in lista_itens:
        a = i.__dict__
        lista.append(a)
    utills.salvar_infos('lista_itens', lista)

if __name__ == '__main__':
    load_itens()
    a = input()
    if a == 's':
        system('clear')
        mostrar()
    elif a == 'n':
        add_item()
        write()