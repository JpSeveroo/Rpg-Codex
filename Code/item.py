import utills
from os import system

lista_itens = []

class item :
    def __init__(self):
        self.nome = ''
        self.efeitos = []
        self.descricao = ''
        self.qtd = 0
        self.categoria = ''

def add_item():
    utills.limpar_tela()
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
    objeto.categoria = input('Qual a categoria do item : (Cabeça, Corpo, Pés, Mãos, Utilizaveis)')
    lista_itens.append(objeto)
    interface()

def mostrar():
    utills.limpar_tela()
    for i in range(len(lista_itens)):
        print(f'{i}-{lista_itens[i].nome}')
    input()
    interface()

def load_itens():
    try:
        lista = utills.load_infos('lista_itens')
        for i in lista:
            a = item()
            a.nome = i['nome']
            a.efeitos = i['efeitos']
            a.descricao = i['descricao']
            a.qtd = i['qtd']
            a.categoria = i['categoria']
            lista_itens.append(a)
    except:
        pass

def edit_item():
    mostrar()
    a = int(input('Qual item você deseja editar : ')) - 1
    lista_de_efeitos = []
    lista_itens[a].nome = input('Qual o novo nome : ')
    b = int(input('Numero de efeitos: '))
    for _ in range(b):
        lista = []
        b = input('Efeito: ')
        lista.append(b)
        c = int(input('Modificador: '))
        lista.append(c)
        lista_de_efeitos.append(lista)
    lista_itens[a].efeitos = lista_de_efeitos
    lista_itens[a].descricao = input('Nova descrição: ')
    lista_itens[a].categoria = input('Qual a categoria do item : (cabeca, corpo, pes, maos)')

def excluir_item():
    return

def write():
    lista = []
    for i in lista_itens:
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
        1: add_item,
        2: edit_item,
        3: excluir_item,
        4: mostrar,
    }
    a = opcoes.get(a)
    if a:
        a()

load_itens()

if __name__ == '__main__':
    print(lista_itens)
    interface()