
from collections.abc import Callable

from catalogos import carregar_itens, lista_itens, salvar_itens
from models.item import Item
from utills import limpar_tela


def _solicitar_efeitos() -> list[list[str | int]]:
    quantidade = int(input("Digite o número de efeitos: "))
    efeitos: list[list[str | int]] = []

    for _ in range(quantidade):
        nome = input("Efeito: ")
        modificador = int(input("Modificador: "))
        efeitos.append([nome, modificador])

    return efeitos


def _solicitar_categoria() -> str:
    return input(
        "Qual a categoria do item: "
        "(Cabeça, Corpo, Pés, Mãos, Utilizaveis): "
    )


def adicionar_item() -> None:
    limpar_tela()

    nome = input("Nome: ")
    efeitos = _solicitar_efeitos()
    descricao = input("Descrição: ")
    categoria = _solicitar_categoria()

    novo_item = Item(
        nome=nome,
        efeitos=efeitos,
        descricao=descricao,
        qtd=0,
        categoria=categoria,
    )

    lista_itens.append(novo_item)
    salvar_itens()


def listar_itens() -> None:
    limpar_tela()

    for indice, item in enumerate(lista_itens):
        print(f"{indice}-{item.nome}")


def editar_item() -> None:
    listar_itens()

    indice = int(input("Qual item você deseja editar: "))
    item = lista_itens[indice]

    item.nome = input("Qual o novo nome: ")
    item.efeitos = _solicitar_efeitos()
    item.descricao = input("Nova descrição: ")
    item.categoria = _solicitar_categoria()

    salvar_itens()


def excluir_item() -> None:
    # Funcionalidade não implementada no código original.
    return


def menu_itens() -> None:
    opcoes: dict[int, Callable[[], None]] = {
        1: adicionar_item,
        2: editar_item,
        3: excluir_item,
        4: listar_itens,
    }

    while True:
        print("1- Adicionar um item")
        print("2- Editar um item")
        print("3- Excluir um item")
        print("4- Listar os itens")
        print("5- Finalizar")

        try:
            escolha = int(
                input("Qual das opções você deseja? ")
            )
        except ValueError:
            print("Digite um número válido")
            continue

        if escolha == 5:
            print("Saindo do gerenciador de itens")
            break

        acao = opcoes.get(escolha)

        if acao is None:
            print("Opção inválida")
            continue

        acao()


if __name__ == "__main__":
    carregar_itens()
    menu_itens()
