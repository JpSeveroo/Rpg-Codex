
from dataclasses import dataclass, field


@dataclass(eq=False)
class Inimigo:
    nome: str
    dano: int
    vida: int
    xp: int
    fraquezas: list[str]

    vida_atual: int = field(init=False)
    status: dict[str, int] = field(init=False)
    pericias: dict[str, int] = field(init=False)

    def __post_init__(self) -> None:
        self.reiniciar_estado()

    @property
    def nick(self) -> str:
        return self.nome

    def reiniciar_estado(self) -> None:
        self.vida_atual = self.vida
        self.status = {"hp": self.vida, "mana": 100}
        self.pericias = {"mano a mano": self.dano}
