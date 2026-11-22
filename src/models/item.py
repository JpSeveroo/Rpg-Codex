
from dataclasses import dataclass


@dataclass(eq=False)
class Item:
    nome: str
    efeitos: list[list[str | int]]
    descricao: str
    qtd: int
    categoria: str
