from time import sleep
class Personagem:
    def __init__(self):
        self.nick = ''
        self.raca = ''
        self.classe = ''
        self.xp = 0
        self.nivel = 1
        self.atributos = {
            "força": 0,
            "destreza": 0,
            "constituicao": 0,
            "carisma": 0,
            "inteligencia": 0
        }
        self.pericias = {}
        self.inventario = []
        self.historico = []
        self.status = {"hp": 100, "mana": 50}

    def criar_ficha(self):
        print()
        print('='*22,'\t    📋 CRIAÇÃO DA FICHA CODEX\t ','='*22)
        print("\n⚠️  AVISO: Você poderá revisar e alterar as informações da ficha antes da criação final.")
        print("✅ Siga os passos normalmente. No final, será perguntado se deseja confirmar ou refazer a ficha.\n")

        self.nick = input('Nome: ').strip().capitalize()

        sleep(1)
        print('='*85)
        print('\t\t\tEscolha uma raça')
        print('='*85)
        print("1. 👨 Humano      → +1 em todos os atributos     | Sem habilidades especiais")
        print("2. 🧝 Elfo        → +3 Destreza, +2 Inteligência | -2 Constituição")
        print("3. 🐲 Draconiano  → +5 Força                     | -3 Carisma, não usa poções")
        print('='*85)

        racas_validas = {"humano", "elfo", "draconiano"}

        while True:
            escolha_raca = input('Escolha uma raça: ').strip().lower()
            if escolha_raca == '1' or escolha_raca == 'humano':
                self.raca = 'humano'
            elif escolha_raca == '2' or escolha_raca == 'elfo':
                self.raca = 'elfo'
            elif escolha_raca == '3' or escolha_raca == 'draconiano':
                self.raca = 'draconiano'
            if self.raca in racas_validas:
                break
            print("❌Raça inválida. Tente novamente.")

        sleep(1)
        print()
        print('='*85)
        print("\t\t\tEscolha uma classe:")
        print('='*85)
        print("⚔️  1. Guerreiro  →  +5 Constituição | +3 Força        | -20 Mana")
        print("🥷  2. Ladino     →  +5 Destreza     | +2 Criatividade | -2 Constituição")
        print("🔮 3. Mago       →  +7 Inteligência | +30 Mana        | -3 Força e -3 Constituição")
        print("🪷  4. Clérigo    →  +5 Carisma      | +3 Inteligência | Só pode usar magias sagradas")
        print('='*85)

        classes_validas = {"guerreiro", "ladino", "mago", "clérigo"}

        while True:
            escolha_classe = input('Escolha uma classe: ').strip().lower()
            if escolha_classe == '1' or escolha_classe == 'guerreiro':
                self.classe = 'guerreiro'
            elif escolha_classe == '2' or escolha_classe == 'ladino':
                self.classe = 'ladino'
            elif escolha_classe == '3' or escolha_classe == 'mago':
                self.classe = 'mago'
            elif escolha_classe == '4' or escolha_classe == 'clérigo':
                self.classe = 'clérigo'
            if self.classe in classes_validas:
                break
            print("❌ Classe inválida. Tente novamente.")

        while True:
            pontos_disponiveis = 30
            temp_atributos = {attr: 0 for attr in self.atributos}

            sleep(1)
            print()
            print('='*50)
            print("\tDivisão de pontos por atributos:")
            print('='*50)
            print('\t💪 → FORÇA\n\t🏹 → DESTREZA\n\t🩸 → CONSTITUIÇÃO\n\t💞 → CARISMA\n\t🧠 → INTELIGÊNCIA')
            print('\n[ DICAS ]')
            print('*** Você tem 30 pontos, divida-os sabiamente. \n*** Lembre que os bônus da raça e classe virão depois.')
            print('='*50)

            for atributo in temp_atributos:
                while True:
                    try:
                        pontos = int(input(f'{atributo.capitalize()} (pontos restantes: {pontos_disponiveis}):'))
                        if 0 <= pontos <= pontos_disponiveis:
                            temp_atributos[atributo] = pontos
                            pontos_disponiveis -= pontos
                            break
                        else:
                            print(f"❌ Número inválido. Você pode alocar entre 0 e {pontos_disponiveis} pontos.")
                    except ValueError:
                        print("❌ Digite um número válido.")
            if pontos_disponiveis == 0:
                self.atributos = temp_atributos
                break
            else:
                print(f"\n❗ Você deixou {pontos_disponiveis} pontos sem alocar ou alocou mais do que o permitido.")
                print("Por favor, redistribua seus pontos.")
                input("Pressione Enter para tentar novamente...")   

        # Bônus de raça
        if self.raca == 'humano':
            for chave in self.atributos:
                self.atributos[chave] += 1
        elif self.raca == "elfo":
            self.atributos["destreza"] += 3
            self.atributos["inteligencia"] += 2
            self.atributos["constituicao"] -= 2
        elif self.raca == "draconiano":
            self.atributos["força"] += 5
            self.atributos["carisma"] -= 3

        # Bônus de classe e status
        if self.classe == "guerreiro":
            self.atributos["constituicao"] += 5
            self.atributos["força"] += 3
            self.status = {"hp": 120, "mana": 30}
        elif self.classe == "ladino":
            self.atributos["destreza"] += 5
            self.atributos["constituicao"] -= 2
            self.atributos["inteligencia"] += 2
            self.status = {"hp": 90, "mana": 60}
        elif self.classe == "mago":
            self.atributos["inteligencia"] += 7
            self.atributos["força"] -= 3
            self.atributos["constituicao"] -= 3
            self.status = {"hp": 80, "mana": 80}
        elif self.classe == "clérigo":
            self.atributos["carisma"] += 5
            self.atributos["inteligencia"] += 3
            self.status = {"hp": 100, "mana": 70}

        # Calcular as perícias
        self.calcular_pericias()
        sleep(1)

        while True:
            print()
            confirmar = input("📝 Deseja confirmar a criação desta ficha? (s/n): ").strip().lower()
            if confirmar == "s":
                print("\n============= 🎊 Ficha criada com sucesso! =============")
                break
            elif confirmar == "n":
                print("\n🔁 Recomeçando a criação da ficha...")
                sleep(1)
                self.__init__()  # reseta o personagem
                self.criar_ficha()
                return  # sai da função atual para evitar sobreposição
            else:
                print("❌ Resposta inválida. Digite apenas 's' para sim ou 'n' para não.")

    def calcular_pericias(self):
        self.pericias = {
            "acrobacia": self.atributos["destreza"],
            "blefar": self.atributos["carisma"],
            "mira": self.atributos["destreza"],
            "diplomacia": self.atributos["carisma"],
            "furtividade": self.atributos["inteligencia"],
            "percepcao": self.atributos["inteligencia"],
            "maos_rapidas": self.atributos["destreza"],
            "mano_a_mano": self.atributos["força"],
            "resistencia": self.atributos["força"]
        }

    def visualizar(self):
        sleep(1)
        print(f"\n--------- Ficha de {self.nick} ---------")
        print(f"🧌  Raça: {self.raca.capitalize()} | 💼 Classe: {self.classe.capitalize()}")
        print(f"⭐ Nível: {self.nivel}   | 💠 XP: {self.xp}")
        print("\n✨ Atributos:")
        for k, v in self.atributos.items():
            print(f"  {k.capitalize()}: {v}")
        print("\n🦾 Perícias:")
        for k, v in self.pericias.items():
            print(f"  {k.capitalize()}: {v}")
        print(f"\n💖 HP: {self.status['hp']} | 🫧  Mana: {self.status['mana']}")
        print("------------------------------")
        print()

if __name__ == "__main__":
    p = Personagem()
    p.criar_ficha()
    p.visualizar()
