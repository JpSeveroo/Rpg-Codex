
from dataclasses import InitVar, dataclass, field
from typing import ClassVar

from models.item import Item


_ATRIBUTOS = (
    "força",
    "destreza",
    "constituicao",
    "carisma",
    "inteligencia",
)

_PERICIAS = {
    "acrobacia": "destreza",
    "blefar": "carisma",
    "mira": "destreza",
    "diplomacia": "carisma",
    "furtividade": "inteligencia",
    "percepcao": "inteligencia",
    "maos rapidas": "destreza",
    "mano a mano": "força",
    "resistencia": "força",
}

_BONUS_RACA = {
    "humano": {atributo: 1 for atributo in _ATRIBUTOS},
    "elfo": {
        "destreza": 3,
        "inteligencia": 2,
        "constituicao": -2,
    },
    "draconiano": {
        "força": 5,
        "carisma": -3,
    },
}

_BONUS_CLASSE = {
    "guerreiro": {"força": 8, "destreza": 2},
    "ladino": {"destreza": 5, "inteligencia": 5},
    "mago": {"inteligencia": 7, "carisma": 3},
    "clérigo": {"carisma": 5, "destreza": 5},
}

_PENALIDADES_CLASSE = {
    "guerreiro": {"diplomacia": -3},
    "ladino": {"resistencia": -3},
    "mago": {"mano a mano": -3},
    "clérigo": {"furtividade": -3},
}


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

    modificadores_pericias: dict[str, int] = field(
        default_factory=dict
    )
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
        self.nick = self.nick.strip()
        self.raca = self.raca.strip().lower()
        self.classe = self.classe.strip().lower()

        if not self.nick:
            raise ValueError("O nome do personagem não pode estar vazio.")

        if self.raca not in _BONUS_RACA:
            raise ValueError(f"Raça inválida: {self.raca}")

        if self.classe not in _BONUS_CLASSE:
            raise ValueError(f"Classe inválida: {self.classe}")

        if set(self.atributos) != set(_ATRIBUTOS):
            raise ValueError("Os atributos informados são inválidos.")

        if any(
            type(valor) is not int
            for valor in self.atributos.values()
        ):
            raise ValueError("Os atributos devem conter valores inteiros.")

        if aplicar_bonus and (
            any(valor < 0 for valor in self.atributos.values())
            or sum(self.atributos.values()) != 30
        ):
            raise ValueError(
                "Distribua exatamente 30 pontos não negativos."
            )

        if type(self.nivel) is not int or self.nivel not in self.tabela_xp:
            raise ValueError("Nível inválido.")

        if type(self.xp) is not int or self.xp < 0:
            raise ValueError("A experiência deve ser não negativa.")

        self.atributos = self.atributos.copy()
        self.inventario = self.inventario.copy()
        self.fraquezas = self.fraquezas.copy()
        self.equipamento = self.equipamento.copy()
        self.modificadores_pericias = (
            self.modificadores_pericias.copy()
        )

        if aplicar_bonus:
            self._aplicar_bonus_iniciais()

        self.calcular_pericias()

        self.mana_max = 100
        self.status = {
            "hp": 100 + self.atributos["constituicao"] * 5,
            "mana": self.mana_max,
        }
        self.vida_atual = self.status["hp"]
        self.xp_para_proximo_nivel = self.tabela_xp[self.nivel]

    def _aplicar_bonus_iniciais(self) -> None:
        bonus = (
            _BONUS_RACA[self.raca],
            _BONUS_CLASSE[self.classe],
        )

        for modificadores in bonus:
            for atributo, pontos in modificadores.items():
                self.atributos[atributo] += pontos

    def calcular_pericias(self) -> None:
        penalidades = _PENALIDADES_CLASSE[self.classe]

        self.pericias = {
            pericia: (
                self.atributos[atributo]
                + penalidades.get(pericia, 0)
                + self.modificadores_pericias.get(pericia, 0)
            )
            for pericia, atributo in _PERICIAS.items()
        }

    def alterar_modificador_pericia(
        self,
        pericia: str,
        pontos: int,
    ) -> None:
        if pericia not in _PERICIAS:
            raise ValueError(f"Perícia inválida: {pericia}")

        if type(pontos) is not int:
            raise ValueError("O modificador deve ser inteiro.")

        self.modificadores_pericias[pericia] = (
            self.modificadores_pericias.get(pericia, 0) + pontos
        )

        self.calcular_pericias()

    def adicionar_experiencia(self, quantidade: int) -> None:
        if type(quantidade) is not int or quantidade < 0:
            raise ValueError(
                "A experiência recebida deve ser um inteiro não negativo."
            )

        self.xp += quantidade

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
                "Distribua exatamente 5 pontos entre os atributos válidos."
            )

        vida_maxima_anterior = self.status["hp"]

        self.xp -= int(self.tabela_xp[self.nivel])
        self.nivel += 1

        for atributo, pontos in distribuicao.items():
            self.atributos[atributo] += pontos

        self.xp_para_proximo_nivel = self.tabela_xp[self.nivel]
        self.calcular_pericias()

        nova_vida_maxima = (
            100 + self.atributos["constituicao"] * 5
        )
        self.status["hp"] = nova_vida_maxima
        self.vida_atual = min(
            self.vida_atual + nova_vida_maxima - vida_maxima_anterior,
            nova_vida_maxima,
        )

        return True
