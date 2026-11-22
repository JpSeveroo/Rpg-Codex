
from dataclasses import asdict
from typing import Any

from models.inimigo import Inimigo
from models.item import Item
from utills import load_infos, salvar_infos

lista_itens: list[Item] = []
lista_inimigos: list[Inimigo] = []


def _ler_registros(nome: str) -> list[dict[str, Any]]:
    dados = load_infos(nome)

    if not isinstance(dados, list):
        raise ValueError(
            f"O catálogo '{nome}' não contém uma lista válida."
        )

    if not all(isinstance(registro, dict) for registro in dados):
        raise ValueError(
            f"O catálogo '{nome}' contém registros inválidos."
        )

    return dados


def carregar_itens() -> None:
    registros = _ler_registros("lista_itens")

    itens = [
        Item(
            nome=registro.get("nome", ""),
            efeitos=registro.get("efeitos", []),
            descricao=registro.get("descricao", ""),
            qtd=registro.get("qtd", 0),
            categoria=registro.get("categoria", ""),
        )
        for registro in registros
    ]

    lista_itens[:] = itens


def salvar_itens() -> None:
    dados = [asdict(item) for item in lista_itens]
    salvar_infos("lista_itens", dados)


def carregar_inimigos() -> None:
    registros = _ler_registros("lista_inimigos")

    inimigos = [
        Inimigo(
            nome=registro.get("nome", ""),
            dano=registro.get("dano", 0),
            vida=registro.get("vida", 0),
            xp=registro.get("xp", 0),
            fraquezas=registro.get("fraquezas", []),
        )
        for registro in registros
    ]

    lista_inimigos[:] = inimigos


def salvar_inimigos() -> None:
    dados = [
        {
            "nome": inimigo.nome,
            "dano": inimigo.dano,
            "vida": inimigo.vida,
            "xp": inimigo.xp,
            "fraquezas": inimigo.fraquezas,
            "status": inimigo.status,
            "vida_atual": inimigo.vida_atual,
            "pericias": inimigo.pericias,
            "nick": inimigo.nick,
        }
        for inimigo in lista_inimigos
    ]

    salvar_infos("lista_inimigos", dados)


def carregar_catalogos() -> None:
    carregar_itens()
    carregar_inimigos()
