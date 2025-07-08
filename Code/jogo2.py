import time
from ficha import Personagem
import sys
import os
from rich import print
from item import lista_itens
import inventario
import jogo1
import random

def lore_pos_5andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    texto1 = ('O corpo híbrido de Kairon, se contorce uma última vez antes de desintegrar em fragmentos de energia e dados flutuantes. Sua essência se despede em um último rugido metálico que ecoa até o vazio. A arena silenciosa parece respirar aliviada — ou talvez colapsar. As plataformas ao redor tremem, como se o próprio labirinto reconhecesse sua vitória. Do centro do campo de batalha, uma fenda vertical de luz pura se abre, revelando um corredor estreito e pulsante, revestido de códigos vivos em espirais azuladas. Você cambaleia, exausto, com sua ficha digital ainda em alerta vermelho. O silêncio agora é pesado, não mais opressor, mas carregado de significado. Você derrotou um guardião, um pilar da estrutura de Etherion… e há consequências por isso.')

    jogo1.digitar(texto1)

    print('[bold purple][Sistema]Boss eliminado com sucesso. Integridade do Andar 5 comprometida. Protocolo de restauração iniciado.\n[Sistema] Sua persistência é estatisticamente improvável… e perigosamente inspiradora.[/bold purple]')

    while True:
        try:
            time.sleep(1)
            texto2 = ("\nVocê pode:\n\n1. Avançar para o Andar 6\n2. Investigar inventário\n3. Conferir Atributos")
            jogo1.digitar(texto2)
            time.sleep(1)
            print('\n[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_1 = input('')

            if esc_1 not in ("1", "2", "3"):
                raise ValueError("❗ Opção inválida.")
            if esc_1 == "1":
                lore_6_andar(personagem)
                print()
                break
            elif esc_1 == "2":
                inventario.interface_inv(personagem)
            elif esc_1 == "3":
                #Atributos
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_6_andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')

    texto2 = ('Ao atravessar o portal pulsante que surge após a queda de Kairon, tudo ao seu redor é engolido por uma luz branca e densa. Não há som. Não há vento. Apenas a sensação de que você está sendo puxado para dentro de uma estrutura adormecida... mas viva. Você desperta em uma estação colossal suspensa no vazio, aparentemente abandonada, como se tivesse sido esquecida por eras. Cabos se estendem como artérias ao longo das paredes curvas. O chão metálico vibra sutilmente, como se a própria estrutura tivesse um pulso. Aqui, não há música, não há zumbido — o silêncio é absoluto, e ele pesa sobre você como uma armadura invisível. As luzes que percorrem os trilhos do teto piscam em padrões ritmados — verdes, azuis e vermelhos — lembrando batimentos cardíacos artificiais. Há terminais quebrados, telas que piscam entre estática e dados corrompidos, dutos de ventilação respirando lentamente como se fossem narinas metálicas. Você tem a sensação constante de estar sendo observado, mas nada se move.')
    jogo1.digitar(texto2)
    time.sleep(1)
    print('\n[bold]Até que se move[/bold]\n')

    texto3 = ('De trás de uma parede rebaixada, três figuras surgem, sem emitir um único som. Seus corpos são altos, finos e compostos por ligas pretas com circuitos vermelhos, olhos sem brilho e rostos lisos — como bonecos de vigilância esquecidos. Mas você sente: eles escutam sua presença não com ouvidos, mas com sensores que captam suas intenções. Eles são as Sentinelas Silenciadas — inteligências artificiais esquecidas pelo sistema, programadas para manter o silêncio da estação. Qualquer ruído, vibração ou sinal emocional captado pode ativá-las. Não são inimigos que você pode simplesmente atrair e bater: o perigo está em ser notado.')
    jogo1.digitar(texto3)

    print('\n[bold purple][Sistema]Protocolo Ativo — Área de Atenção Sonora. \nMovimentação brusca ou emissão de som digital ativará contra medidas defensivas autônomas. \nRecomenda-se: discrição, inteligência e controle emocional.[/bold purple]\n')

    while True:
        try:
            time.sleep(1)
            texto4 = ("\nVocê pode:\n\n1. Iniciar combate 6\n2. Tentar se esgueirar pelas sombras (requer furtividade) — Uma tentativa tática, silenciosa. Se bem-sucedida, você evita o combate direto e pode alcançar um terminal que desativa as sentinelas.)")
            jogo1.digitar(texto4)
            time.sleep(1)

            print('\n[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_1 = input('')

            if esc_1 not in ("1", "2"):
                raise ValueError("❗ Opção inválida.")
            if esc_1 == "1":
                #COMBATEEEEEEEEEEEE
                print()
                break
            elif esc_1 == "2":
                if personagem.atributos['furtividade'] >= 20:
                    texto5 = ('Sucesso total. Você se move como um fragmento apagado entre os dados, confundindo os sensores das sentinelas. Você alcança um terminal auxiliar e pode desativar 1 inimigo imediatamente ou iniciar o combate com vantagem.')
                    jogo1.digitar(texto5)

                    print('[bold purple][Sistema]Ruído ignorado. Presença não detectada. Parâmetro mantido[/bold purple]')

                    texto6 = ('Ao enganar as sentinelas, a estação inteira parece “desligar”. Um silêncio novo surge — não mais pesado, mas libertador. As luzes mudam para um tom azul suave. Um dos painéis centrais se ergue, revelando uma espiral de escadas virtuais em queda livre.')
                    jogo1.digitar(texto6)
                    time.sleep(2.5)
                    lore_recompensa001(personagem)
                    lore_pos_6andar(personagem)

                elif personagem.atributos['furtividade'] < 20:
                    texto6 = ('Falha crítica. Um leve som de sua movimentação ecoa pela estação — o suficiente. As três sentinelas giram as cabeças na sua direção instantaneamente.')
                    jogo1.digitar(texto6)

                    print('[bold purple][Sistema]Presença confirmada. Silêncio violado. Protocolo de punição iniciado.[/bold purple]')

                    texto7 = ('Você recebe dano crítico inicial e as sentinelas iniciam o combate em modo agressivo.')
                    jogo1.digitar(texto7)

                    #COMBATEEEEEEEEEEEEEEEEEEEEE

                    #DEPOIS DO COMBATE TEM COITO😈😈😈😈😈😈
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa001(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [300] \nPoção de cura [2]\nPoção de mana [2][/bold purple]")
    text_inf = ('\nItens sendo computados...')
    jogo1.digitar(text_inf)

    personagem.inventario[0].qtd = 2
    personagem.inventario[1].qtd = 2

    time.sleep(8)

def lore_pos_6andar(personagem):
    print('[bold purple][Sistema]Protocolo de silêncio restaurado. Fluxo de dados liberado. Acesso ao Andar 7 desbloqueado. [Sistema]Recomenda-se verificar estado do inventário antes de prosseguir.[/bold purple]')

    while True:
        try:
            time.sleep(1)
            texto8 = ("\nVocê pode:\n\n1. Avançar para o Andar 7\n2. Investigar inventário\n3. Conferir Atributos\n4. Examinar os terminais inativos da estação em busca de dados perdidos. (Pode render informação da lore ou um item raro.)")
            jogo1.digitar(texto8)
            time.sleep(1)
            print('\n[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_2 = input('')

            if esc_2 not in ("1", "2", "3","4"):
                raise ValueError("❗ Opção inválida.")
            if esc_2 == "1":
                lore_7_andar(personagem)
                print()
                break
            elif esc_2 == "2":
                inventario.interface_inv(personagem)
            elif esc_2 == "3":
                #Atributos
                print()
            elif esc_2 == "4":
                if personagem.atributos['maos rapidas'] > 20:
                    texto9 = ('Você decide vasculhar a estação em busca de recursos escondidos entre cabos, painéis e restos de unidades antigas.')
                    jogo1.digitar(texto9)
                    #ADICIONAR A KACETA DO ITEM NO INVENTARIO
                    print('\n[bold purple][Sistema]Você encontrou um Fragmento de Dados Recuperados[/bold purple]\n')
                else:
                    texto9 = ('Você decide vasculhar a estação em busca de recursos escondidos entre cabos, painéis e restos de unidades antigas.')
                    jogo1.digitar(texto9)

                    print('\n[bold purple][Sistema]Nada foi encontrado...[/bold purple]\n')

        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_7_andar(personagem):
    texto10 = ('Ao deixar para trás o silêncio opressor da Estação, você atravessa o portal e é recebido por um cenário que desafia toda lógica e expectativa. À sua frente, um vasto jardim digital se estende até onde a vista alcança — mas não há vida aqui. As plantas, feitas de vetores geométricos cinzentos, estão imóveis e estéreis, como esculturas abandonadas pelo tempo. O ar é pesado com o cheiro metálico da corrosão digital, e partículas de dados flutuam lentamente, como folhas mortas em um outono eterno. O chão é um mosaico quebrado de chips e fragmentos de sistemas caídos. A sensação é de que este lugar foi um dia vibrante, mas sofreu uma falha irreversível. No centro do jardim, uma figura surge lentamente: a Flor - Código Cadavérica. Essa entidade parece imóvel à primeira vista, mas seus olhos escarlates brilham com uma inteligência fria e predatória. Ela não se move, mas com um simples pensamento, manipula os dados ao redor para criar armadilhas mentais e ataques de confusão.')

    jogo1.digitar(texto10)

    print('\n[bold purple][Sistema]Atenção — Entidade de controle mental detectada. Cuidado com ilusões e manipulações do ambiente.[bold purple]\n')
    
    while True:
        try:
            time.sleep(1)
            texto11 = ("\nVocê pode:\n\n1. Efetuar um ataque direto utilizando toda sua força no primeiro ataque com risco de levar uma sequência de dano que consuma boa parte da sua vida, mas que possui 20% de chances de cortar o caule binário do inimigo levando-o a morte.\n2. Iniciar combate direto")
            jogo1.digitar(texto11)
            time.sleep(1)
            print('\n[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_1 = input('')

            if esc_1 not in ("1", "2"):
                raise ValueError("❗ Opção inválida.")
            if esc_1 == "1":
                chance = random.random()
                if chance < 0.2:
                    texto12 = ('No instante em que sua lâmina rasgou o ar com a fúria de mil sóis, um brilho intenso irrompeu. Não era apenas a força bruta, mas a precisão de um mestre, aliada a uma sorte improvável, que guiou seu ataque. O metal encontrou o ponto mais vulnerável do inimigo: o caule binário, a essência pulsante de sua existência digital, onde a vida e o código se entrelaçavam em uma dança caótica')
                    jogo1.digitar(texto12)

                    print('[bold purple]Inimigo derrotado sem chances de reagir. 8° Andar liberado.[/bold purple]')

                    time.sleep(3)

                    lore_pos_7andar(personagem)

                else:
                    #VANTAGEM PRO INIMIGO
                    #COMBATEEEEEEEEEEEEEEEE
                    print()
            elif esc_1 == "2":
                #COMBATEEEEEEEEEEEEEEEE
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa002(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    item_escolhido001 = ''

    personagem.inventario[0].qtd = 2
    personagem.inventario[1].qtd = 2

'''AJEITAR ESSE BASCUIO
    if personagem.raca == 'elfo':
        while True:
            try:
                texto6 = ("\nQual destes 3 itens você deseja levar consigo? \n 👖[1] Calças frouxas do Andarilho verde: Calças leves e maleáveis feitas de tecido encantado com fios vegetais antigos. Ajudam o elfo a se mover como o vento entre as folhas, mas exigem foco constante por que ficam querendo cair toda hora, diminuindo o respeito que o personagem passa. (+1 resistência) (+1 furtividade) (-2 diplomacia)\n 📖[2] Livro Mofado de Poções: Livro esquecido coberto de musgo e cheiro de terra molhada. Amplifica o poder das poções de cura, mas seu dono se perde nos detalhes alquímicos, dificultando perceber o ambiente ao redor. (poções de cura melhoradas)\n 🧤[3] Luvas Élficas surradas: leves e confortáveis, oferecem vantagem em tarefas delicadas. (+1 mãos rápidas) ")
                jogo1.digitar(texto6)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa001 = input().strip()

                if recompensa001 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa001 == "1":
                    personagem.inventario.append(lista_itens[2])
                    item_escolhido001 = '🏹 Arco Simples'
                    print()

                elif recompensa001 == "2":
                    personagem.inventario.append(lista_itens[3])
                    item_escolhido001 = '🍃 Broche da Folha'
                    print()
                elif recompensa001 == "3":  
                    personagem.inventario.append(lista_itens[4])
                    item_escolhido001 = '🧤 Luvas Élficas surradas'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")
    
    elif personagem.raca == 'humano':
        while True:
            try:
                texto6 = ("\nQual destes 3 itens você deseja levar consigo? \n ⚔️[1] Espada de combate simples: confiável e robusta, a clássica espada de aventureiro iniciante. (+1 mano a mano)\n 🍀[2] Medalhão da Sorte: um amuleto simples que ajuda a encontrar respostas por pura sorte. (+1 percepção)\n 🧤[3] Botas de Couro: melhora a armadura e a resistência a terrenos difíceis (lama, neve, areia) fora de combate. (+1 resistência)")
                jogo1.digitar(texto6)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa001 = input().strip()

                if recompensa001 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa001 == "1":
                    personagem.inventario.append(lista_itens[5])
                    item_escolhido001 = '⚔️ Espada de combate simples'
                    print()

                elif recompensa001 == "2":
                    personagem.inventario.append(lista_itens[6])
                    item_escolhido001 = '🍀 Medalhão da Sorte'
                    print()
                elif recompensa001 == "3":
                    personagem.inventario.append(lista_itens[7])
                    item_escolhido001 = '🧤 Botas de Couro'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")

    elif personagem.raca == 'draconiano':
        while True:
            try:
                texto6 = ("\nQual destes 3 itens você deseja levar consigo? \n 🗡️[1] Adaga de Escamas: pequena adaga com símbolos dracônicos entalhados, item comum entre guerreiros draconianos inexperientes. (+1 mano a mano)\n 🧿[2] Talismã do caçador: alimenta o instinto de caça dos draconianos, os deixando mais ágeis. (+1 acrobacia)\n 🪨[3] Colar quebrado de Pedra Dracônica: pequeno pingente com uma pedra rachada da cor do dragão ancestral do personagem; Acalma o coração dos draconianos e os deixam mais sociáveis. (+1 diplomacia)")
                jogo1.digitar(texto6)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa001 = input().strip()

                if recompensa001 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa001 == "1":
                    personagem.inventario.append(lista_itens[8])
                    item_escolhido001 = '🗡️ Adaga de Escamas'
                    print()

                elif recompensa001 == "2":
                    personagem.inventario.append(lista_itens[9])
                    item_escolhido001 = '🧿 Talismã do caçador'
                    print()
                elif recompensa001 == "3":
                    personagem.inventario.append(lista_itens[10])
                    item_escolhido001 = '🪨 Colar quebrado de Pedra Dracônica'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")
    
    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [225] \nPoção de cura [1]\nPoção de mana [1]\nItens: 📒 Livro de perícias, {item_escolhido001}[/bold purple]")
    text_inf = ('\nItens sendo computados...')
    jogo1.digitar(text_inf)
    time.sleep(8)

def lore_pos_7andar(personagem):
    print()'''





