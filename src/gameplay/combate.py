
from random import randint
from time import sleep

from InquirerPy import inquirer

from catalogos import lista_inimigos, lista_itens
from gameplay import inventario
from models.inimigo import Inimigo
from models.personagem import Personagem
from ui.ficha import processar_evolucao
from utills import digitar, limpar_tela, tempo_digitar

# === UTILITÁRIOS ===

tempo_digitar(0.02)


def get_nome(personagem: Personagem | Inimigo) -> str:
    if isinstance(personagem, Personagem):
        return personagem.nick
    return personagem.nome


def rolar_dado() -> tuple[int, bool]:
    dado = randint(1, 6)
    condicao = randint(1, 6)
    critico = condicao == dado
    return dado, critico


# === DANO E AÇÕES ===

def calc_dano(
    personagem: Personagem | Inimigo,
    pericia_principal: str,
    bonus_extra: bool = False,
    pericia_secundaria: str | None = None,
) -> int:
    multiplicador = equip(personagem, pericia_principal)
    base = int(
        personagem.pericias.get(pericia_principal, 0)
        * 2
        * multiplicador
    )
    dado, critico = rolar_dado()
    dano_base = base - ((base // (dado + 1)) + 2)
    dano = dano_base if dano_base > 0 else 1

    if bonus_extra:
        dano += personagem.pericias.get(pericia_secundaria, 0)

    if critico:
        dano += dano_base // 2
        digitar(
            f"🎲 {personagem.nick} rola 1d6: {dado}; dano = {dano} "
            "🎉 QUE SORTE, DEU CRÍTICO!"
        )
    else:
        digitar(f"🎲 {personagem.nick} rola 1d6: {dado}; dano = {dano}")

    return dano


def executar_ataque(
    atacante: Personagem | Inimigo,
    defensor: Personagem | Inimigo,
    pericia_principal: str,
    custo_mana: int,
    bonus_extra: bool = False,
    pericia_secundaria: str | None = None,
) -> bool:
    if atacante.status["mana"] < custo_mana:
        digitar("⚠️ Mana insuficiente! Tente outra ação.")
        sleep(1.5)
        return False

    atacante.status["mana"] -= custo_mana

    if pericia_secundaria:
        digitar(
            f"⚔️ {atacante.nick} usou a perícia "
            f"{pericia_secundaria} no ataque especial!"
        )

        if bonus_extra:
            digitar(
                f"🎯 A perícia escolhida ({pericia_secundaria}) "
                f"é eficaz contra {defensor.nome}!"
            )
        else:
            digitar(
                f"💨 A perícia escolhida ({pericia_secundaria}) "
                "não teve efeito"
            )

    dano = calc_dano(
        atacante,
        pericia_principal,
        bonus_extra,
        pericia_secundaria,
    )

    if isinstance(atacante, Inimigo):
        dano -= defensor.pericias.get("resistencia", 0) // 4

        if dano < 1:
            dano = 1

        digitar(f"🛡️ Dano reduzido pela sua resistencia para {dano}!")

    defensor.vida_atual -= dano
    if defensor.vida_atual < 0:
        defensor.vida_atual = 0

    tipo_de_ataque = (
        "ataque especial" if pericia_secundaria else "ataque"
    )

    digitar(
        f"\n⚔️  {get_nome(atacante)} fez um {tipo_de_ataque} "
        f"em {get_nome(defensor)}! causando {dano} de dano!"
    )
    digitar(
        f"❤️  {get_nome(defensor)} agora tem "
        f"{defensor.vida_atual} HP."
    )
    print()
    sleep(2)
    return True


def ataque(
    atacante: Personagem | Inimigo,
    defensor: Personagem | Inimigo,
    pericia_principal: str,
) -> bool:
    custo_mana = 5
    return executar_ataque(
        atacante, defensor, pericia_principal, custo_mana
    )


def ataque_especial(
    atacante: Personagem | Inimigo,
    defensor: Personagem | Inimigo,
    pericia_principal: str,
    pericia_secundaria: str,
) -> bool:
    custo_especial = 10

    acertou_fraqueza = pericia_secundaria in getattr(
        defensor, "fraquezas", []
    )

    return executar_ataque(
        atacante,
        defensor,
        pericia_principal,
        custo_especial,
        bonus_extra=acertou_fraqueza,
        pericia_secundaria=pericia_secundaria,
    )


def esquivar(personagem: Personagem, mana_max: int) -> bool:
    acrobacia = personagem.pericias.get("acrobacia", 0)
    dado = randint(1, 20)
    total = dado + acrobacia

    digitar(
        f"🤸 {personagem.nick} tenta se esquivar! "
        f"Rolagem: {dado} + Acrobacia: ({acrobacia}) = {total}"
    )
    sleep(2)

    if total >= 15:
        recuperado = 5
        personagem.status["mana"] += recuperado

        if personagem.status["mana"] > mana_max:
            personagem.status["mana"] = mana_max

        digitar(
            "✅ Esquiva bem-sucedida! "
            f"você recuperou {recuperado} de mana."
        )
        sleep(2)
        return True

    digitar(
        "❌ Esquiva falhou! Você não foi agil o suficiente "
        "e nem conseguiu recuperar mana."
    )
    sleep(2)
    return False


# === PARTE VISUAL ===

def barra(life: Personagem | Inimigo) -> str:
    hp_max = life.status.get("hp", 1)

    if hp_max == 0:
        hp_max = 1

    preenchido = int((life.vida_atual / hp_max) * 10)
    vazio = 10 - preenchido
    return ("#" * preenchido) + ("-" * vazio)


def tabelas(personagem: Personagem, inimigo: Inimigo) -> None:
    def write(info: str, info1: object, info2: object) -> None:
        print(
            "|"
            + f"{info} : {info1}".center(33)
            + "|"
            + " " * 25
            + "|"
            + f"{info} : {info2}".center(33)
            + "|"
        )

    def write2(
        info: str,
        info1: str,
        info2: object,
        info3: object,
    ) -> None:
        print(
            "|"
            + f"{info} : {info2}".center(33)
            + "|"
            + " " * 25
            + "|"
            + f"{info1} : {info3}".center(33)
            + "|"
        )

    def show_life(
        primeiro: Personagem | Inimigo,
        segundo: Personagem | Inimigo,
    ) -> None:
        barra_a = barra(primeiro)
        barra_b = barra(segundo)
        print(
            "|"
            + f"Vida : {barra_a}  {primeiro.vida_atual}/{primeiro.status['hp']}".center(33)
            + "|"
            + " " * 25
            + "|"
            + f"Vida : {barra_b}  {segundo.vida_atual}/{segundo.status['hp']}".center(33)
            + "|"
        )

    print("-" * 35 + " " * 25 + "-" * 35)
    write("Nome", get_nome(personagem), get_nome(inimigo))
    show_life(personagem, inimigo)
    write2("Mana", "Poder", personagem.status["mana"], inimigo.dano)
    print("-" * 35 + " " * 25 + "-" * 35)


def inv(personagem: Personagem, mana_max: int) -> None:
    lista_nome = [item.nome for item in personagem.inventario]

    print("-" * 35)

    if len(lista_nome) != 0:
        lista_nome.append("Sair")

        escolha = inquirer.select(
            message="Itens no inventário: ",
            choices=lista_nome,
        ).execute()

        if escolha == "Sair":
            return

        confirmar = inquirer.confirm(
            message="Você deseja usar o item ?"
        ).execute()

        if confirmar:
            numero = lista_nome.index(escolha)

            if personagem.inventario[numero].categoria == "Utilizaveis":
                personagem.inventario[numero].qtd -= 1
                efeitos = personagem.inventario[numero].efeitos
                descricao = personagem.inventario[numero].descricao

                for efeito in efeitos:
                    if efeito[0] == "vida_atual":
                        personagem.vida_atual += efeito[1]
                        digitar(
                            f"💊 {personagem.nick} recuperou "
                            f"{efeito[1]} de HP!"
                        )

                        if personagem.vida_atual > personagem.status["hp"]:
                            personagem.vida_atual = personagem.status["hp"]

                        digitar(descricao)
                        sleep(2)
                    else:
                        personagem.status[efeito[0]] += efeito[1]
                        digitar(descricao)
                        sleep(2)

                    if personagem.status["mana"] > mana_max:
                        personagem.status["mana"] = mana_max
            else:
                print("Este item não é um utilizavel!")
                input("Pressione enter para voltar...")
                inv(personagem, mana_max)

        print("-" * 35)
    else:
        print("Não há itens no seu inventário!")
        print("-" * 35)


# === FUNÇÕES COMPLEMENTARES ===

def equip(
    personagem: Personagem | Inimigo,
    pericia_principal: str,
) -> float:
    if not hasattr(personagem, "equipamento"):
        return 1

    # A leitura do campo "equipado" é a mesma da implementação original.
    arma = inventario.equipamento.itens["Mãos"]["equipado"]

    if not arma:
        if pericia_principal == "mano a mano":
            digitar(
                "❌Você não tinha uma arma adequada pra esse tipo de "
                "ataque equipada e teve que dar um soco, dano reduzido"
            )
        if pericia_principal == "mira":
            digitar(
                "❌Você não tinha uma arma adequada pra esse tipo de "
                "ataque equipada ent pegou uma pedra no chão e jogou, "
                "dano reduzido"
            )
        return 0.5

    efeitos = getattr(arma, "efeitos", [])
    pericias_arma = [efeito[0] for efeito in efeitos]

    if pericia_principal in pericias_arma:
        return 1

    return 0.5


def xp(personagem: Personagem, inimigo: Inimigo) -> None:
    xp_ganho = inimigo.xp
    personagem.xp += xp_ganho
    digitar(f"Você ganhou {xp_ganho} de xp")


def adv_IA(inimigo: Inimigo, jogador: Personagem) -> None:
    ataque(inimigo, jogador, "mano a mano")


# === INTERAÇÃO COM O JOGADOR ===

def acoes(
    valor: str | tuple[str, str, str],
    personagem: Personagem,
    inimigo: Inimigo,
    mana_max: int,
) -> bool:
    if isinstance(valor, tuple):
        tipo_acao, alcance, pericia = valor

        if tipo_acao == "Ataque Especial":
            if alcance == "Corpo a Corpo":
                return ataque_especial(
                    personagem, inimigo, "mano a mano", pericia
                )

            if alcance == "Longo Alcance":
                return ataque_especial(
                    personagem, inimigo, "mira", pericia
                )

            return False
    else:
        if valor == "Corpo a Corpo":
            return ataque(personagem, inimigo, "mano a mano")

        if valor == "Longo Alcance":
            return ataque(personagem, inimigo, "mira")

        if valor == "Inventário":
            inv(personagem, mana_max)
            return True

        if valor == "Esquivar":
            return esquivar(personagem, mana_max)

    return False


def loop_principal(
    personagem: Personagem,
    inimigo: Inimigo,
    mana_max: int,
) -> None:
    limpar_tela()
    tabelas(personagem, inimigo)
    print()

    while True:
        escolha = inquirer.select(
            message="Qual a sua próxima ação:",
            choices=[
                "Ataque",
                "Ataque Especial",
                "Inventário",
                "Esquivar",
            ],
        ).execute()

        if personagem.vida_atual <= 0:
            digitar(
                "Seu personagem foi reduzido a um amontoado de código."
            )
            return

        if escolha == "Ataque":
            alcance = inquirer.select(
                message="Qual a sua próxima ação:",
                choices=["Corpo a Corpo", "Longo Alcance", "Voltar"],
            ).execute()

            if alcance == "Voltar":
                continue

            valor_acao = alcance

        elif escolha == "Ataque Especial":
            alcance = inquirer.select(
                message="Qual a sua próxima ação:",
                choices=["Corpo a Corpo", "Longo Alcance", "Voltar"],
            ).execute()

            if alcance == "Voltar":
                continue

            pericia = inquirer.select(
                message=(
                    "Escolha qual perícia vc quer usar "
                    "para melhorar o ataque:"
                ),
                choices=[
                    "acrobacia",
                    "blefar",
                    "mira",
                    "diplomacia",
                    "furtividade",
                    "percepção",
                    "maos rapidas",
                    "mano a mano",
                    "resistencia",
                    "Voltar",
                ],
            ).execute()

            if pericia == "Voltar":
                continue

            valor_acao = (escolha, alcance, pericia)

        elif escolha == "Esquivar":
            sucesso = esquivar(personagem, mana_max)
            break

        elif escolha == "Inventário":
            inv(personagem, mana_max)
            continue

        else:
            valor_acao = escolha

        sucesso = acoes(valor_acao, personagem, inimigo, mana_max)

        if sucesso:
            break

        digitar(
            "⚠️ Ação inválida ou mana insuficiente. "
            "Escolha outra ação."
        )
        sleep(2)

    if inimigo.vida_atual > 0:
        adv_IA(inimigo, personagem)


# === FUNÇÃO DO COMBATE ===

def combate(
    personagem: Personagem,
    inimigo: Inimigo,
) -> Personagem | Inimigo | None:
    personagem.vida_atual = (
        personagem.vida_atual
        if personagem.vida_atual > 0
        else personagem.status.get("hp", 100)
    )

    personagem.status["mana"] = (
        personagem.status.get("mana", 100)
        if personagem.status.get("mana", None) is not None
        else 100
    )

    inimigo.vida_atual = inimigo.vida

    inimigo.status["mana"] = (
        inimigo.status.get("mana", 100)
        if inimigo.status.get("mana", None) is not None
        else 100
    )

    print(
        f"\n⚔️ Começando combate: "
        f"{get_nome(personagem)} VS {get_nome(inimigo)}!\n"
    )
    sleep(2)

    while personagem.vida_atual > 0 and inimigo.vida_atual > 0:
        loop_principal(personagem, inimigo, 100)

    if personagem.vida_atual > 0:
        digitar(f"\n🏆 {personagem.nick} venceu o combate!")
        xp(personagem, inimigo)
        processar_evolucao(personagem)
        sleep(3)
        limpar_tela()
        return personagem

    if inimigo.vida_atual > 0:
        digitar(f"\n💀 {personagem.nick} foi derrotado na torre...")

        # Importação local para evitar dependência circular.
        from interface import Interface

        Interface.interface_principal()
        sleep(3)
        limpar_tela()
        return inimigo

    return None


# === EXEMPLO DE EXECUÇÃO ===

if __name__ == "__main__":
    from catalogos import carregar_catalogos

    carregar_catalogos()

    pocao_cura = lista_itens[0]
    pocao_mana = lista_itens[1]

    pocao_cura.qtd = 2
    pocao_mana.qtd = 2

    p1 = Personagem(
        nick="Artemis",
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

    p1.atributos["força"] = 6
    p1.status["hp"] = 100
    p1.status["mana"] = 100
    p1.pericias["mano a mano"] = 20
    p1.pericias["mira"] = 8
    p1.pericias["acrobacia"] = 5
    p1.pericias["resistencia"] = 8
    p1.vida_atual = 100
    p1.xp = 99
    p1.xp_para_proximo_nivel = 100

    p1.inventario.append(pocao_cura)
    p1.inventario.append(pocao_mana)
    p1.inventario.append(lista_itens[5])
    p1.is_player = True

    inventario.equipando(p1, lista_itens[5], "Mãos")

    inimigo = lista_inimigos[0]

    vencedor = combate(p1, inimigo)
