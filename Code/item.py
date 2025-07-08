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
    write()

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
            novo_item = item()
            novo_item.nome = i.get('nome', '')
            novo_item.efeitos = i.get('efeitos', [])
            novo_item.descricao = i.get('descricao', '')
            novo_item.qtd = i.get('qtd', 0)
            novo_item.categoria = i.get('categoria', '')
            lista_itens.append(novo_item)
    except Exception as e:
        print(f"Erro ao carregar itens: {e}")

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
    write()

def excluir_item():
    return

def write():
    lista = []
    for i in lista_itens:
        a = i.__dict__
        lista.append(a)
    utills.salvar_infos('lista_itens', lista)

def interface():
    while True:
        print('1- Adicionar um item')
        print('2- Editar um item')
        print('3- Excluir um item')
        print('4- Listar os itens')
        print('5- Finalizar')
        try:
            a = int(input('Qual das opções você deseja ? '))
        except ValueError:
            print('Digite um número válido')
            continue
        if a == 5:
            print('Saindo do gerenciador de itens')
            break
        opcoes = {
            1: add_item,
            2: edit_item,
            3: excluir_item,
            4: mostrar,
        }
        a = opcoes.get(a)
        if a:
            a()
        else:
            print('Opção invalida')

if __name__ == '__main__':
    load_itens()
    interface()