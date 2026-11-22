
from dataclasses import fields, is_dataclass
from typing import Any

from models.item import Item
from models.personagem import Personagem
from models.usuario import Usuario
from utills import DATA_DIR, load_infos, salvar_infos


def _carregar_registros(nome: str) -> list[dict[str, Any]]:
    dados = load_infos(nome)

    if dados is None:
        caminho = DATA_DIR / f"{nome}.json"

        if caminho.is_file():
            raise ValueError(
                f"Não foi possível carregar o arquivo {caminho}."
            )

        return []

    if not isinstance(dados, list):
        raise ValueError(f"O arquivo {nome}.json deve conter uma lista.")

    if not all(isinstance(registro, dict) for registro in dados):
        raise ValueError(
            f"O arquivo {nome}.json contém registros inválidos."
        )

    return dados


def _serializar(valor: Any) -> Any:
    if is_dataclass(valor) and not isinstance(valor, type):
        return {
            campo.name: _serializar(getattr(valor, campo.name))
            for campo in fields(valor)
        }

    if isinstance(valor, dict):
        return {
            chave: _serializar(conteudo)
            for chave, conteudo in valor.items()
        }

    if isinstance(valor, (list, tuple)):
        return [_serializar(item) for item in valor]

    if hasattr(valor, "itens"):
        return {"itens": _serializar(valor.itens)}

    if valor is None or isinstance(
        valor, (str, int, float, bool)
    ):
        return valor

    raise TypeError(
        f"Tipo não suportado na serialização: {type(valor).__name__}"
    )


def carregar_usuarios() -> list[Usuario]:
    usuarios = []

    for dados in _carregar_registros("usuarios"):
        usuario = Usuario(
            username=dados.get("_username", dados.get("username", "")),
            senha_hash=dados.get(
                "_password",
                dados.get("senha_hash", ""),
            ),
            personagens=dados.get("personagens", []),
        )

        usuarios.append(usuario)

    return usuarios


def salvar_usuarios(usuarios: list[Usuario]) -> None:
    dados = [
        {
            "_username": usuario.username,
            "_password": usuario.senha_hash,
            "personagens": usuario.personagens,
        }
        for usuario in usuarios
    ]

    salvar_infos("usuarios", dados)


def _carregar_item(dados: dict[str, Any]) -> Item:
    return Item(
        nome=dados["nome"],
        efeitos=dados["efeitos"],
        descricao=dados["descricao"],
        qtd=dados["qtd"],
        categoria=dados["categoria"],
    )


def carregar_personagens() -> list[Personagem]:
    personagens = []

    for dados in _carregar_registros("personagem"):
        inventario = [
            _carregar_item(item)
            for item in dados.get("inventario", [])
        ]

        personagem = Personagem(
            nick=dados["nick"],
            raca=dados["raca"],
            classe=dados["classe"],
            atributos=dados["atributos"],
            xp=dados.get("xp", 0),
            nivel=dados.get("nivel", 1),
            inventario=inventario,
            fraquezas=dados.get("fraquezas", []),
            equipamento=dados.get(
                "equipamento",
                {"maos": None},
            ),
            andar_esfinge_completado=dados.get(
                "andar_esfinge_completado",
                False,
            ),
            andar_cupula_completado=dados.get(
                "andar_cupula_completado",
                False,
            ),
            checkpoint=dados.get("checkpoint", 0),
            aplicar_bonus=False,
        )

        campos_salvos = (
            "pericias",
            "status",
            "mana_max",
            "vida_atual",
            "xp_para_proximo_nivel",
        )

        for campo in campos_salvos:
            if campo in dados:
                setattr(personagem, campo, dados[campo])

        if (
            "modificadores_pericias" in dados
            and hasattr(personagem, "modificadores_pericias")
        ):
            personagem.modificadores_pericias = dados[
                "modificadores_pericias"
            ]

        personagens.append(personagem)

    return personagens


def salvar_personagens(personagens: list[Personagem]) -> None:
    dados = [_serializar(personagem) for personagem in personagens]
    salvar_infos("personagem", dados)
