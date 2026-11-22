
from dataclasses import dataclass


@dataclass
class Item:
    nome: str
    efeitos: list[list[str | int]]
    descricao: str
    qtd: int
    categoria: str
