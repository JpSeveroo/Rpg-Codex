def criar_ficha():
    print('='*5, ' CRIAÇÃO DA FICHA CODEX ', '='*5)

    nick = input('Nome: ').strip().lower()

    print('='*15)
    print('\t\tEscolha uma raça'.upper())
    print('='*15)
    print("1. Humano      → +1 em todos os atributos | Sem habilidades especiais")
    print("2. Elfo        → +3 Destreza, +2 Inteligência | -2 Constituição")
    print("3. Draconiano  → +5 Força | -3 Carisma, não usa poções")
    print("4. Vampiro     → +5 Carisma, regenera 5 HP por turno | -5 resistência mágica")
    print('='*15)

    racas_validas = {
        "humano", "elfo", "draconiano", "vampiro"
    }
    
    while True:
        raca = input('Raça: ').strip().lower()
        if raca in racas_validas:
            break
        print("Raça inválida. Tente novamente.")
#Esquema de escolha  da raça acima, acho que dá pra colocar uns try except pra verficação,
#  mas por enquanto estou fazendo o escopo geral. O mesmo serve pras classes abaixo

    print('='*15)
    print("\nEscolha uma classe:".upper())
    print('='*15)
    print("1. Guerreiro  → +5 Constituição, +3 Força | Mana -20")
    print("2. Ladino     → +5 Destreza, +2 Criatividade | -2 Constituição")
    print("3. Mago       → +7 Inteligência, +30 Mana | -3 Força, -3 Constituição")
    print("4. Clérigo    → +5 Carisma, +3 Inteligência | Só pode usar magias sagradas")
    print('='*15)

    classes_validas = {
        "guerreiro", "ladino", "mago", "clérigo"
    }

    while True:
        classe = input('Classe: ').strip().lower()
        if classe in classes_validas:
            break
        print("Classe inválida. Tente novamente.")

if __name__ == '__main__':
    criar_ficha()

#A seguir tem que fazer o esquema de distribuição de pontos por atributos(30 pontos) conforme o gosto do usuário e em seguida 
# fazer o balanceamento conforme a escolha de classe e raça. Posteriormente vincular as pericias com os atributos. Fazer o return 
# da ficha completa e exibir que a ficha foi criada com sucesso terminando essa função criada

#Depois criar uma função pra salvar a ficha em arquivo json

#Depois criar uma função pra carregar a ficha