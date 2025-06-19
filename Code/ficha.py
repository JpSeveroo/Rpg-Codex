class Personagem:
    def __init__(self):
        self.nick = ''
        self.raca = ''
        self.classe = ''
        self.xp = 0
        self.nivel = 1
        self.atributos = {
            "forca": 0,
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
        print('='*5, ' CRIAÇÃO DA FICHA CODEX ', '='*5)
        self.nick = input('Nome: ').strip().capitalize()

        print('='*15)
        print('\t\tEscolha uma raça')
        print('='*15)
        print("1. Humano      → +1 em todos os atributos | Sem habilidades especiais")
        print("2. Elfo        → +3 Destreza, +2 Inteligência | -2 Constituição")
        print("3. Draconiano  → +5 Força | -3 Carisma, não usa poções")
        print('='*15)

        racas_validas = {"humano", "elfo", "draconiano"}

        while True:
            self.raca = input('Raça: ').strip().lower()
            if self.raca in racas_validas:
                break
            print("Raça inválida. Tente novamente.")

        print('='*15)
        print("Escolha uma classe:")
        print('='*15)
        print("1. Guerreiro  → +5 Constituição, +3 Força | Mana -20")
        print("2. Ladino     → +5 Destreza, +2 Criatividade | -2 Constituição")
        print("3. Mago       → +7 Inteligência, +30 Mana | -3 Força, -3 Constituição")
        print("4. Clérigo    → +5 Carisma, +3 Inteligência | Só pode usar magias sagradas")
        print('='*15)

        classes_validas = {"guerreiro", "ladino", "mago", "clérigo"}

        while True:
            self.classe = input('Classe: ').strip().lower()
            if self.classe in classes_validas:
                break
            print("Classe inválida. Tente novamente.")

        print('=='*10)
        print('\tDIVISÃO DE PONTOS POR ATRIBUTOS\n')
        print('• FORÇA\n• DESTREZA\n• CONSTITUIÇÃO\n• CARISMA\n• INTELIGÊNCIA')
        print('\n[DICAS]')
        print('* Divida seus pontos sabiamente. Lembre que os bônus da raça e classe virão depois.')
        print('=='*10)

        pontos_disponiveis = 30
        for atributo in self.atributos:
            while True:
                try:
                    pontos = int(input(f'{atributo.capitalize()}: '))
                    if 0 <= pontos <= pontos_disponiveis:
                        self.atributos[atributo] = pontos
                        pontos_disponiveis -= pontos
                        print(f"Pontos restantes: {pontos_disponiveis}")
                        break
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Digite um número válido.")

        # Bônus de raça
        if self.raca == 'humano':
            for chave in self.atributos:
                self.atributos[chave] += 1
        elif self.raca == "elfo":
            self.atributos["destreza"] += 3
            self.atributos["inteligencia"] += 2
            self.atributos["constituicao"] -= 2
        elif self.raca == "draconiano":
            self.atributos["forca"] += 5
            self.atributos["carisma"] -= 3

        # Bônus de classe e status
        if self.classe == "guerreiro":
            self.atributos["constituicao"] += 5
            self.atributos["forca"] += 3
            self.status = {"hp": 120, "mana": 30}
        elif self.classe == "ladino":
            self.atributos["destreza"] += 5
            self.atributos["constituicao"] -= 2
            self.atributos["inteligencia"] += 2
            self.status = {"hp": 90, "mana": 60}
        elif self.classe == "mago":
            self.atributos["inteligencia"] += 7
            self.atributos["forca"] -= 3
            self.atributos["constituicao"] -= 3
            self.status = {"hp": 80, "mana": 80}
        elif self.classe == "clérigo":
            self.atributos["carisma"] += 5
            self.atributos["inteligencia"] += 3
            self.status = {"hp": 100, "mana": 70}

        # Calcular as perícias
        self.calcular_pericias()
        print("\nFicha criada com sucesso!")

    def calcular_pericias(self):
        self.pericias = {
            "acrobacia": self.atributos["destreza"],
            "blefar": self.atributos["carisma"],
            "cura": self.atributos["inteligencia"],
            "criatividade": self.atributos["destreza"],
            "diplomacia": self.atributos["inteligencia"],
            "percepcao": self.atributos["inteligencia"],
            "maos_rapidas": self.atributos["destreza"],
            "sobrevivencia": self.atributos["forca"]
        }

    def visualizar(self):
        print(f"\n--- Ficha de {self.nick} ---")
        print(f"Raça: {self.raca.capitalize()} | Classe: {self.classe.capitalize()}")
        print(f"Nível: {self.nivel} | XP: {self.xp}")
        print("\nAtributos:")
        for k, v in self.atributos.items():
            print(f"  {k.capitalize()}: {v}")
        print("\nPerícias:")
        for k, v in self.pericias.items():
            print(f"  {k.capitalize()}: {v}")
        print(f"\nHP: {self.status['hp']} | Mana: {self.status['mana']}")
        print("------------------------------")

if __name__ == "__main__":
    p = Personagem()
    p.criar_ficha()
    p.visualizar()