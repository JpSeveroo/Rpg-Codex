
from collections.abc import Callable

from catalogos import (
    carregar_inimigos,
    lista_inimigos,
    salvar_inimigos,
)
from models.inimigo import Inimigo
from utills import limpar_tela


def _solicitar_fraquezas() -> list[str]:
    quantidade = int(input("Número de fraquezas: "))

    return [
        input(f"Digite a fraqueza {indice + 1}: ")
        for indice in range(quantidade)
    ]


def adicionar_inimigo() -> None:
    limpar_tela()

    nome = input("Nome: ")
    dano = int(input("Dano: "))
    vida = int(input("Vida: "))
    fraquezas = _solicitar_fraquezas()

    inimigo = Inimigo(
        nome=nome,
        dano=dano,
        vida=vida,
        xp=0,
        fraquezas=fraquezas,
    )

    lista_inimigos.append(inimigo)
    salvar_inimigos()


def listar_inimigos() -> None:
    limpar_tela()

    if not lista_inimigos:
        print("Não tem inimigo ainda")
        return

    print("Lista de Inimigos")

    for indice, inimigo in enumerate(lista_inimigos, start=1):
        print(f"Inimigo {indice}")
        print(
            f"Nome: {inimigo.nome}; "
            f"Dano: {inimigo.dano}; "
            f"Vida: {inimigo.vida}; "
            f"Fraquezas: {', '.join(inimigo.fraquezas)}"
        )
        print()


def editar_inimigo() -> None:
    listar_inimigos()

    try:
        indice = int(
            input("Qual inimigo você deseja editar: ")
        ) - 1
    except ValueError:
        print("Digite um número válido.")
        return

    if not 0 <= indice < len(lista_inimigos):
        print("Índice inválido.")
        return

    inimigo = lista_inimigos[indice]

    inimigo.nome = input("Qual o novo nome: ")
    inimigo.fraquezas = _solicitar_fraquezas()
    inimigo.vida = int(input("Nova vida: "))
    inimigo.dano = int(input("Novo dano: "))

    salvar_inimigos()


def excluir_inimigo() -> None:
    listar_inimigos()

    try:
        indice = int(
            input("Qual inimigo você deseja excluir: ")
        ) - 1
    except ValueError:
        print("Digite um número válido.")
        return

    if not 0 <= indice < len(lista_inimigos):
        print("Índice inválido.")
        return

    del lista_inimigos[indice]
    salvar_inimigos()

    print("Inimigo excluído com sucesso.")


def menu_inimigos() -> None:
    opcoes: dict[int, Callable[[], None]] = {
        1: adicionar_inimigo,
        2: editar_inimigo,
        3: excluir_inimigo,
        4: listar_inimigos,
    }

    while True:
        print("\n1- Adicionar um inimigo")
        print("2- Editar um inimigo")
        print("3- Excluir um inimigo")
        print("4- Listar os inimigos")
        print("5- Finalizar")

        try:
            escolha = int(
                input("Qual das opções você deseja? ")
            )
        except ValueError:
            print("Digite um número válido.")
            continue

        if escolha == 5:
            print("Saindo do gerenciador de inimigos")
            break

        acao = opcoes.get(escolha)

        if acao is None:
            print("Opção inválida.")
            continue

        acao()


if __name__ == "__main__":
    carregar_inimigos()
    menu_inimigos()
