import utills

lista_itens = []

class item :
    def __init__(self):
        self.nome = ''
        self.efeitos = ''

def add_item():
    a = input('Nome: ')
    b = input('Efeito: ')
    objeto = item()
    objeto.nome = a
    objeto.efeitos = b
    lista_itens.append(objeto)

def load():
    try:
        lista = utills.load_infos('lista_itens')
        for i in lista:
            a = item()
            a.nome = i['nome']
            a.efeitos = i['efeitos']
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
    load()
    add_item()
    write()