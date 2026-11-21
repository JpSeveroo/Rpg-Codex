from time import sleep
import utills

class Personagem:

    tabela_xp = {
        1: 100, 2: 120, 3: 150, 4: 170, 5: 190,
        6: 200, 7: 220, 8: 240, 9: 250, 10: 270,
        11: 300, 12: 320, 13: 340, 14: 350, 15: 400,
        16: 450, 17: 500, 18: 520, 19: 550, 20: 600,
        21: 650, 22: 700, 23: 800, 24: 900, 25: 950,
        26: 1100, 27: 1200, 28: 1300, 29: 1450, 30: float('inf')
    }

    def __init__(self):
        self.nick = ''
        self.raca = ''
        self.classe = ''
        self.xp = 0
        self.nivel = 1
        self.xp_para_proximo_nivel = self.tabela_xp.get(self.nivel, 100)
        self.atributos = {
            "força": 0,
            "destreza": 0,
            "constituicao": 0,
            "carisma": 0,
            "inteligencia": 0
        }
        self.pericias = {
            "acrobacia": 0,
            "blefar": 0,
            "mira": 0,
            "diplomacia": 0,
            "furtividade": 0,
            "percepcao": 0,
            "maos rapidas": 0,
            "mano a mano": 0,
            "resistencia": 0
        }
        self.inventario = []
        self.fraquezas = []
        self.status = {"hp": 100, "mana": 100}
        self.mana_max = self.status['mana']
        self.vida_atual = self.status["hp"]
        self.equipamento = {
            "maos": None,
}
        self.andar_esfinge_completado = False
        self.andar_cupula_completado = False
        self.checkpoint = 0

    def criar_ficha(self):
        print()
        print('='*22,'\t    📋 CRIAÇÃO DA FICHA CODEX\t ','='*22)
        print("\n⚠️  AVISO: Você poderá revisar e alterar as informações da ficha antes da criação final.")
        print("✅ Siga os passos normalmente. No final, será perguntado se deseja confirmar ou refazer a ficha.\n")

        self.nick = input('Nome: ').strip()

        sleep(1)
        print('='*85)
        print('\t\t\tEscolha uma raça')
        print('='*85)
        print("1. 👨 Humano      → +1 em todos os atributos     | Sem reduções")
        print("2. 🧝 Elfo        → +3 Destreza, +2 Inteligência | -2 Resistência")
        print("3. 🐲 Draconiano  → +5 Força                     | -2 Diplomacia")
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
        print("⚔️  1. Guerreiro  →  +8 Força        | +2 Destreza     | -3 Diplomacia")
        print("🥷  2. Ladino     →  +5 Destreza     | +5 Inteligência | -3 Resistência")
        print("🔮  3. Mago       →  +7 Inteligência | +3 Carisma      | -3 Mano a mano")
        print("🪷  4. Clérigo    →  +5 Carisma      | +5 Destreza     | -3 Furtividade")
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

        #calcula hp baseado na constituição
        self.status["hp"] = 100 + (self.atributos["constituicao"] * 5)
        self.vida_atual = self.status["hp"]

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
            "maos rapidas": self.atributos["destreza"],
            "mano a mano": self.atributos["força"],
            "resistencia": self.atributos["força"]
        }
    
    def evoluir_nivel(self):
        while self.nivel < max(self.tabela_xp.keys()) and self.xp >= self.tabela_xp[self.nivel]:
            xp_necessario = self.tabela_xp[self.nivel]
            self.xp -= xp_necessario
            self.nivel += 1
            self.xp_para_proximo_nivel = self.tabela_xp.get(self.nivel, float('inf'))

            utills.digitar(f"\n🎉 Parabéns, {self.nick}! Você alcançou o Nível {self.nivel}!")

            pontos_disponiveis = 5
            utills.digitar(f"Você tem {pontos_disponiveis} pontos para distribuir entre seus atributos.")
            atributos = list(self.atributos.keys())

            while pontos_disponiveis > 0:
                utills.digitar("\n✨ Atributos disponíveis:")
                for i, nome in enumerate(atributos, 1):
                    print(f"  {i}. {nome.capitalize()}: {self.atributos[nome]}")

                try:
                    escolha = int(input(f"Escolha o número do atributo (pontos restantes: {pontos_disponiveis}): "))
                    if not 1 <= escolha <= len(atributos):
                        utills.digitar("❌ Escolha inválida.")
                        continue

                    atributo = atributos[escolha - 1]

                    qtd = int(input(f"Quantos pontos deseja adicionar a {atributo.capitalize()}? "))
                    if not 1 <= qtd <= pontos_disponiveis:
                        utills.digitar(f"❌ Você pode adicionar entre 1 e {pontos_disponiveis} pontos.")
                        continue

                    self.atributos[atributo] += qtd
                    pontos_disponiveis -= qtd
                    utills.digitar(f"✅ {qtd} pontos adicionados a {atributo.capitalize()}.")

                except ValueError:
                    utills.digitar("❌ Digite um número válido.")

                self.calcular_pericias()
                utills.digitar("\n✨ Atributos atualizados com sucesso!")
                sleep(3)

        if self.nivel >= max(self.tabela_xp.keys()):
            self.xp_para_proximo_nivel = float('inf')
            utills.digitar(f"🏆 {self.nick} atingiu o nível máximo!")
        else:
            self.xp_para_proximo_nivel = self.tabela_xp.get(self.nivel, float('inf'))

    def mostrar_status(self):
        print(f"\n🧾 Status de {self.nick}")
        print(f"🎚️ Nível {self.nivel} | 💠 XP: {self.xp}/{self.xp_para_proximo_nivel}")
        print(f"❤️ Vida: {self.vida_atual}/{self.status['hp']} | 🔮 Mana: {self.status['mana']}/{self.mana_max}")
    
        print("\n🧬 Atributos:")
        for atr, val in self.atributos.items():
            print(f"  {atr.capitalize():<13}: {val}")
        print()

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
