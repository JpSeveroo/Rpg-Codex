
from collections.abc import Mapping
from time import sleep

from models.personagem import Personagem
from utills import digitar

_ATRIBUTOS = (
    "força",
    "destreza",
    "constituicao",
    "carisma",
    "inteligencia",
)

_RACAS = {
    "1": "humano",
    "2": "elfo",
    "3": "draconiano",
}

_CLASSES = {
    "1": "guerreiro",
    "2": "ladino",
    "3": "mago",
    "4": "clérigo",
}


def _selecionar_opcao(
    mensagem: str,
    opcoes: dict[str, str],
) -> str:
    while True:
        escolha = input(mensagem).strip().lower()

        if escolha in opcoes:
            return opcoes[escolha]

        if escolha in opcoes.values():
            return escolha

        print("❌ Opção inválida. Tente novamente.")


def _solicitar_inteiro(
    mensagem: str,
    minimo: int,
    maximo: int,
) -> int:
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("❌ Digite um número válido.")
            continue

        if minimo <= valor <= maximo:
            return valor

        print(
            f"❌ O valor deve estar entre {minimo} e {maximo}."
        )


def _distribuir_pontos(
    atributos: tuple[str, ...],
    total: int,
    *,
    distribuicao_livre: bool = False,
    valores_atuais: Mapping[str, int] | None = None,
) -> dict[str, int]:
    if not distribuicao_livre:
        while True:
            distribuicao = dict.fromkeys(atributos, 0)
            restantes = total

            for atributo in atributos:
                pontos = _solicitar_inteiro(
                    f"{atributo.capitalize()} "
                    f"(pontos restantes: {restantes}): ",
                    0,
                    restantes,
                )

                distribuicao[atributo] = pontos
                restantes -= pontos

            if restantes == 0:
                return distribuicao

            print(
                f"\n❗ Você deixou {restantes} pontos "
                "sem distribuir."
            )
            print("Por favor, redistribua seus pontos.")
            input("Pressione Enter para tentar novamente...")

    distribuicao = dict.fromkeys(atributos, 0)
    restantes = total

    while restantes > 0:
        digitar("\n✨ Atributos disponíveis:")

        for indice, atributo in enumerate(atributos, 1):
            valor_atual = (
                valores_atuais[atributo]
                if valores_atuais is not None
                else 0
            )

            print(
                f"  {indice}. {atributo.capitalize()}: "
                f"{valor_atual + distribuicao[atributo]}"
            )

        escolha = _solicitar_inteiro(
            f"Escolha o número do atributo "
            f"(pontos restantes: {restantes}): ",
            1,
            len(atributos),
        )

        atributo = atributos[escolha - 1]

        quantidade = _solicitar_inteiro(
            f"Quantos pontos deseja adicionar "
            f"a {atributo.capitalize()}? ",
            1,
            restantes,
        )

        distribuicao[atributo] += quantidade
        restantes -= quantidade

        digitar(
            f"✅ {quantidade} pontos adicionados "
            f"a {atributo.capitalize()}."
        )

    return distribuicao


def _solicitar_nome(nomes_existentes: set[str]) -> str:
    while True:
        nome = input("Nome: ").strip()

        if nome not in nomes_existentes:
            return nome

        print(
            "O nome escolhido para o personagem "
            "não está disponível."
        )


def criar_personagem(
    nomes_existentes: set[str],
) -> Personagem:
    while True:
        print()
        print(
            "=" * 22,
            "\t    📋 CRIAÇÃO DA FICHA CODEX\t",
            "=" * 22,
        )
        print(
            "\n⚠️ Você poderá revisar as informações "
            "antes de confirmar a criação."
        )

        nome = _solicitar_nome(nomes_existentes)

        sleep(1)
        print("=" * 85)
        print("\t\t\tEscolha uma raça")
        print("=" * 85)
        print("1. 👨 Humano      → +1 em todos os atributos")
        print(
            "2. 🧝 Elfo        → +3 Destreza, "
            "+2 Inteligência | -2 Constituição"
        )
        print(
            "3. 🐲 Draconiano  → +5 Força | -3 Carisma"
        )
        print("=" * 85)

        raca = _selecionar_opcao("Escolha uma raça: ", _RACAS)

        sleep(1)
        print()
        print("=" * 85)
        print("\t\t\tEscolha uma classe:")
        print("=" * 85)
        print(
            "1. ⚔️ Guerreiro  → +8 Força, "
            "+2 Destreza | -3 Diplomacia"
        )
        print(
            "2. 🥷 Ladino     → +5 Destreza, "
            "+5 Inteligência | -3 Resistência"
        )
        print(
            "3. 🔮 Mago       → +7 Inteligência, "
            "+3 Carisma | -3 Mano a mano"
        )
        print(
            "4. 🪷 Clérigo    → +5 Carisma, "
            "+5 Destreza | -3 Furtividade"
        )
        print("=" * 85)

        classe = _selecionar_opcao(
            "Escolha uma classe: ",
            _CLASSES,
        )

        sleep(1)
        print()
        print("=" * 50)
        print("\tDivisão de pontos por atributos:")
        print("=" * 50)
        print(
            "\t💪 → FORÇA\n"
            "\t🏹 → DESTREZA\n"
            "\t🩸 → CONSTITUIÇÃO\n"
            "\t💞 → CARISMA\n"
            "\t🧠 → INTELIGÊNCIA"
        )
        print("\n[ DICAS ]")
        print(
            "*** Você tem 30 pontos. "
            "Divida-os sabiamente."
        )
        print(
            "*** Os bônus da raça e da classe "
            "serão aplicados depois."
        )
        print("=" * 50)

        atributos = _distribuir_pontos(
            _ATRIBUTOS,
            total=30,
        )

        personagem = Personagem(
            nick=nome,
            raca=raca,
            classe=classe,
            atributos=atributos,
        )

        mostrar_ficha(personagem)

        while True:
            confirmar = input(
                "📝 Deseja confirmar a criação "
                "desta ficha? (s/n): "
            ).strip().lower()

            if confirmar == "s":
                print(
                    "\n============= 🎊 Ficha criada "
                    "com sucesso! ============="
                )
                return personagem

            if confirmar == "n":
                print(
                    "\n🔁 Recomeçando a criação da ficha..."
                )
                sleep(1)
                break

            print(
                "❌ Resposta inválida. "
                "Digite apenas 's' ou 'n'."
            )


def mostrar_status(personagem: Personagem) -> None:
    print(f"\n🧾 Status de {personagem.nick}")
    print(
        f"🎚️ Nível {personagem.nivel} | "
        f"💠 XP: {personagem.xp}/"
        f"{personagem.xp_para_proximo_nivel}"
    )
    print(
        f"❤️ Vida: {personagem.vida_atual}/"
        f"{personagem.status['hp']} | "
        f"🔮 Mana: {personagem.status['mana']}/"
        f"{personagem.mana_max}"
    )

    print("\n🧬 Atributos:")

    for atributo, valor in personagem.atributos.items():
        print(f"  {atributo.capitalize():<13}: {valor}")

    print()


def mostrar_ficha(personagem: Personagem) -> None:
    sleep(1)

    print(f"\n--------- Ficha de {personagem.nick} ---------")
    print(
        f"🧌 Raça: {personagem.raca.capitalize()} | "
        f"💼 Classe: {personagem.classe.capitalize()}"
    )
    print(
        f"⭐ Nível: {personagem.nivel} | "
        f"💠 XP: {personagem.xp}"
    )

    print("\n✨ Atributos:")

    for atributo, valor in personagem.atributos.items():
        print(f"  {atributo.capitalize()}: {valor}")

    print("\n🦾 Perícias:")

    for pericia, valor in personagem.pericias.items():
        print(f"  {pericia.capitalize()}: {valor}")

    print(
        f"\n💖 HP: {personagem.status['hp']} | "
        f"🫧 Mana: {personagem.status['mana']}"
    )
    print("------------------------------")
    print()


def processar_evolucao(personagem: Personagem) -> int:
    evolucoes = 0

    while personagem.pode_evoluir():
        proximo_nivel = personagem.nivel + 1

        digitar(
            f"\n🎉 Parabéns, {personagem.nick}! "
            f"Você alcançou o Nível {proximo_nivel}!"
        )
        digitar(
            "Você tem 5 pontos para distribuir "
            "entre seus atributos."
        )

        distribuicao = _distribuir_pontos(
            tuple(personagem.atributos),
            total=5,
            distribuicao_livre=True,
            valores_atuais=personagem.atributos,
        )

        if personagem.evoluir_nivel(distribuicao):
            evolucoes += 1
            digitar("\n✨ Atributos atualizados com sucesso!")
            sleep(3)

    if personagem.nivel >= max(personagem.tabela_xp):
        digitar(
            f"🏆 {personagem.nick} atingiu o nível máximo!"
        )

    return evolucoes
