
import os

from InquirerPy import inquirer
from rich.console import Console
from rich.text import Text

from models.item import Item
from models.personagem import Personagem


class Equipamento:
    def __init__(self) -> None:
        self.itens = {
            "Cabeça": {"equipado": False, "item": ""},
            "Corpo": {"equipado": False, "item": ""},
            "Pés": {"equipado": False, "item": ""},
            "Mãos": {"equipado": False, "item": ""},
        }


equipamento = Equipamento()
escolhido = ""


def _nome_equipamento(personagem: Personagem, parte: str) -> str:
    try:
        return personagem.equipamento.itens[parte]["item"].nome
    except AttributeError:
        return ""


def _linha_equipamento(
    personagem: Personagem,
    parte: str,
    pericia: str,
    rotulo: str,
) -> None:
    nome = _nome_equipamento(personagem, parte)

    esquerda = f"{parte}: {nome}".ljust(33)
    direita = f"{rotulo}: {personagem.pericias[pericia]}".center(33)

    print(f"|{esquerda}|{' ' * 10}|{direita}|")


def _linha_pericia(
    personagem: Personagem,
    pericia: str,
    rotulo: str,
) -> None:
    direita = f"{rotulo}: {personagem.pericias[pericia]}".center(33)
    print(f"|{'-' * 33}|{' ' * 10}|{direita}|")


def equips(personagem: Personagem) -> None:
    print("-" * 35 + " " * 10 + "-" * 35)

    _linha_equipamento(personagem, "Cabeça", "acrobacia", "Acrobacia")
    _linha_pericia(personagem, "blefar", "Blefar")

    _linha_equipamento(personagem, "Corpo", "mira", "Mira")
    _linha_pericia(personagem, "diplomacia", "Diplomacia")

    _linha_equipamento(personagem, "Pés", "furtividade", "Furtividade")
    _linha_pericia(personagem, "percepcao", "Percepção")

    _linha_equipamento(
        personagem,
        "Mãos",
        "maos rapidas",
        "Mãos Rápidas",
    )
    _linha_pericia(personagem, "mano a mano", "Mano a Mano")

    vida = f"Vida: {personagem.vida_atual}".center(33)
    resistencia = (
        f"Resistência: {personagem.pericias['resistencia']}"
    ).center(33)

    print(f"|{vida}|{' ' * 10}|{resistencia}|")

    mana = f"Mana: {personagem.status['mana']}".center(33)
    print(f"|{mana}|{' ' * 10}{'-' * 35}")

    print("-" * 35)


def interface_inv(personagem: Personagem) -> None:
    global escolhido

    escolhido = ""

    os.system("cls" if os.name == "nt" else "clear")

    equips(personagem)

    print(personagem.inventario[0].nome)

    personagem.equipamento = equipamento

    disponiveis: list[Item] = []

    escolha = inquirer.select(
        message="Qual equipamento você deseja alterar ?",
        choices=[
            "Cabeça",
            "Corpo",
            "Pés",
            "Mãos",
            "Utilizaveis",
            "Sair",
        ],
    ).execute()

    for item in personagem.inventario:
        if item.categoria == escolha:
            disponiveis.append(item)

    escolhido = escolha

    opcoes = {
        "Cabeça": equip_itens,
        "Corpo": equip_itens,
        "Pés": equip_itens,
        "Mãos": equip_itens,
        "Utilizaveis": utilizaveis,
        "Sair": sair,
    }

    acao = opcoes.get(escolha)

    if acao:
        acao(personagem, disponiveis)


def equip_itens(
    personagem: Personagem,
    disponiveis: list[Item],
) -> None:
    global escolhido

    if not equipamento.itens[escolhido]["equipado"]:
        if len(disponiveis) == 0:
            print(
                "Não há nenhum equipamento "
                "disponivel para essa parte"
            )
            input("Pressione enter para voltar...")
            interface_inv(personagem)
            return

        nomes_itens = [item.nome for item in disponiveis]
        nomes_itens.append("Sair")

        escolha = inquirer.select(
            message=(
                "Qual o item que você deseja "
                f"equipar na(o) {escolhido}: "
            ),
            choices=nomes_itens,
        ).execute()

        if escolha == "Sair":
            interface_inv(personagem)
            return

        item = disponiveis[nomes_itens.index(escolha)]

        equipamento.itens[escolhido]["item"] = item

        equipando(personagem, item, escolhido)
        interface_inv(personagem)

    else:
        print(
            f"Não é possivel equipar um item na(o) {escolhido}"
        )

        confirmar = inquirer.confirm(
            message="Você deseja desequipar ?"
        ).execute()

        if confirmar:
            item = equipamento.itens[escolhido]["item"]
            desequipando(personagem, item, escolhido)

        interface_inv(personagem)


def sair(
    personagem: Personagem,
    disponiveis: list[Item],
) -> tuple[list[Item], Personagem]:
    return disponiveis, personagem


def utilizaveis(
    personagem: Personagem,
    disponiveis: list[Item],
) -> None:
    nomes_itens = [item.nome for item in disponiveis]
    nomes_itens.append("Sair")

    if not nomes_itens:
        print("Não há nenhum utilizavel disponivel")
        input("Pressione enter para voltar...")
        interface_inv(personagem)
        return

    escolha = inquirer.select(
        message="Qual o item que você deseja utilizar: ",
        choices=nomes_itens,
    ).execute()

    if escolha == "Sair":
        interface_inv(personagem)
        return

    item = disponiveis[nomes_itens.index(escolha)]

    print(item.nome)

    if item.efeitos[0][0] == "vida_atual":
        if personagem.status["hp"] - personagem.vida_atual >= 50:
            personagem.vida_atual += item.efeitos[0][1]
        else:
            personagem.vida_atual += (
                personagem.status["hp"] - personagem.vida_atual
            )

        personagem.inventario[
            personagem.inventario.index(item)
        ].qtd -= 1

        if item.qtd == 0:
            personagem.inventario.remove(item)

        interface_inv(personagem)

    elif item.efeitos[0][0] == "mana":
        if 100 - personagem.status["mana"] >= 25:
            personagem.status["mana"] += item.efeitos[0][1]
        else:
            personagem.status["mana"] += (
                50 - personagem.status["mana"]
            )

        personagem.inventario[
            personagem.inventario.index(item)
        ].qtd -= 1

        if item.qtd == 0:
            personagem.inventario.remove(item)

        interface_inv(personagem)

    elif item.efeitos[0][0] == "analise":
        print("teste")
        display(item.descricao)
        interface_inv(personagem)


def display(fonte: str) -> None:
    console = Console()
    texto = Text()

    for trecho in fonte.split("."):
        texto.append(trecho)

    console.print(texto)
    input("Pressione enter para continuar...")


def equipando(
    personagem: Personagem,
    item: Item,
    parte: str,
) -> None:
    for efeito in item.efeitos:
        personagem.pericias[efeito[0]] += efeito[1]

    equipamento.itens[parte]["equipado"] = True


def desequipando(
    personagem: Personagem,
    item: Item,
    parte: str,
) -> None:
    for efeito in item.efeitos:
        personagem.pericias[efeito[0]] -= efeito[1]

        equipamento.itens[parte]["equipado"] = False
        equipamento.itens[parte]["item"] = ""


if __name__ == "__main__":
    from catalogos import carregar_catalogos, lista_itens

    carregar_catalogos()

    personagem = Personagem(
        nick="Teste",
        raca="humano",
        classe="guerreiro",
        atributos={
            "força": 6,
            "destreza": 6,
            "constituicao": 6,
            "carisma": 6,
            "inteligencia": 6,
        },
    )

    personagem.inventario.append(lista_itens[0])
    personagem.inventario[0].qtd = 2

    personagem.inventario.append(lista_itens[1])
    personagem.inventario[1].qtd = 2

    for indice in (4, 5, 6, 7, 8, 9, 24, 12):
        personagem.inventario.append(lista_itens[indice])

    personagem.vida_atual = 50
    personagem.status["mana"] = 0

    interface_inv(personagem)
