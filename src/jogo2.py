import random
import time

from InquirerPy import inquirer
from rich import print

import inventario
import jogo1
import jogo3
from combate import combate
from inimigos import lista_inimigos
from item import lista_itens
from utills import digitar, limpar_tela


def lore_pos_5andar(personagem):
    limpar_tela()
    texto1 = ('O corpo híbrido de Kairon, se contorce uma última vez antes de desintegrar em fragmentos de energia e dados flutuantes. Sua essência se despede em um último rugido metálico que ecoa até o vazio. A arena silenciosa parece respirar aliviada — ou talvez colapsar. As plataformas ao redor tremem, como se o próprio labirinto reconhecesse sua vitória. Do centro do campo de batalha, uma fenda vertical de luz pura se abre, revelando um corredor estreito e pulsante, revestido de códigos vivos em espirais azuladas. Você cambaleia, exausto, com sua ficha digital ainda em alerta vermelho. O silêncio agora é pesado, não mais opressor, mas carregado de significado. Você derrotou um guardião, um pilar da estrutura de Etherion… e há consequências por isso.')

    digitar(texto1)

    print('[bold purple][Sistema]Boss eliminado com sucesso. Integridade do Andar 5 comprometida. Protocolo de restauração iniciado.\n[Sistema] Sua persistência é estatisticamente improvável… e perigosamente inspiradora.[/bold purple]')

    while True:
        opcao = inquirer.select(
            message="O que deseja fazer?\n",
            choices=[
                "⬆️ Avançar para o Andar 6",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem"
            ]
        ).execute()

        if opcao == "⬆️ Avançar para o Andar 6":
            lore_6_andar(personagem)
            break
        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)
        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")

def lore_6_andar(personagem):
    limpar_tela()

    texto2 = ('Ao atravessar o portal pulsante que surge após a queda de Kairon, tudo ao seu redor é engolido por uma luz branca e densa. Não há som. Não há vento. Apenas a sensação de que você está sendo puxado para dentro de uma estrutura adormecida... mas viva. Você desperta em uma estação colossal suspensa no vazio, aparentemente abandonada, como se tivesse sido esquecida por eras. Cabos se estendem como artérias ao longo das paredes curvas. O chão metálico vibra sutilmente, como se a própria estrutura tivesse um pulso. Aqui, não há música, não há zumbido — o silêncio é absoluto, e ele pesa sobre você como uma armadura invisível. As luzes que percorrem os trilhos do teto piscam em padrões ritmados — verdes, azuis e vermelhos — lembrando batimentos cardíacos artificiais. Há terminais quebrados, telas que piscam entre estática e dados corrompidos, dutos de ventilação respirando lentamente como se fossem narinas metálicas. Você tem a sensação constante de estar sendo observado, mas nada se move.')
    digitar(texto2)
    time.sleep(1)
    print('\n[bold purple]Até que se move[/bold purple]\n')

    texto3 = ('De trás de uma parede rebaixada, três figuras surgem, sem emitir um único som. Seus corpos são altos, finos e compostos por ligas pretas com circuitos vermelhos, olhos sem brilho e rostos lisos — como bonecos de vigilância esquecidos. Mas você sente: eles escutam sua presença não com ouvidos, mas com sensores que captam suas intenções. Eles são as Sentinelas Silenciadas — inteligências artificiais esquecidas pelo sistema, programadas para manter o silêncio da estação. Qualquer ruído, vibração ou sinal emocional captado pode ativá-las. Não são inimigos que você pode simplesmente atrair e bater: o perigo está em ser notado.')
    digitar(texto3)

    print('\n[bold purple][Sistema]Protocolo Ativo — Área de Atenção Sonora. \nMovimentação brusca ou emissão de som digital ativará contra medidas defensivas autônomas. \nRecomenda-se: discrição, inteligência e controle emocional.[/bold purple]\n')

    while True:
        opcao = inquirer.select(
            message="Como deseja proceder?\n",
            choices=[
                "⚔️ Iniciar combate direto",
                "👣 Tentar se esgueirar pelas sombras (requer furtividade)",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem"
            ]
        ).execute()

        if opcao == "⚔️ Iniciar combate direto":
            vencedor = combate(personagem, lista_inimigos[4]) 
            if vencedor == personagem:
                lore_recompensa001(personagem)
                lore_pos_6andar(personagem)
                break

        elif opcao == "👣 Tentar se esgueirar pelas sombras (requer furtividade)":
            if personagem.pericias.get('furtividade', 0) >= 20:
                digitar("Você se move silenciosamente entre os cabos...")
                lore_recompensa001(personagem)
                lore_pos_6andar(personagem)
                break
            else:
                digitar("Um ruído leve alerta as sentinelas. Combate é iniciado com desvantagem.")
                vencedor = combate(personagem, lista_inimigos[4]) 
                if vencedor == personagem:
                    lore_recompensa001(personagem)
                    lore_pos_6andar(personagem)
                    break

        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)

        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")


def lore_recompensa001(personagem):
    limpar_tela()
    print("[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [300] \nPoção de cura [2]\nPoção de mana [2][/bold purple]")
    digitar('\nPressione ENTER para prosseguir...')
    input()
    personagem.inventario[0].qtd = 2
    personagem.inventario[1].qtd = 2

def lore_pos_6andar(personagem):
    limpar_tela()


    print('[bold purple][Sistema]Protocolo de silêncio restaurado. Fluxo de dados liberado. Acesso ao Andar 7 desbloqueado. [Sistema]Recomenda-se verificar estado do inventário antes de prosseguir.[/bold purple]')
    explorado = False
    while True:
        opcao = inquirer.select(
            message="O que deseja fazer?\n",
            choices=[
                "⬆️ Avançar para o Andar 7",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem",
                "📂 Examinar terminais em busca de dados (Requer mãos rápidas)"
            ]
        ).execute()

        if opcao == "⬆️ Avançar para o Andar 7":
            lore_7_andar(personagem)
            break

        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)

        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")

        elif opcao == "📂 Examinar terminais em busca de dados (Requer mãos rápidas)":
            if not explorado:
                explorado = True
                if personagem.pericias.get('maos rapidas', 0) >= 20:
                    digitar("Você encontra um Fragmento de Dados Recuperados.")
                    personagem.inventario.append(lista_itens[81])
                else:
                    digitar("Você revira os cabos... mas nada é encontrado.")
                input("\nPressione ENTER para continuar...")
            else:
                print('[bold purple][Sistema] Você já explorou este andar.[/bold purple]')


def lore_7_andar(personagem):
    limpar_tela()

    texto10 = ('Ao deixar para trás o silêncio opressor da Estação, você atravessa o portal e é recebido por um cenário que desafia toda lógica e expectativa. À sua frente, um vasto jardim digital se estende até onde a vista alcança — mas não há vida aqui. As plantas, feitas de vetores geométricos cinzentos, estão imóveis e estéreis, como esculturas abandonadas pelo tempo. O ar é pesado com o cheiro metálico da corrosão digital, e partículas de dados flutuam lentamente, como folhas mortas em um outono eterno. O chão é um mosaico quebrado de chips e fragmentos de sistemas caídos. A sensação é de que este lugar foi um dia vibrante, mas sofreu uma falha irreversível. No centro do jardim, uma figura surge lentamente: a Flor - Código Cadavérica. Essa entidade parece imóvel à primeira vista, mas seus olhos escarlates brilham com uma inteligência fria e predatória. Ela não se move, mas com um simples pensamento, manipula os dados ao redor para criar armadilhas mentais e ataques de confusão.')

    digitar(texto10)

    print('\n[bold purple][Sistema]Atenção — Entidade de controle mental detectada. Cuidado com ilusões e manipulações do ambiente.[/bold purple]\n')
    
    while True:
        opcao = inquirer.select(
            message="Como deseja proceder?\n",
            choices=[
                "💥 Efetuar um ataque direto utilizando toda sua força no primeiro ataque com risco de levar uma sequência de dano que consuma boa parte da sua vida, mas que possui 20% de chances de cortar o caule binário do inimigo levando-o a morte.",
                "⚔️ Iniciar combate direto",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem"
            ]
        ).execute()

        if opcao == "💥 Efetuar um ataque direto utilizando toda sua força no primeiro ataque com risco de levar uma sequência de dano que consuma boa parte da sua vida, mas que possui 20% de chances de cortar o caule binário do inimigo levando-o a morte.":
            chance = random.random()
            if chance < 0.2:
                texto12 = ('No instante em que sua lâmina rasgou o ar com a fúria de mil sóis, um brilho intenso irrompeu. Não era apenas a força bruta, mas a precisão de um mestre, aliada a uma sorte improvável, que guiou seu ataque. O metal encontrou o ponto mais vulnerável do inimigo: o caule binário, a essência pulsante de sua existência digital, onde a vida e o código se entrelaçavam em uma dança caótica')
                jogo1.digitar(texto12)

                print('[bold purple]Inimigo derrotado sem chances de reagir. 8° Andar liberado.[/bold purple]')

                time.sleep(3)
                lore_recompensa002(personagem)
                lore_pos_7andar(personagem)

            else:
                #VANTAGEM PRO INIMIGO
                vencedor = combate(personagem, lista_inimigos[5]) 
                if vencedor == personagem:
                    lore_recompensa002(personagem)
                    lore_pos_7andar(personagem)

        elif opcao == "⚔️ Iniciar combate direto":
            vencedor = combate(personagem, lista_inimigos[4]) 
            if vencedor == personagem:
                lore_recompensa002(personagem)
                lore_pos_7andar(personagem)
                break
            print()

        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)

        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")

def lore_recompensa002(personagem):
    limpar_tela()
    item_escolhido001 = ''

    personagem.inventario[0].qtd = 2
    personagem.inventario[1].qtd = 2

    if personagem.raca == 'elfo':
        while True:
            print()
            opcao = inquirer.select(
            message="Qual destes 3 itens você deseja levar consigo?\n",
            choices=[
                "👖 Calças frouxas do Andarilho verde: Calças leves e maleáveis feitas de tecido encantado com fios vegetais antigos. Ajudam o elfo a se mover como o vento entre as folhas, mas exigem foco constante por que ficam querendo cair toda hora, diminuindo o respeito que o personagem passa. (+2 resistência),(+2 furtividade),(-2 diplomacia)",
                "🪭 Elmo da Dança das Sombras: Um elmo leve adornado com penas negras que amplifica a agilidade e destreza do portador em combates corpo a corpo, facilitando movimentos acrobáticos e ataques rápidos. Porém, o barulho causado pelas penas ao se mover pode comprometer a furtividade. (+2 mano a mano), (+2 acrobacia), (-2 furtividade)",
                "🌻 Broche de Girassol: Um broche mágico com um girassol encantado que nunca murcha. Irradia calor e simpatia, facilitando interações sociais, mas torna o portador mais vulnerável a mentiras. (+2 diplomacia)"
            ]
            ).execute()

            if opcao == "👖 Calças frouxas do Andarilho verde: Calças leves e maleáveis feitas de tecido encantado com fios vegetais antigos. Ajudam o elfo a se mover como o vento entre as folhas, mas exigem foco constante por que ficam querendo cair toda hora, diminuindo o respeito que o personagem passa. (+2 resistência),(+2 furtividade),(-2 diplomacia)":

                personagem.inventario.append(lista_itens[28])
                item_escolhido001 = '👖 Calças frouxas do Andarilho verde'
                print()

            elif opcao == "🪭 Elmo da Dança das Sombras: Um elmo leve adornado com penas negras que amplifica a agilidade e destreza do portador em combates corpo a corpo, facilitando movimentos acrobáticos e ataques rápidos. Porém, o barulho causado pelas penas ao se mover pode comprometer a furtividade. (+2 mano a mano), (+2 acrobacia), (-2 furtividade)":
                personagem.inventario.append(lista_itens[83])
                item_escolhido001 = '🪭 Elmo da Dança das Sombras'
                print()

            elif opcao == "🌻 Broche de Girassol: Um broche mágico com um girassol encantado que nunca murcha. Irradia calor e simpatia, facilitando interações sociais, mas torna o portador mais vulnerável a mentiras. (+2 diplomacia)":
                personagem.inventario.append(lista_itens[30])
                item_escolhido001 = '🌻 Broche de Girassol'
                print()
            break
    
    elif personagem.raca == 'humano':
        while True:
            print()
            opcao = inquirer.select(
            message="Qual destes 3 itens você deseja levar consigo?\n",
            choices=[
                "⚔️ Espada de Cavaleiro Antigo: Espada rústica mas confiável, forjada para os cavaleiros que protegiam antigos reis da região. Melhora o combate corpo a corpo. (+2 mano a mano)",
                "🛡️ Escudo de Madeira Reforçado: Escudo resistente, feito das árvores ancestrais do jardim. Dá defesa extra e estabilidade, mas seu peso dificulta movimentos rápidos. (+2 resistência)",
                "🪶 Pena de Corvo Solar: Rara pena negra com brilho dourado nas pontas. Dizem que quem a carrega ganha olhos atentos e mãos ágeis. (+2 mãos rápidas)"
            ]
            ).execute()

            if opcao == "⚔️ Espada de Cavaleiro Antigo: Espada rústica mas confiável, forjada para os cavaleiros que protegiam antigos reis da região. Melhora o combate corpo a corpo. (+2 mano a mano)":

                personagem.inventario.append(lista_itens[31])
                item_escolhido001 = '⚔️ Espada de Cavaleiro Antigo'
                print()

            elif opcao == "🛡️ Escudo de Madeira Reforçado: Escudo resistente, feito das árvores ancestrais do jardim. Dá defesa extra e estabilidade, mas seu peso dificulta movimentos rápidos. (+2 resistência)":
                personagem.inventario.append(lista_itens[41])
                item_escolhido001 = '🛡️ Escudo de Madeira Reforçado'
                print()

            elif opcao == "🪶 Pena de Corvo Solar: Rara pena negra com brilho dourado nas pontas. Dizem que quem a carrega ganha olhos atentos e mãos ágeis. (+2 mãos rápidas)":
                personagem.inventario.append(lista_itens[33])
                item_escolhido001 = '🪶 Pena de Corvo Solar'
                print()
            break

    elif personagem.raca == 'draconiano':
        while True:
            print()
            opcao = inquirer.select(
            message="Qual destes 3 itens você deseja levar consigo?\n",
            choices=[
                "🐲 Escama de Dragão Ancião: Fragmento ancestral endurecido de um grande dragão. Reforça a defesa do portador (+2 resistência)",
                "💍 Anel do Patriarca: Símbolo da linhagem draconiana. Melhora a presença social, mas sua energia imponente facilita negociações. (+2 diplomacia)",
                "🔨 Maça de Escamas: Maça pesada revestida com escamas negras, símbolo de brutalidade e poder. Aumenta o dano físico e a resistência, mas deixa o portador menos ágil. (+2 mano a mano)"
            ]
            ).execute()

            if opcao == "🐲 Escama de Dragão Ancião: Fragmento ancestral endurecido de um grande dragão. Reforça a defesa do portador (+2 resistência)":

                personagem.inventario.append(lista_itens[8])
                item_escolhido001 = '🐲 Escama de Dragão Ancião'
                print()

            elif opcao == "💍 Anel do Patriarca: Símbolo da linhagem draconiana. Melhora a presença social, mas sua energia imponente facilita negociações. (+2 diplomacia)":
                personagem.inventario.append(lista_itens[9])
                item_escolhido001 = '💍 Anel do Patriarca'
                print()

            elif opcao == "🔨 Maça de Escamas: Maça pesada revestida com escamas negras, símbolo de brutalidade e poder. Aumenta o dano físico e a resistência, mas deixa o portador menos ágil. (+2 mano a mano)":
                personagem.inventario.append(lista_itens[10])
                item_escolhido001 = '🔨 Maça de Escamas'
                print()
            break
    
    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [320] \nPoção de cura [2]\nPoção de mana [2]\nItem: {item_escolhido001}[/bold purple]")
    text_inf = ('\nPressione ENTER para prosseguir...')
    digitar(text_inf)
    input('')

def lore_pos_7andar(personagem):
    limpar_tela()

    texto14 = ('Ao derrotar a Flor-Código Cadavérica o portal para o próximo andar é revelado.')
    digitar(texto14)
    while True:
        opcao = inquirer.select(
            message="O que deseja fazer?\n",
            choices=[
                "⬆️ Avançar para o Andar 8",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem"
            ]
        ).execute()

        if opcao == "⬆️ Avançar para o Andar 8":
            lore_8_andar(personagem)
            break
        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)
        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")

def lore_8_andar(personagem):
    limpar_tela()

    texto16 = ('Ao atravessar o portal, você entra em uma imensa cúpula de cristal virtual que lembra a anterior, mas aqui a atmosfera é ainda mais densa, quase palpável. As paredes são cobertas por circuitos interligados, que brilham em uma sequência hipnótica, emitindo um zumbido persistente que parece ressoar diretamente em sua mente. O ar vibra com uma energia que desgasta lentamente a concentração e a força mental. Fragmentos de códigos, símbolos e padrões complexos giram ao seu redor, formando ilusões que testam não apenas sua inteligência, mas sua capacidade de manter a mente firme diante do desgaste contínuo. No centro da cúpula, um pedestal exibe um orbe pulsante, o núcleo do desafio. Você deve ser capaz de resistir a uma série de ataques mentais intensos e enigmas que pressionam sua mente, forçando-o a usar sua Perícia de Resistência para manter o foco e não sucumbir à exaustão psíquica. Conforme o jogador pisa no coração da cúpula, os circuitos ao redor começam a emitir ondas mentais pulsantes. A luz se intensifica até tudo se tornar branco por um momento. Quando a visão volta, o cenário está parado. Só resta o jogador... e uma única pergunta projetada no ar diante dele.')
    jogo1.digitar(texto16)

    time.sleep(1)
    print('\n[bold blue]"O quanto você sabe sobre tudo? Quer testar seus conhecimentos?"[/italic][/bold blue]\n')

    texto17 = ('A pergunta se forma dentro da mente do jogador — como se a torre estivesse escavando memórias para confundir e desestabilizar. Falhar na resistência a esse teste poderá causa uma perda irrecuperável da sua consciência...')
    jogo1.digitar(texto17)

    while True:
        opcao = inquirer.select(
            message="O que deseja fazer?\n",
            choices=[
                "🧠 Enfrentar diretamente o desafio mental.",
                "⬆️ Ignorar todo o andar e ir direto para o próximo.",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem"
            ]
        ).execute()

        if opcao == "🧠 Enfrentar diretamente o desafio mental.":
            lore_2_enigma(personagem)
            print()
            break
        
        elif opcao == "⬆️ Ignorar todo o andar e ir direto para o próximo.":
            lore_pos_8andar(personagem)
            break
        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)
        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")

def lore_2_enigma(personagem):
    #SE ERRAR PERDE 20% DE PONTOS NO ATRIBUTO DE PERCEPÇÃO
    if personagem.andar_cupula_completado:
        time.sleep(1)
        limpar_tela()

        print("\n[bold purple]⚠️ O Andar da cúpula foi destruído por corrompimento dimensional. Você avança direto para o próximo andar...[/bold purple]\n")
        lore_pos_8andar(personagem)
        return
    else:
        print('[bold purple][Sistema]Iniciando teste de resiliência cognitiva.[/bold purple]')
        time.sleep(1)
        print('[bold purple][Sistema]A mente do Eco será testada não por força, mas pela integridade de suas lembranças.[/bold purple]')
        time.sleep(1)

        if personagem.atributos['resistencia'] >= 25:
            while True:
                opcao = inquirer.select(
                    message='[bold purple][italic]"O que foi a Queda do Éter?"[/italic][/bold purple]',
                    choices=[
                        "A) A ruptura de uma aliança entre as raças antigas e o sistema de proteção central.",
                        "B) O colapso entre os planos físico e digital que dissolveu a barreira entre alma e código",
                        "C) Um evento mágico que corrompeu os ecos originais da raça draconiana"
                    ]
                ).execute()
                if opcao == "A) A ruptura de uma aliança entre as raças antigas e o sistema de proteção central.":
                    morte_cupula(personagem)
                    break
                elif opcao == "B) O colapso entre os planos físico e digital que dissolveu a barreira entre alma e código":
                    lore_recompensa003(personagem)
                    break
                elif opcao == "C) Um evento mágico que corrompeu os ecos originais da raça draconiana":
                    morte_cupula(personagem)
                    break 
        
        elif 20 <= personagem.atributos['resistencia'] <25:
             while True:
                opcao = inquirer.select(
                    message='[bold purple][italic]"Por que o Eco Corrompido foi criado, segundo os registros fragmentados do sistema?"[/italic][/bold purple]',
                    choices=[
                        "A) Para impedir que Ecos coletassem fragmentos de si mesmos em andares superiores.",
                        "B) Para testar a integridade emocional dos que desejam transcender a prisão do Etherion",
                        "C) Porque era uma anomalia espontânea, resultado de dados acumulados corrompidos"
                    ]
                ).execute()
                if opcao == "A) Para impedir que Ecos coletassem fragmentos de si mesmos em andares superiores.":
                    morte_cupula(personagem)
                    break
                elif opcao == "B) Para testar a integridade emocional dos que desejam transcender a prisão do Etherion":
                    lore_recompensa003(personagem)
                    break
                elif opcao == "C) Porque era uma anomalia espontânea, resultado de dados acumulados corrompidos":
                    morte_cupula(personagem)
                    break

        
        elif personagem.atributos['resistencia'] < 20:
            while True:
                opcao = inquirer.select(
                    message='[bold purple][italic]"Qual é o verdadeiro propósito da Torre de Etherion, segundo os fragmentos mais antigos?"[/italic][/bold purple]',
                    choices=[
                        "A) Proteger as últimas memórias conscientes antes da extinção do mundo físico",
                        "B) Reciclar identidades digitais e reconstruir consciências aptas a coexistir com o novo mundo pós-Éter",
                        "C) Isolar ecos contaminados para evitar a propagação da corrupção para fora do núcleo"
                    ]
                ).execute()
                if opcao == "A) Proteger as últimas memórias conscientes antes da extinção do mundo físico":
                    morte_cupula(personagem)
                elif opcao == "B) Reciclar identidades digitais e reconstruir consciências aptas a coexistir com o novo mundo pós-Éter":
                    lore_recompensa003(personagem)
                elif opcao == "C) Isolar ecos contaminados para evitar a propagação da corrupção para fora do núcleo":
                    morte_cupula(personagem) 

def morte_cupula(personagem):
    limpar_tela()
    personagem.andar_cupula_completado = True

    texto22 = ('\nAs alternativas surgem. Mas o zumbido cresce. A resposta certa escapa, como fumaça entre os dedos. Você hesita. Escolhe...')
    jogo1.digitar(texto22)
    time.sleep(1)
    print('\n[bold purple]ERRADO[/bold purple]\n')

    texto23 = ('Imediatamente, a cúpula se fecha como uma lente queima-neurônios. Um pulso mental desaba sobre ele como uma avalanche psíquica. Seus joelhos falham. A luz se apaga. Mas não há escuridão.')
    jogo1.digitar(texto23)
    time.sleep(1)

    print('\n[bold purple]Há vazio.[/bold purple]\n')

    texto24 = ('Uma rachadura se abre dentro de sua consciência, profunda e irreversível. A percepção — o que antes lhe permitia detectar mentiras, identificar padrões, ver através das ilusões — se despedaça para sempre.')
    jogo1.digitar(texto24)

    print("\n[bold purple]🧠 Percepção reduzida permanentemente em 20% ?[/bold purple]\n")

    texto25 = ('E então, a Torre sussurra… uma última sentença.')
    jogo1.digitar(texto25)

    print("\n[bold blue][italic]“Um Eco que não compreende a essência... não pode continuar existindo.”[/italic][/bold blue]\n")

    texto26 = ('Seu corpo trava. Seus olhos dilatam. Tudo desmorona. Não com um estrondo, mas com o silêncio absoluto da desconexão. A sua alma, antes entrelaçada com o código e o passado, é rejeitada pelo sistema central.')
    jogo1.digitar(texto26)

    print(f'[bold red]🩸 {personagem.nick} MORREU [/bold red]')
    lore_6_andar(personagem)

def lore_recompensa003(personagem):
    limpar_tela()

    personagem.inventario.append(lista_itens[38])

    texto22 = ('Ao responder... uma onda de luz dourada varre a cúpula. As ilusões ao redor desaparecem como fumaça, revelando um céu estrelado artificial acima. Os circuitos brilham em verde, como se reconhecessem a lucidez do seu espírito. A torre aceita sua resposta.')
    jogo1.digitar(texto22)

    print('[bold purple][Sistema]Integridade mental: confirmada. Fragmento de sabedoria desbloqueado.[/bold purple]')

    texto23 = ('O orbe flutua até sua testa, tocando suavemente sua pele. Imagens antigas invadem sua mente: civilizações desaparecidas, ecos quebrados buscando sentido, o nascimento do próprio Etherion. O orbe flutua até sua testa, tocando suavemente sua pele. Imagens antigas invadem sua mente: civilizações desaparecidas, ecos quebrados buscando sentido, o nascimento do próprio Etherion. Você sente algo se expandir dentro de si. A mente se aclara. As ilusões do mundo se tornam mais fáceis de perceber. Você agora não apenas vê… mas compreende.')
    jogo1.digitar(texto23)

    print('[bold purple][Sistema]Novo item adquirido, 🦯Cetro da perturbação(+4 percepção)[/bold purple]')

    texto24 = ('A cúpula se abre. Um portal translúcido surge, conduzindo você ao próximo andar. Mas antes de atravessar, uma voz antiga — serena, quase orgulhosa — ecoa em sua mente:')
    jogo1.digitar(texto24)

    print('[bold blue]“Você entendeu. Não basta sobreviver à torre... é preciso compreendê-la.”[/bold blue]')
    time.sleep(1)

    print("[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [350] \nItem: Cetro da Perturbação[/bold purple]")
    text_inf = ('\nPressione ENTER para prosseguir...')
    jogo1.digitar(text_inf)
    input('')

    lore_pos_8andar(personagem)


def lore_pos_8andar(personagem):
    limpar_tela()

    explore2 = False
    while True:
        opcao = inquirer.select(
            message="O que deseja fazer?\n",
            choices=[
                "🧩 Explorar a cúpula em busca de itens.",
                "⬆️ Ignorar todo o andar e ir direto para o próximo.",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem"
            ]
        ).execute()

        if opcao == "🧩 Explorar a cúpula em busca de itens.":
            if not explore2:
                    explore2 = True
                    if personagem.atributos['maos rapidas'] >= 20:
                        personagem.inventario.append(lista_itens[82])
                        time.sleep(1)
                        print('\n[bold purple][Sistema]Você encontrou um Fragmento de Dados Recuperados[/bold purple]\n')
                    else:
                        texto26 = ('Você decide vasculhar a estação em busca de recursos escondidos entre cabos, painéis e restos de unidades antigas.')
                        jogo1.digitar(texto26)
                        print('\n[bold purple][Sistema]Nada foi encontrado...[/bold purple]\n')
            else:
                print('[bold purple][Sistema]Você já explorou este andar...[/bold purple]')
        
        elif opcao == "⬆️ Ignorar todo o andar e ir direto para o próximo.":
            lore_9_andar(personagem)
            print()
            break
        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)
        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")

def lore_9_andar(personagem):
    limpar_tela()

    texto26 = ('Ao confrontar o 8° andar e escolher seguir em frente um portal é aberto para dar continuidade a sua jornada. Entretanto... O portal que se abre diante de você não é feito de luz ou código limpo — mas de ruídos dissonantes e fragmentos instáveis, como se estivesse sendo reconstruído em tempo real por algo... corrompido. Ao atravessá-lo, a paisagem que surge é um campo irregular de dados brutos, com estruturas quebradas, restos de arquivos antigos e marcas no chão que denunciam batalhas passadas — talvez suas. A atmosfera é pesada, não por silêncio ou opressão, mas por uma sensação crescente de déjà vu distorcido. À frente, três figuras se formam lentamente, emergindo da distorção como ecos quebrados do passado. Mas você os reconhece. Eles não são novos. Eles são versões torturadas de inimigos que você já enfrentou — agora reconstruídos, modificados, mutados por algo desconhecido que corrompe a lógica do Etherion.')
    jogo1.digitar(texto26)

    time.sleep(1)

    print(f'\n[bold purple][Sistema]{personagem.nick} bateu de frente com [italic]"Os três mutados"[/italic][/bold purple]\n')

    print('\n[bold purple]Anomalian do Vórtice[/bold purple]')
    texto27 = ('Agora mais rápido, mais agressivo. Seu corpo se contorce em espirais invertidas de código, projetando instabilidade para o ambiente.\n')
    jogo1.digitar(texto27)

    print('\n[bold purple]Gárgula Carcinizada[/bold purple]')
    texto28 = ('Sua antiga forma metálica está agora coberta por placas cristalinas afiadas. Sua força física dobrou, e seus olhos brilham em azul profundo.\n')
    jogo1.digitar(texto28)

    print('\n[bold purple]Juiz Fragmentado[/bold purple]')
    texto28 = ('Sua aparência lembra uma máscara quebrada de si mesmo, com sua voz oscilando entre julgamento e loucura\n')
    jogo1.digitar(texto28)

    print('[bold purple][Sistema]Entidades reconhecidas em estado de mutação crítica. Recompensas elevadas. Letalidade: EXTREMA.[/bold purple]')
    print('[bold purple][Sistema]Dados sugerem correlação com os fragmentos instáveis colhidos anteriormente. Recomenda-se cautela e foco.[/bold purple]')

    texto29 = ('\nEsses mutantes são o reflexo de quanto mais você avança, mais o Labirinto lembra de você — e tenta usar sua própria jornada contra você. Não são apenas inimigos: são provas de que o sistema está reagindo. Adaptando-se.')
    jogo1.digitar(texto29)

    while True:
        opcao = inquirer.select(
            message="Como deseja proceder?\n",
            choices=[
                "⚔️ Iniciar combate direto",
                "👣 Tentar derrotar algum inimigo de surpresa enquanto você tenta blefar sobre sua existência (Requer perícia de blefe)",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem"
            ]
        ).execute()

        if opcao == "⚔️ Iniciar combate direto":
            vencedor = combate(personagem, lista_inimigos[4]) 
            if vencedor == personagem:
                lore_recompensa004(personagem)
                break
                print()

        elif opcao == "👣 Tentar derrotar algum inimigo de surpresa enquanto você tenta blefar sobre sua existência (Requer perícia de blefe)":
            if personagem.pericias['blefe'] > 20:
                #-1 inimigo
                vencedor = combate(personagem, lista_inimigos[5]) 
                if vencedor == personagem:
                    lore_recompensa004(personagem)
                    print()
            else:
                #Tenta blefar com os inimigos e toma no cu
                vencedor = combate(personagem, lista_inimigos[5]) 
                if vencedor == personagem:
                    lore_recompensa004(personagem)
                    print()

        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)

        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")

def lore_recompensa004(personagem):
    limpar_tela()
    item_escolhido002 = ''

    personagem.inventario[0].qtd = 3
    personagem.inventario[1].qtd = 3

    if personagem.raca == 'elfo':
        while True:
            print()
            opcao = inquirer.select(
            message="Qual destes 3 itens você deseja levar consigo?\n",
            choices=[
                "🎓 Elmo Dourado do Guardião Caído: Reluzente mesmo coberto de poeira e sangue, este elmo é símbolo de um antigo defensor élfico. Protege o portador e eleva sua imponência, mas é pesado e por conta disso é mais difícil de se locomover com ele. (+3 resistência), (+3 diplomacia), (-3 acrobacia)",
                "⚔️ Espada Longa do Veterano: Forjada nas eras antigas, passou por inúmeras batalhas. Seu fio é preciso e a lâmina, bem equilibrada. (+3 mano a mano)",
                "🛡️ Escudo de Madeira Encantada: Escudo leve feito de madeira das florestas élficas, reforçado com magia ancestral emanada pelas runas desenhadas nele. Resistente e útil para defesa. (+3 resistência)"
            ]
            ).execute()

            if opcao == "🎓 Elmo Dourado do Guardião Caído: Reluzente mesmo coberto de poeira e sangue, este elmo é símbolo de um antigo defensor élfico. Protege o portador e eleva sua imponência, mas é pesado e por conta disso é mais difícil de se locomover com ele. (+3 resistência), (+3 diplomacia), (-3 acrobacia)":

                personagem.inventario.append(lista_itens[39])
                item_escolhido001 = '🎓 Elmo Dourado do Guardião Caído'
                print()

            elif opcao == "⚔️ Espada Longa do Veterano: Forjada nas eras antigas, passou por inúmeras batalhas. Seu fio é preciso e a lâmina, bem equilibrada. (+3 mano a mano)":
                personagem.inventario.append(lista_itens[40])
                item_escolhido001 = '⚔️ Espada Longa do Veterano'
                print()

            elif opcao == "🛡️[3] Escudo de Madeira Encantada: Escudo leve feito de madeira das florestas élficas, reforçado com magia ancestral emanada pelas runas desenhadas nele. Resistente e útil para defesa. (+3 resistência)":
                personagem.inventario.append(lista_itens[41])
                item_escolhido001 = '🛡️ Escudo de Madeira Encantada'
                print()
            break
        
    
    elif personagem.raca == 'humano':
        while True:
            print()
            opcao = inquirer.select(
            message="Qual destes 3 itens você deseja levar consigo?\n",
            choices=[
                "🪓 Machado da Vanguarda: Machado robusto, pesado, feito para abrir caminho em meio ao caos. Aumenta a força bruta, mas atrapalha a destreza das mãos. (+6 mano a mano), (-3 mãos rápidas)",
                "🏹 Besta do Veterano: Uma besta com mecanismo reforçado e maior alcance. Esse equipamento acerta os adversários a distancia com muito mais potencia e velocidade que uma besta comum. (+3 mira)",
                "☠️ Medalhão do General morto: Relíquia de um antigo comandante. Impõe respeito e melhora a capacidade de liderança, mas carrega o peso do orgulho e não permite ataques pelas costas. (+3 diplomacia), (+3 inteligência), (-3 furtividade)"
            ]
            ).execute()

            if opcao == "🪓 Machado da Vanguarda: Machado robusto, pesado, feito para abrir caminho em meio ao caos. Aumenta a força bruta, mas atrapalha a destreza das mãos. (+6 mano a mano), (-3 mãos rápidas)":

                personagem.inventario.append(lista_itens[42])
                item_escolhido001 = '🪓 Machado da Vanguarda: Machado robusto'
                print()

            elif opcao == "🏹 Besta do Veterano: Uma besta com mecanismo reforçado e maior alcance. Esse equipamento acerta os adversários a distancia com muito mais potencia e velocidade que uma besta comum. (+3 mira)":
                personagem.inventario.append(lista_itens[43])
                item_escolhido001 = '🏹 Besta do Veterano'
                print()

            elif opcao == "☠️ Medalhão do General morto: Relíquia de um antigo comandante. Impõe respeito e melhora a capacidade de liderança, mas carrega o peso do orgulho e não permite ataques pelas costas. (+3 diplomacia), (+3 inteligência), (-3 furtividade)":
                personagem.inventario.append(lista_itens[44])
                item_escolhido001 = '☠️ Medalhão do General morto'
                print()
            break

    elif personagem.raca == 'draconiano':
        while True:
            print()
            opcao = inquirer.select(
            message="Qual destes 3 itens você deseja levar consigo?\n",
            choices=[
                "☠️ Bracelete de Ossos Esmagados: Feito com os ossos dos inimigos vencidos, simboliza a brutalidade e selvageria do exercito draconiano. É um artefato pesado que limita a agilidade das mãos. (+3 acrobacia), (+3 mano a mano), (-3 mãos rápidas)",
                "🦯 Lança da Escama Rubra: Símbolo da bravura dos guerreiros draconianos, ela foi forjada para perfurar escudos ao ser arremessada. Sua lâmina nunca perde o fio, permanecendo sempre afiada mesmo após anos de uso intenso. (+3 mira)",
                "🥾 Botas de assassinos Dracônicos: Calçados leves usadas por assassinos para melhorar a furtividade, os saltos e esquivas. O equipamento é desconfortável quando o usuário fica parado o que deixa mais difícil de mirar. (+3 acrobacia), (+3 furtividade), (-3 mira)"
            ]
            ).execute()

            if opcao == "☠️ Bracelete de Ossos Esmagados: Feito com os ossos dos inimigos vencidos, simboliza a brutalidade e selvageria do exercito draconiano. É um artefato pesado que limita a agilidade das mãos. (+3 acrobacia), (+3 mano a mano), (-3 mãos rápidas)":

                personagem.inventario.append(lista_itens[45])
                item_escolhido001 = '☠️ Bracelete de Ossos Esmagados'
                print()

            elif opcao == "🦯 Lança da Escama Rubra: Símbolo da bravura dos guerreiros draconianos, ela foi forjada para perfurar escudos ao ser arremessada. Sua lâmina nunca perde o fio, permanecendo sempre afiada mesmo após anos de uso intenso. (+3 mira)":
                personagem.inventario.append(lista_itens[46])
                item_escolhido001 = '🦯 Lança da Escama Rubra'
                print()

            elif opcao == "🥾 Botas de assassinos Dracônicos: Calçados leves usadas por assassinos para melhorar a furtividade, os saltos e esquivas. O equipamento é desconfortável quando o usuário fica parado o que deixa mais difícil de mirar. (+3 acrobacia), (+3 furtividade), (-3 mira)":
                personagem.inventario.append(lista_itens[47])
                item_escolhido001 = '🥾 Botas de assassinos Dracônicos'
                print(item_escolhido001)
            break
    
    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [400] \nPoção de cura [3]\nPoção de mana [3]\nItem: {item_escolhido002}[/bold purple]")
    text_inf = ('\nPressione ENTER para prosseguir...')
    digitar(text_inf)
    input('')

def lore_10_andar(personagem):
    limpar_tela()

    texto31 = ('O último dos três mutantes cai, desintegrando-se em uma explosão fragmentada de luz e dados corrompidos. O ambiente, antes distorcido por instabilidade e ecos falhos, começa lentamente a se recompor. O campo de batalha se silencia, mas o silêncio não traz paz — apenas expectativa. Uma onda fria percorre seu núcleo digital. Você sente que algo no Etherion acordou com esta batalha. Não foi só um teste... foi uma coleta de dados. ')
    jogo1.digitar(texto31)

    print('\n[bold purple][Sistema]Tríade Mutacional neutralizada. Mutações arquivadas. Instabilidade local reduzida.[/bold purple]')
    print('[bold purple][Sistema]Você foi observado. Seu padrão de combate está sendo interpretado. O próximo desafio não será uma simulação... será pessoal.[/bold purple]\n')

    texto32 = ('Você acorda… de pé.\nMas onde?\n Ao seu redor há apenas silêncio absoluto, do tipo que parece comprimir seus pensamentos, como se toda a realidade estivesse prendendo a respiração. Luz não vem de cima. Ela emana das paredes de espelho — milhões de superfícies refletindo versões fragmentadas de você: alguns machucados, outros sorrindo, alguns... mortos. Nenhum se move em sincronia com você. Eles vivem por conta própria. Eles o observam. E julgam. O chão é de vidro negro, refletindo com precisão algo que você não está fazendo. Ele se mexe antes de você. Ele te antecipa. No centro do salão, um trono feito de dados cristalizados flutua acima de um lago de vazio. Sobre ele, sentado em silêncio, está ele — a figura com sua silhueta, seu olhar... mas distorcido. A armadura que veste parece feita de algoritmos mortos, e a máscara que cobre metade de seu rosto pulsa em vermelho. Ele não levanta a voz. Ele penetra sua mente.')
    jogo1.digitar(texto32)
    time.sleep(1)

    print('\n[bold blue]"Você veio até aqui para fugir de mim… Mas tudo o que fez foi se aproximar."[/bold blue]')
    print('[bold blue]"O sistema não me criou. Você me alimentou."[/bold blue]')
    print('[bold blue]"Com cada escolha ignorada, cada parte de si enterrada nos andares anteriores."[/bold blue]')
    print('[bold blue]"Eu sou o que você trancou fora de si para sobreviver."[/bold blue]\n')

    texto33 = ('Ele se levanta.\nSeus pés não tocam o chão.\nTodos os espelhos se apagam.\n')
    digitar(texto33)

    print('[bold blue]"Vamos ver… quem é mais real."[/bold blue]\n')

    texto34 = ('A sua ficha treme. Não por instabilidade... mas por resposta emocional. Você sente medo. Não do combate. Mas do que pode ver se perder.')
    digitar(texto34)

    print('\n[bold purple]"Identidade Espelhada detectada. Proteções removidas. Resposta emocional em níveis críticos."[/bold purple]')
    print('[bold purple]"A integridade deste combate é absoluta. Sem manipulação externa. Sem chance de fuga."[/bold purple]')
    print('[bold purple]"Você está prestes a enfrentar: Eco Corrompido – O Reflexo Falho"[/bold purple]\n')

    while True:
        texto35 = '\n1. Iniciar o combate'
        digitar(texto35)

        try:
            time.sleep(1)
            esc_8 = input("\nEscolha uma opção: ").strip()
            if esc_8 not in ("1"):
                raise ValueError("❗ Opção inválida.")
            if esc_8 == "1":
                
                    lore_recompensa005(personagem)
                    lore_pos_10andar(personagem)
                    break

        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa005(personagem):
    limpar_tela()
    personagem.inventario[0].qtd = 5
    personagem.inventario[1].qtd = 5

    item_escolhido003 = ''
    
    if personagem.raca == 'elfo':
        item_escolhido003 = '🔨 Aljava rúnica'
        personagem.inventario.append(lista_itens[48])
            
    
    elif personagem.raca == 'humano':
        item_escolhido003 = '📜 Pergaminho da Revelação'
        personagem.inventario.append(lista_itens[49])

    elif personagem.raca == 'draconiano':
        item_escolhido003 = '🐲 Marca do dragão soberano:'
        personagem.inventario.append(lista_itens[50])

    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [900] \nPoção de cura [5]\nPoção de mana [5]\nItem: {item_escolhido003}[/bold purple]")
    text_inf = ('\nPressione ENTER para prosseguir...')
    jogo1.digitar(text_inf)
    input('')

def lore_pos_10andar(personagem):
    texto36 = ('O golpe final atravessa o peito do Echo Corrompido. Mas ele não sangra. Ele desfaz-se em luz — não como um inimigo derrotado, mas como uma parte de você sendo libertada. O trono estilhaça. Os espelhos explodem para dentro, não para fora, e todos os reflexos se alinham. Por um instante, todas as versões de você o encaram… e sorriem, em uníssono, antes de desaparecerem.\n O silêncio é restaurado. Mas ele agora é seu aliado, não seu inimigo.\n')
    jogo1.digitar(texto36)

    print('[bold purple][Sistema] Combate sistêmico encerrado. Integridade emocional assimilada. Nova funcionalidade desbloqueada.][/bold purple]')
    print('[bold purple][Sistema] Núcleo da Identidade absorvido. Você agora é reconhecido como Unidade Coerente.][/bold purple]\n')

    texto37 = ('À sua frente, um fragmento de espelho intacto flutua. Ao tocá-lo, ele se dissolve em códigos que se reorganizam como uma porta espiralada, levando ao próximo andar.')
    jogo1.digitar(texto37)

    while True:
        opcao = inquirer.select(
            message="O que deseja fazer?\n",
            choices=[
                "⬆️ Avançar para o Andar 6",
                "🎒 Investigar Inventário",
                "🔍 Conferir status do personagem"
            ]
        ).execute()

        if opcao == "⬆️ Avançar para o Andar 11":
            lore_recompensa005(personagem)
            jogo3.lore_11_andar(personagem)
            break
        elif opcao == "🎒 Investigar Inventário":
            inventario.interface_inv(personagem)
        elif opcao == "🔍 Conferir status do personagem":
            limpar_tela()
            personagem.mostrar_status()
            input("\nPressione ENTER para voltar...")
    


