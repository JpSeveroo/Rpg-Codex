import os
import random
import time

from rich import print

import gameplay.inventario as inventario
import story.jogo1 as jogo1
from catalogos import lista_itens


def lore_11_andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')

    texto1 = ('Quando seus pés tocam o solo do 11° andar, você sente algo diferente. O ambiente não pulsa. Ele... chora. À sua frente se estende um longo corredor de pedra digitalizada, de arquitetura pesada, como se tivesse sido construída com a própria culpa dos que falharam. As paredes vibram com inscrições quebradas: nomes de Echos esquecidos, sentenças de falhas, gritos engasgados em linhas de código.')
    jogo1.digitar(texto1)

    texto2 = ('\nA cada passo, fragmentos de vozes ecoam — não altos, não ameaçadores — apenas tristes.')
    jogo1.digitar(texto2)
    print('\n[bold blue][italic]“Eu quase alcancei…”\n“Era só mais uma decisão… só mais uma chance…”\n“Eles disseram que eu não era forte… talvez estivessem certos…”[/italic][/bold blue]\n')

    texto3 = ('Você percebe que essas vozes não são gravações… são presenças. Sombras sem forma se arrastam pelas laterais do corredor, tentando evitar a luz tênue que emana de vitrais distorcidos no teto. São como ecos vivos da desistência, retorcidos por remorso. É então que elas surgem: os Lamentadores, Seres espectrais sem rosto, feitos de névoa e lembranças mal resolvidas. Seus corpos oscilam como dados instáveis, e seus olhos — se é que têm — brilham com o vazio daquilo que nunca foi concluído. Eles não atacam de imediato. Eles se aproximam em silêncio, murmurando o nome do jogador, e depois... as falas de seus erros passados. Como se soubessem de tudo. Eles não querem só ferir. Querem desistência. Querem que você se junte a eles. Cada Lamentador parece carregar dentro de si o último pensamento de um Echo derrotado. E quanto mais deles se aproximam, mais pesada se torna a atmosfera.')
    jogo1.digitar(texto3)

    print('[bold purple][Sistema]Andar 11 detectado. Presença de Lamentadores em estado ativo.]\n[Sistema] Aviso. Exposição prolongada à influência dos Lamentadores reduz resistência emocional e integridade cognitiva.[bold purple]')

    while True:
        texto4 = '\n1. Iniciar combate direto.\n2. Tentar purificá-los — Se você possui fragmentos de lore suficientes, pode tentar redimir suas almas com palavras e lembranças. \n3. Investigar inventário\n4. Conferir Atributos'
        jogo1.digitar(texto4)

        try:
            time.sleep(1)
            esc_1 = input("\nEscolha uma opção: ").strip()
            if esc_1 not in ("1","2","3","4"):
                raise ValueError("❗ Opção inválida.")
            if esc_1 == "1":
                #COMBATEEE
                lore_recompensa001(personagem)
                lore_pos_11andar(personagem)
                break
            elif esc_1 == "2":
                break
                 #PEGAR OS FRAGMENTOS ANTERIORES E VER SE O USUARIO TEM NO INVENTARIO

            elif esc_1 == "3":
                inventario.interface_inv(personagem)
            elif esc_1 == "4":
                #ATRIBUTOSSSS
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa001(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    personagem.inventario[0].qtd += 3
    personagem.inventario[1].qtd += 3
    personagem.inventario.append(lista_itens[79])

    item_escolhido001 = ''
    
    if personagem.raca == 'elfo':
        while True:
            try:
                texto4 = ("\nQual destes 3 itens você deseja levar consigo? \n ⚰️[1] Manto das Sombras Dilaceradas: Este manto escuro parece rasgado pelas bordas, mas as fendas se movem como se fossem rasgos na própria realidade. Envolve o portador em sombras vivas, facilitando desaparecimentos e movimentos furtivos. (+3 furtividade)\n 🗡️[2] Adaga da Lâmina Partida: Uma adaga aparentemente quebrada, mas cuja lâmina incompleta vibra com magia ancestral. Ideal para golpes rápidos e traiçoeiros, sua aparência danificada engana os inimigos, mas dificulta bloqueios ou defesas prolongadas. (+3 mano a mano), (+3 mãos rápidas), (-3resistência)\n 🔇[3]Bracelete do Eco Silencioso: Feito de metal prateado e fino como teia de aranha, este bracelete amplifica a sensibilidade do portador aos sons e vibrações ao redor, facilitando perceber armadilhas ou presenças ocultas. (+3 percepção)")
                jogo1.digitar(texto4)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa001 = input().strip()

                if recompensa001 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa001 == "1":
                    personagem.inventario.append(lista_itens[51])
                    item_escolhido001 = '⚰️ Manto das Sombras Dilaceradas'
                    print()

                elif recompensa001 == "2":
                    personagem.inventario.append(lista_itens[52])
                    item_escolhido001 = '🗡️ Adaga da Lâmina Partida'
                    print()
                elif recompensa001 == "3":  
                    personagem.inventario.append(lista_itens[53])
                    item_escolhido001 = '🔇 Bracelete do Eco Silencioso'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")
    
    elif personagem.raca == 'humano':
        while True:
            try:
                texto5 = ("\nQual destes 3 itens você deseja levar consigo? \n ⚔️[1] Espada do Lamento Estilhaçado: Espada longa de aço escurecido com rachaduras ao longo da lâmina. Cada golpe emite um leve som agudo, como um lamento distante, que perturba os oponentes. Apesar do aspecto danificado, a lâmina é resistente e eficiente. (+3 mano a mano)\n 🛡️[2] Escudo do Juramento Ruído: Escudo metálico de formato irregular, com a superfície coberta por símbolos apagados e riscos profundos. Ele abafa sons ao redor quando erguido, protegendo não só fisicamente, mas criando uma breve zona de silêncio. Contudo, seu peso reduz um pouco a mobilidade. (+3 resistência), (+3 furtividade), (-3 acrobacia)\n 🧤[3] Luvas do Sentinela Esquecido: Luvas de couro reforçado com pequenas placas metálicas nas costas das mãos. Facilitam o manuseio rápido de armas ou objetos, mas o toque frio e áspero reduz a precisão em tarefas delicadas. (+3 mãos rápidas), (+3 mira), (-3 blefar)")
                jogo1.digitar(texto5)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa001 = input().strip()

                if recompensa001 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa001 == "1":
                    personagem.inventario.append(lista_itens[54])
                    item_escolhido001 = '⚔️ Espada do Lamento Estilhaçado'
                    print()

                elif recompensa001 == "2":
                    personagem.inventario.append(lista_itens[55])
                    item_escolhido001 = '🛡️ Escudo do Juramento Ruído'
                    print()
                elif recompensa001 == "3":
                    personagem.inventario.append(lista_itens[56])
                    item_escolhido001 = '🧤 Luvas do Sentinela Esquecido'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")

    elif personagem.raca == 'draconiano':
        while True:
            try:
                texto6 = ("\nQual destes 3 itens você deseja levar consigo? \n 🧤[1] Manoplas do Rugido Quebrado: Manoplas de metal escuro, marcadas por batalhas, que amplificam a força do portador em combate corpo a corpo. Cada golpe ecoa um rugido abafado, mas o peso excessivo dificulta movimentos rápidos. (+3 mano a mano), (+3 resistência), (-3 acrobacia)\n 🐍[2] Cinturão das Mandíbulas Rachadas: Cinturão largo feito de couro reforçado com placas metálicas danificadas. Aumenta a resistência física e a capacidade de suportar danos. (+3 resistência)\n 👀[3] Elmo do Olho de Falcão: Elmo de metal com uma viseira móvel que amplia a visão do portador, destacando movimentos e detalhes distantes. Aumenta significativamente a percepção. (+3 percepção)")
                jogo1.digitar(texto6)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa001 = input().strip()

                if recompensa001 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa001 == "1":
                    personagem.inventario.append(lista_itens[57])
                    item_escolhido001 = '🧤 Manoplas do Rugido Quebrado'
                    print()

                elif recompensa001 == "2":
                    personagem.inventario.append(lista_itens[58])
                    item_escolhido001 = '🐍 Cinturão das Mandíbulas Rachadas'
                    print()
                elif recompensa001 == "3":
                    personagem.inventario.append(lista_itens[59])
                    item_escolhido001 = '👀 Elmo do Olho de Falcão'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")


    print(f'[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [450] \nPoção de cura [3]\nPoção de mana [3]\nItem: {item_escolhido001}, 📜 Fragmento de Lore — "Registro Refletido" Unidade Eco-10[/bold purple]')
    text_inf = ('\nPressione ENTER para prosseguir...')
    jogo1.digitar(text_inf)
    input('')

def lore_pos_11andar(personagem):
    texto5 = ('Os últimos Lamentadores se dissolvem lentamente, não em fragmentos de código como os inimigos anteriores, mas em luz suave, como se tivessem sido libertos de uma dor ancestral. Aqueles que você enfrentou ruíram em silêncio, mas os que você purificou… sorriram antes de partir — ou ao menos, você acha que sorriram.\nO Velório das Vozes silencia de vez.\nO chão, antes repleto de inscrições trêmulas, agora está limpo. Onde antes estavam nomes incompletos, surge apenas uma única inscrição:')
    jogo1.digitar(texto5)

    print('[bold blue][italic]\n"Aqueles que escutam a dor dos outros não a carregam sozinhos."\n"Siga.\n"[/italic][/bold blue]')

    texto6 = ('Uma porta de mármore digital se abre, sem som, apenas com uma corrente de ar que parece respirar.')
    jogo1.digitar(texto6)

    print('\n[bold purple][Sistema] Fragmento memorial restaurado. Você foi lembrado pelas vozes que salvou.[bold purple]\n')

    texto7 = ('Você sente como se algo antigo e obscuro tivesse sido deixado para trás. Mas o caminho continua.')
    jogo1.digitar(texto7)

    while True:
        texto8 = '\n1. Avançar para o próximo andar.\n2.  Conferir atributos \n3. Investigar inventário'
        jogo1.digitar(texto8)

        try:
            time.sleep(1)
            esc_2 = input("\nEscolha uma opção: ").strip()
            if esc_2 not in ("1","2","3"):
                raise ValueError("❗ Opção inválida.")
            if esc_2 == "1":
                lore_12_andar(personagem)
                break
            elif esc_2 == "2":
                #Conferir atributos
                print()

            elif esc_2 == "3":
                inventario.interface_inv(personagem)
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_12_andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')

    texto9 = ('O chão desaparece sob seus pés, e você sente seu corpo — ou o que restou dele — ser puxado para baixo, girado, lançado... até finalmente ser arremessado em um novo ambiente. Você desperta de pé, ou quase, em uma plataforma circular girando lentamente no vazio. Acima, abaixo e ao redor de você, colossais engrenagens vivas se movem em um balé mecânico e preciso. Trilhos flutuantes deslizam no ar, pontes se retraem e reaparecem, correntes se esticam em ângulos impossíveis. A torre agora é um relógio, e você está dentro dele. O som não é mais digital — é físico: estalos de ferro, o rugido distante de vapor escapando, e o baque ritmado de algo — ou alguém — se aproximando. Uma luz vermelha pulsa no fundo das engrenagens. ')
    jogo1.digitar(texto9)
    
    print('\n[bold purple][Sistema]Andar 12 — Núcleo da Inércia detectado.][/bold purple]')
    print('[bold purple][Sistema]Habilidade: Senso do dominador ativada: Status do usuário bloqueado temporariamente.[/bold purple]')
    print('[bold purple][Sistema]Terreno instável. Gravidade variável. Risco de esmagamento crítico.[/bold purple]\n')

    texto10 = ('E então você os vê. Emergindo das laterais dos trilhos, deslizando como carruagens vivas sobre cabos de cobre, surgem os 3 Guardiões de Pulso. Eles têm forma humanoide, mas são frios e assimétricos — criaturas construídas com cobre, vidro rúnico e engrenagens pulsantes. No lugar de olhos, um único visor circular, onde um ponteiro gira freneticamente, marcando o tempo entre seus ataques. Cada movimento deles causa reverberações no solo, como se fossem extensões conscientes da própria torre. Eles não falam. Não precisam. O som metálico de seus braços girando — cada um terminando em lâminas de força rotacional — é a única advertência. Eles não querem te testar. Eles querem te arrancar deste lugar como se você fosse uma peça fora do eixo.')
    jogo1.digitar(texto10)

    while True:
        texto4 = '\n1. Iniciar combate direto.'
        jogo1.digitar(texto4)

        try:
            time.sleep(1)
            esc_3 = input("\nEscolha uma opção: ").strip()
            if esc_3 not in ("1"):
                raise ValueError("❗ Opção inválida.")
            if esc_3 == "1":
                #COMBATEEE
                lore_recompensa002(personagem)
                lore_pos_12andar(personagem)
                break
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa002(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    personagem.inventario[0].qtd += 3
    personagem.inventario[1].qtd += 3

    chance = random.random()
    if chance < 0.4:
        personagem.inventario.append(lista_itens[79])
        print('[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [480] \nPoção de cura [1]\nPoção de mana [1]\nItem: 📜 Fragmento de Lore — "Compasso da Máquina: Registro dos Guardiões de Pulso"[/bold purple]')
        text_inf = ('\nPressione ENTER para prosseguir...')
        jogo1.digitar(text_inf)
        input('')
    else:
        print("[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [480] \nPoção de cura [1]\nPoção de mana [1][/bold purple]")
        text_inf = ('\nPressione ENTER para prosseguir...')
        jogo1.digitar(text_inf)
        input('')

def lore_pos_12andar(personagem):
    texto11 = ('Com um estrondo final, o último Guardião de Pulso colapsa sobre si mesmo. Suas engrenagens se partem em ângulos impossíveis, como se o tempo interno que o guiava tivesse finalmente parado. As luzes vermelhas de seus visores se apagam... uma por uma. Mas a torre não silencia. Ao contrário, agora ela desacelera. As engrenagens colossais que giravam ao seu redor começam a parar, como um coração mecânico que enfim se rendeu à exaustão. Trilhos estagnam no ar, plataformas param de girar, e a gravidade — pela primeira vez neste andar — estabiliza-se. Você respira, mesmo que o ar seja só um código simulando oxigênio.')
    jogo1.digitar(texto11)

    print('\n[bold purple][Sistema]Unidade sobrevivente. Ritmo da inércia neutralizado.][/bold purple]')
    print('[bold purple][Sistema]Integração espacial do jogador reforçada. Resistência corporal aumentada temporariamente.[/bold purple]')
    print('[bold purple][Sistema]Status desbloqueado.[/bold purple]\n')

    texto12 = ('No centro da arena, onde antes uma engrenagem girava sem fim, surge uma luz vertical azul. Um feixe que escaneia seu corpo inteiro antes de projetar uma nova plataforma de elevação. No chão, um pequeno fragmento em forma de ponteiro de relógio permanece. Ao tocá-lo, você escuta uma frase repetida como uma falha no tempo')
    jogo1.digitar(texto12)

    print('\n[bold blue][italic]“Aqueles que param o movimento... veem além do instante.”[/italic][/bold blue]')
    print('[bold blue][italic]"Você foi mais rápido do que o tempo."[/italic][/bold blue]')
    print('[bold blue]"Mais forte que a força."[italic][/italic][/bold blue]')
    print('[bold blue][italic]"E mais equilibrado que o próprio espaço."[/italic][/bold blue]')
    print('[bold blue][italic]"Mas Etherion não para"[/italic][/bold blue]')
    print('[bold blue][italic]"Ela apenas te dá tempo o suficiente... para respirar antes do próximo colapso."[/italic][/bold blue]')

    while True:
        texto4 = '\n1. Avançar para o próximo andar.\n2. Investigar 12° andar \n3. Investigar inventário\n4. Conferir Atributos'
        jogo1.digitar(texto4)

        try:
            time.sleep(1)
            esc_1 = input("\nEscolha uma opção: ").strip()
            if esc_1 not in ("1","2","3","4"):
                raise ValueError("❗ Opção inválida.")
            if esc_1 == "1":
                #lore_13_andar(personagem)
                break
            elif esc_1 == "2":
                chance = random.random()
                if chance < 0.4:
                    personagem.inventario.append(lista_itens[79])

            elif esc_1 == "3":
                inventario.interface_inv(personagem)
            elif esc_1 == "4":
                #ATRIBUTOSSSS
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")



