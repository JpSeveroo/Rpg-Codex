
from dataclasses import InitVar, dataclass, field
from typing import ClassVar

from models.item import Item


@dataclass(eq=False)
class Personagem:
    nick: str
    raca: str
    classe: str
    atributos: dict[str, int]

    xp: int = 0
    nivel: int = 1
    inventario: list[Item] = field(default_factory=list)
    fraquezas: list[str] = field(default_factory=list)
    equipamento: dict[str, object] = field(
        default_factory=lambda: {"maos": None}
    )

    andar_esfinge_completado: bool = False
    andar_cupula_completado: bool = False
    checkpoint: int = 0

    aplicar_bonus: InitVar[bool] = True

    pericias: dict[str, int] = field(init=False)
    status: dict[str, int] = field(init=False)
    mana_max: int = field(init=False)
    vida_atual: int = field(init=False)
    xp_para_proximo_nivel: int | float = field(init=False)

    tabela_xp: ClassVar[dict[int, int | float]] = {
        1: 100, 2: 120, 3: 150, 4: 170, 5: 190,
        6: 200, 7: 220, 8: 240, 9: 250, 10: 270,
        11: 300, 12: 320, 13: 340, 14: 350, 15: 400,
        16: 450, 17: 500, 18: 520, 19: 550, 20: 600,
        21: 650, 22: 700, 23: 800, 24: 900, 25: 950,
        26: 1100, 27: 1200, 28: 1300, 29: 1450,
        30: float("inf"),
    }

    def __post_init__(self, aplicar_bonus: bool) -> None:
        self.atributos = self.atributos.copy()
        self.inventario = self.inventario.copy()
        self.fraquezas = self.fraquezas.copy()
        self.equipamento = self.equipamento.copy()

        self.pericias = {
            "acrobacia": 0,
            "blefar": 0,
            "mira": 0,
            "diplomacia": 0,
            "furtividade": 0,
            "percepcao": 0,
            "maos rapidas": 0,
            "mano a mano": 0,
            "resistencia": 0,
        }

        self.status = {"hp": 100, "mana": 100}
        self.mana_max = self.status["mana"]
        self.vida_atual = self.status["hp"]

        self.xp_para_proximo_nivel = self.tabela_xp.get(
            self.nivel, 100
        )

        if aplicar_bonus:
            self._aplicar_bonus_iniciais()

        self.status["hp"] = (
            100 + self.atributos["constituicao"] * 5
        )
        self.vida_atual = self.status["hp"]

        self.calcular_pericias()

    def _aplicar_bonus_iniciais(self) -> None:
        if self.raca == "humano":
            for atributo in self.atributos:
                self.atributos[atributo] += 1

        elif self.raca == "elfo":
            self.atributos["destreza"] += 3
            self.atributos["inteligencia"] += 2
            self.atributos["constituicao"] -= 2

        elif self.raca == "draconiano":
            self.atributos["força"] += 5
            self.atributos["carisma"] -= 3

        if self.classe == "guerreiro":
            self.atributos["força"] += 8
            self.atributos["destreza"] += 2
            self.pericias["diplomacia"] -= 3

        elif self.classe == "ladino":
            self.atributos["destreza"] += 5
            self.atributos["inteligencia"] += 5
            self.pericias["resistencia"] -= 3

        elif self.classe == "mago":
            self.atributos["inteligencia"] += 7
            self.atributos["carisma"] += 3
            self.pericias["mano a mano"] -= 3

        elif self.classe == "clérigo":
            self.atributos["carisma"] += 5
            self.atributos["destreza"] += 5
            self.pericias["furtividade"] -= 3

    def calcular_pericias(self) -> None:
        self.pericias = {
            "acrobacia": self.atributos["destreza"],
            "blefar": self.atributos["carisma"],
            "mira": self.atributos["destreza"],
            "diplomacia": self.atributos["carisma"],
            "furtividade": self.atributos["inteligencia"],
            "percepcao": self.atributos["inteligencia"],
            "maos rapidas": self.atributos["destreza"],
            "mano a mano": self.atributos["força"],
            "resistencia": self.atributos["força"],
        }

    def pode_evoluir(self) -> bool:
        return (
            self.nivel < max(self.tabela_xp)
            and self.xp >= self.tabela_xp[self.nivel]
        )

    def evoluir_nivel(
        self,
        distribuicao: dict[str, int],
    ) -> bool:
        if not self.pode_evoluir():
            return False

        if (
            any(
                atributo not in self.atributos
                for atributo in distribuicao
            )
            or any(
                type(pontos) is not int or pontos < 0
                for pontos in distribuicao.values()
            )
            or sum(distribuicao.values()) != 5
        ):
            raise ValueError(
                "Distribua exatamente 5 pontos entre os atributos."
            )

        xp_necessario = self.tabela_xp[self.nivel]

        self.xp -= int(xp_necessario)
        self.nivel += 1

        self.xp_para_proximo_nivel = self.tabela_xp.get(
            self.nivel, float("inf")
        )

        for atributo, pontos in distribuicao.items():
            self.atributos[atributo] += pontos

        self.calcular_pericias()

        if self.nivel >= max(self.tabela_xp):
            self.xp_para_proximo_nivel = float("inf")
        else:
            self.xp_para_proximo_nivel = self.tabela_xp.get(
                self.nivel, float("inf")
            )

        return True
