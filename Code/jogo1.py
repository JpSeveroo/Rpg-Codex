import time
from ficha import Personagem
import sys
import os
from rich import print
from item import lista_itens
import inventario
from utills import digitar, tempo_digitar

def lore_introducao(personagem):
    print()
    texto1 = (' No silêncio absoluto de uma existência que não é mais carne nem alma, você desperta. Oque vê não é um mundo, mas um vasto espaço digital — uma planície infinita e vazia, onde o horizonte se dissolve em pixels azuis e violetas, iluminados por uma aurora elétrica que pulsa com o ritmo de um código ancestral. Acima, o céu é uma tela viva, uma tapeçaria de fragmentos de memória, dados e histórias esquecidas. O ar, ou o que resta dele, vibra comum zumbido constante, uma sinfonia mecânica e etérea, como o respirar sutil de uma inteligência que observa cada movimento. À distância, recortando o infinito, ergue-se o Labirinto de Etherion — uma torre monumental e impossivelmente alta, feita de açotranslúcido, luz pulsante e padrões de circuitos que se entrelaçam como raízes de umaárvore cibernética. Cada andar brilha com um espectro de cores e ecos de vozes perdidas,um convite e um aviso ao mesmo tempo. Uma mensagem fria e impessoal se materializa diante de você, uma sentença gravada notecido da realidade:\n')
    digitar(texto1)

    print(f"[bold purple][Sistema Etherion Iniciado.]\n"
      "[A única forma de liberdade é alcançar o último andar.]\n"
      "[Progresso será perdido em caso de morte.]\n"
      f"[Boa sorte, {personagem.nick}.][/bold purple]")
    
    print()
    texto3 = (' Você não é um ser físico, mas um Eco — uma consciência fragmentada, arrancada do mundo original pela Queda do Éter, um cataclismo que destruiu a linha entre a matéria e a energia, a vida e o código. Etherion é um santuário e uma prisão: aqui, a essência das raças ancestrais — humanos, elfos, draconianos — se fundiu e se perdeu, reciclada em uma tapeçaria digital onde magia e tecnologia são indistintas. Este não é um mundo de certezas, mas de possibilidades codificadas. Cada passo é um teste, cada sombra uma lembrança, cada inimigo um fragmento do passado e um desafio do presente. À sua frente, o Labirinto se estende como um abismo infinito, pulsando com segredos e armadilhas, guardando a verdade que pode libertá-lo — ou destruí-lo. Você pode: ')
    digitar(texto3)

    while True:
        texto4 = ('\n1. Avançar para o primeiro andar do Labirinto, iniciando sua ascensão rumo à liberdade. \n2. Investigar inventário')
        digitar(texto4)

        try:
            time.sleep(1)
            esc_1 = input("\nEscolha uma opção (1 ou 2): ").strip()
            if esc_1 not in ("1", "2"):
                raise ValueError("❗ Opção inválida.")

            if esc_1 == "1":
                lore_1_andar(personagem)
                break  # só sai do loop se for pra andar 1

            elif esc_1 == "2":
                inventario.interface_inv(personagem)
                lore_introducao(personagem)
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_1_andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.checkpoint >= 1:
        tempo_digitar(0)
    print()
    texto5 = 'Você atravessa o portal que o leva do vazio da planície para dentro do Labirinto. A luz muda, tornando-se mais fria e metálica. O chão abaixo é um mosaico de placas metálicas e circuitos pulsantes, estendendo-se até onde a vista alcança. O ar é pesado com uma energia estática, e a sensação de estar sendo observado é constante. À distância, silhuetas se movem entre os pilares de luz — 3 Gárgulas de Dados, sentinelas programadas para detectar e eliminar intrusos. Suas asas de metal rangem, e seus olhos brilham com uma luz vermelha ameaçadora. Uma voz sintética, reconhecida do terminal, ecoa no ambiente:\n'
    digitar(texto5)

    print(f"[bold purple][Sistema: “{personagem.nick}, prepare-se. O primeiro teste começou.”][/bold purple]")

    while True:
        texto6 = '\n1. Iniciar o combate — Enfrentar as Gárgulas de Dados com as habilidades que possui, aprendendo a dominar o sistema de turnos e a usar sua força para progredir. \n2. Investigar inventário'
        digitar(texto6)
        try:
            time.sleep(1)
            esc_1 = input("\nEscolha uma opção (1 ou 2): ").strip()
            if esc_1 not in ("1", "2"):
                raise ValueError("❗ Opção inválida.")
            if esc_1 == "1":
                #❗❗❗❗❗❗❗FALTA O COMBATE
                lore_recompensa001(personagem)
                lore_pos_1andar(personagem)
                break

            elif esc_1 == "2":
                inventario.interface_inv(personagem)
                lore_1_andar(personagem)
            break 
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa001(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    item_escolhido001 = ''
    if personagem.checkpoint >= 1:
        tempo_digitar(0)
    personagem.checkpoint += 1

    personagem.inventario.append(lista_itens[0])
    personagem.inventario[0].qtd = 1
    personagem.inventario.append(lista_itens[1])
    personagem.inventario[1].qtd = 1#Alterar a quantidade com extend dps

    if personagem.raca == 'elfo':
        while True:
            try:
                texto6 = ("\nQual destes 3 itens você deseja levar consigo? \n 🏹[1] Arco Simples: Um arco leve, resistente, símbolo do treinamento élfico. Não mágico e um pouco velho, mas usável. (+1 mira)\n 🍃[2] Broche da Folha: broche simples que pode ajudar em interações sociais. (+1 diplomacia)\n 🧤[3] Luvas Élficas surradas: leves e confortáveis, oferecem vantagem em tarefas delicadas. (+1 mãos rápidas) ")
                digitar(texto6)
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
                digitar(texto6)
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
                digitar(texto6)
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
    text_inf = ('\nPressione ENTER para prosseguir...')
    digitar(text_inf)
    a = input('')

def lore_pos_1andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.checkpoint >= 1:
        tempo_digitar(0)
    texto7 = ('\nCom o último golpe, a última Gárgula de Dados desmorona numa cascata de fragmentos de código, dissipando-se no ar frio do Labirinto. O silêncio retorna, pesado e cheio de expectativa. Sua ficha digital pulsa com uma luz verde, sinalizando o progresso — um novo degrau conquistado na escalada rumo ao último andar. Uma mensagem aparece diante de seus olhos:')
    digitar(texto7)

    print(f'[bold purple]\n[Sistema]: “Parabéns, {personagem.nick}. Andar 1 conquistado. \nLembre-se, agora não há mais volta, o que lhe resta é continuar persistindo até alcançar um ponto seguro, \nse falhar no caminho antes de alcançar um ponto seguro você terá problemas com as gárgulas novamente” [/bold purple]\n')

    texto8 = ('À frente, o caminho se abre para um corredor iluminado por fios de energia azul que serpenteiam pelas paredes metálicas. O ar vibra com uma tensão diferente — mais densa, como se algo mais antigo e complexo estivesse aguardando. Você dá um passo à frente, consciente de que cada andar é um passo mais perto da liberdade — ou do abismo.')  
    digitar(texto8)

    while True:
        try:
            texto9 = ('\n1. Avançar para o Andar 2\n2. Abrir o inventário\n3. Conferir Atributos')
            digitar(texto9)
            print('\n[bold purple] Oque você quer fazer agora?[/bold purple] ',end='')
            esc_2 = input("").strip()
            if esc_2 not in ("1", "2", "3"):
                raise ValueError("❗ Opção inválida.")
            if esc_2 == "1":
                lore_2_andar(personagem)
                break

            elif esc_2 == "2":
                inventario.interface_inv(personagem)
            elif esc_2 == "3":
                #Atributos
                print()

        except ValueError as e:
            print(f"{e} Tente novamente.")
    
def lore_2_andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.checkpoint >= 2:
        tempo_digitar(0)
    texto10 = ('\nAo cruzar o limiar do primeiro andar, a estrutura muda. A luz branca e fria cede espaço a um ambiente opaco, repleto de tons azul-escuros e verdes foscos. O chão agora parece instável — como vidro rachado — refletindo sua imagem distorcida a cada passo. Fragmentos de memória flutuam ao seu redor como pedaços de dados corrompidos: rostos sem nome, vozes sem origem, sentimentos desconectados. Este é o Mar de Fragmentos — um andar onde os resíduos de antigas consciências e dados quebrados se acumulam, gerando distorções no espaço e criando ameaças imprevisíveis. Você caminha entre os escombros flutuantes quando uma nova mensagem se sobrepõe à sua visão:')
    digitar(texto10)

    texto11 = ('Do meio da névoa de dados, surge uma nova entidade: o Anomalian, um espectro digital formado por memórias colapsadas e linhas de código expostas. Seus braços se alongam como fios rompidos, os olhos brilham com um azul pulsante e irregular. Ele não ruge... ele chia, como um arquivo corrompido tentando se reproduzir. A criatura se aproxima. Sua presença distorce os arredores. O chão treme. Sua ficha emite um alerta:')
    digitar(texto11)

    print('\n[bold purple][Sistema: “Este andar não testa sua força, mas sua estabilidade. Fragmentos instáveis detectados. Hostilidade: Alta.”]:[/bold purple]\n')

    texto11 = ('Do meio da névoa de dados, surge uma nova entidade: o Anomalian, um espectro digital formado por memórias colapsadas e linhas de código expostas. Seus braços se alongam como fios rompidos, os olhos brilham com um azul pulsante e irregular. Ele não ruge... ele chia, como um arquivo corrompido tentando se reproduzir. A criatura se aproxima. Sua presença distorce os arredores. O chão treme. Sua ficha emite um alerta:')
    digitar(texto11)

    print('\n[bold purple][Alerta: Corrupção emocional detectada. Combate iniciado.]:[/bold purple]\n')

########### ATE AQUI TAMO CANDENCIADO
    while True:
        try:
            time.sleep(1)
            texto12 = ('Você pode: \n1.Enfrentar o Anomalian — Confrontar a distorção com foco e resistência, dominando o combate contra uma entidade instável.\n2.Tentar Estabilizar o ambiente — Usar parte da sua energia para reconfigurar o campo ao seu redor, reduzindo a agressividade do inimigo. [Pontos de diplomacia necessários: 12]')
            digitar(texto12)

            print('\n[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_3 = input(" ").strip()
            if esc_3 not in ("1", "2"):
                raise ValueError("❗ Opção inválida.")
            if esc_3 == "1":
                #❗❗❗❗❗❗❗FALTA O COMBATE
                lore_recompensa002(personagem)
                lore_pos_2andar(personagem)
                print()

            elif esc_3 == "2" and personagem.atributos['diplomacia'] >= 12:
                #Vantagem para o personagem
                print()
            break 
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa002(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    personagem.inventario[0].qtd = 1
    personagem.inventario[0].qtd = 1
    if personagem.checkpoint >= 1:
        tempo_digitar(0)
    personagem.checkpoint += 1

    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [150] \nPoção de cura [1]\nPoção de mana [1]")
    text_inf = ('\nPressione ENTER para prosseguir...')
    digitar(text_inf)
    a = input('')


def lore_pos_2andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.checkpoint >= 2:
        tempo_digitar(0)
    texto13 = ('\nO corpo disforme do Anomalian se retorce uma última vez antes de desintegrar em uma explosão silenciosa de luz azulada e linhas quebradas. Os fragmentos de memória que flutuavam ao redor cessam seu giro caótico e, por um breve instante, o Mar de Fragmentos parece calmo. As distorções cessam. A corrupção regride. Você respira — ou simula respirar. A sensação de alívio é estranhamente real. Uma nova linha de código começa a se desenhar no chão à sua frente, como uma serpente de luz, guiando-o até um anel flutuante de dados, que pulsa lentamente.')
    digitar(texto13)

    print('\n[bold purple][Sistema: Instabilidade contida.”] \n[Sistema: Setor de Memória Intermediária desbloqueado. Andar 3 liberado.][/bold purple]')

    while True:
        try:
            time.sleep(1)
            texto14 = ("\nVocê pode:\n\n1. Avançar para o Andar 3\n2. Investigar inventário\n3. Conferir Atributos")
            digitar(texto14)
            time.sleep(1)
            print('\n[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_4 = input('')

            if esc_4 not in ("1", "2", "3"):
                raise ValueError("❗ Opção inválida.")
            if esc_4 == "1":
                texto13 = ('\nConforme você atravessa o anel, tudo ao redor se desfaz como uma tela sendo reinicializada. Por instantes, existe apenas escuridão e um sussurro distante — a mesma voz misteriosa de antes, ainda fragmentada, mas um pouco mais clara:')
                digitar(texto13)

                print('"[bold blue]...Eles nos dividem por camadas... mas somos inteiros... ainda somos inteiros..."[/bold blue]')

                texto15 = ('Você não tem tempo para responder.\nA escuridão dá lugar a uma nova paisagem: O Andar 3.')
                digitar(texto15)
                time.sleep(1)
                lore_3_andar(personagem)
                print()
            elif esc_4 == "2":
                inventario.interface_inv(personagem)
            elif esc_4 == "3":
                #Atributos
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_3_andar(personagem):
    if personagem.checkpoint >= 3:
        tempo_digitar(0)
    personagem.checkpoint +=1
    os.system('cls' if os.name == 'nt' else 'clear')
    
    texto16 = ('\nVocê atravessa o portal do Andar 3 e se encontra em uma cúpula colossal. As paredes circulares são revestidas por inúmeros cristais de dados, cada um pulsando com uma luz tênue em diferentes frequências, como batimentos digitais. O chão, liso e polido, reflete sua imagem como um espelho de mercúrio, distorcendo levemente a realidade. Não há sinal de inimigos, nem som que quebre o silêncio, exceto por um sutil zumbido de ruído branco. Contudo, uma sensação incômoda de que algo está fundamentalmente errado paira no ar. No centro da cúpula, uma estrutura imponente se ergue: uma esfinge negra, etérea e flutuante, sua forma absorvendo a pouca luz do ambiente.Uma mensagem espectral se materializa à sua frente: ')
    digitar(texto16)

    print(f'\n[bold purple][Sistema] "Desafio de Integridade Perceptiva iniciado."\n[Sistema] Qualquer erro lógico nesta sala desencadeará uma reinicialização forçada do {personagem.nick}.]\n[Sistema] Recompensa única detectada [/bold purple]\n')

    texto17 = ('A voz da esfinge ecoa pela cúpula, grave e ressonante, parecendo vir de todos os lugares e de lugar nenhum ao mesmo tempo:')
    digitar(texto17)

    print('[bold blue]"Viajante... Você sente a anomalia? O véu da realidade tremula aqui.\nPara avançar, seus olhos devem ver além do óbvio, sua mente deve discernir a desarmonia."[/bold blue]\n')

    texto18 = ('Ela se inclina ligeiramente, como se o observasse com atenção.')
    digitar(texto18)

    print('[bold blue]"Um único erro.\nUma falha em perceber o que se esconde à plena vista... e esta existência será reescrita.\nMas para aquele que enxerga a verdade, uma recompensa aguarda." [/bold blue]\n')

    texto19 = ('Para superar este desafio, você precisará ser perspicaz o suficiente. É um teste de acuidade, um confronto direto com a ilusão.')
    digitar(texto19)

    while True:
        try:
            texto20 = ("\nVocê pode:\n\n1. Enfrentar o Enigma, no qual sua capacidade de percepção determinará a dificuldade do desafio. Quanto mais aguçada sua percepção, mais claro será o caminho para a solução.\n2. Seguir em frente e Desistir, abandonando o enigma sem tentar, perdendo a chance de obter uma recompensa única, mas avança para o próximo andar sem sofrer penalidades.")
            digitar(texto20)
            
            time.sleep(1)
            print('\n[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_5 = input('')
            if esc_5 not in ("1", "2"):
                raise ValueError("❗ Opção inválida.")
            if esc_5 == "1":
                lore_1_enigma(personagem)

            elif esc_5 == "2":
                lore_4_andar(personagem)
            break 
        except ValueError as e:
            print(f"{e} Tente novamente.")


#FAZER A PARTE DE SAIR DO INVENTARIO COLOCAR PRA VOLTAR PRA ESCOLHA
#ATRIBUTOS
#ADICIONAR POÇOES NO INV
#FAZER O CHECKPOINT
def lore_1_enigma(personagem):
    if personagem.checkpoint >= 3:
        tempo_digitar(0)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.andar_esfinge_completado:
        print("[bold purple]⚠️ O Andar da Esfinge foi destruído por corrompimento dimensional. Você avança direto para o próximo andar...[/bold purple]")
        lore_4_andar(personagem)
        return
    
    else:
        if personagem.atributos['percepcao'] >= 18:
            while True:
                try:
                    print('[bold purple][italic]"Sempre sigo você, \nMas não tenho vida,\n Só apareço quando a luz me permite."[/italic][/bold purple]\n')
                    texto21 = ('Alternativas:\n A) Um animal domesticado 🐕 \nB) Sua sombra 🌑 \nC) Um reflexo no espelho 🪞')
                    digitar(texto21)

                    time.sleep(1)
                    print('\n [bold purple]Qual a sua resposta? [/bold purple]',end='')
                    resp_1 = input('').lower()

                    if resp_1 not in ("a", "b", "c"):
                        raise ValueError("❗ Opção inválida.")
                    if resp_1 == "a":
                            morte_esfinge(personagem)
                            break

                    elif resp_1 == "b":
                        personagem.andar_esfinge_completado = True
                        texto23 = ('O silêncio na Cúpula da Percepção se quebra quando o Eco profere a resposta correta. Um zumbido suave preenche o ar, e a Esfinge Negra se inclina.')
                        digitar(texto23)

                        print(f'[bold blue]"{personagem.nick}... Você sim vê a verdade "[/bold blue]')

                        texto24 = ('Sua voz ecoa, sem surpresa, mas com reconhecimento. A Esfinge então se dissolve em partículas douradas, revelando a "🎭 Máscara da inverdade". O caminho para o próximo andar se abre, e Etherion aceita sua acuidade. A jornada continua, e você carrega a máscara da inverdade.')
                        digitar(texto24)
                        personagem.inventario.append(lista_itens[11])

                        lore_4_andar(personagem)
                        break
                    
                    elif resp_1 == "c":
                        morte_esfinge(personagem)
                        break
                except ValueError as e:
                    print(f"{e} Tente novamente.")       

        
        elif 12 <= personagem.atributos['percepcao'] < 18:
            while True:
                try:
                    print('[bold purple][italic]"Não sou vivo, mas cresço, \nNão tenho pulmões, mas respiro,\n Não tenho boca, mas devoro tudo."[/italic][/bold purple]\n')
                    texto22 = ('Alternativas: \nA) O fogo 🔥 \nB) A sombra 🌑 \nC) O tempo ⏳')
                    digitar(texto22)
                    
                    time.sleep(1)
                    print('\n [bold purple]Qual a sua resposta? [/bold purple]',end='')
                    resp_1 = input('').lower()

                    if resp_1 not in ("a", "b", "c"):
                        raise ValueError("❗ Opção inválida.")
                    if resp_1 == "a":
                        personagem.andar_esfinge_completado = True
                        texto23 = ('O silêncio na Cúpula da Percepção se quebra quando o Eco profere a resposta correta. Um zumbido suave preenche o ar, e a Esfinge Negra se inclina.')
                        digitar(texto23)

                        print(f'[bold blue]"{personagem.nick}... Você sim vê a verdade "[/bold blue]')

                        texto24 = ('Sua voz ecoa, sem surpresa, mas com reconhecimento. A Esfinge então se dissolve em partículas douradas, revelando a "🎭 Máscara da inverdade". O caminho para o próximo andar se abre, e Etherion aceita sua acuidade. A jornada continua, e você carrega a máscara da inverdade.')
                        digitar(texto24)
                        personagem.inventario.append(lista_itens[11])
                        lore_4_andar(personagem)
                        break
                    
                    elif resp_1 == "b":
                        morte_esfinge(personagem)
                        break
                    
                    elif resp_1 == "c":
                        morte_esfinge(personagem)
                        break

                except ValueError as e:
                    print(f"{e} Tente novamente.")  

        elif personagem.atributos['percepcao'] < 12:
            while True:
                try:
                    print('[bold purple][italic]"Não tenho forma, nem sombra que me prenda,\n Sou a força que molda e que desvenda, \nEm silêncio corro, sem deixar vestígio, \nTransformo o sólido em poeira, \nE ainda que eu jamais seja tocado, \nSem mim, nada se move, nada existe."[/italic][/bold purple]\n')
                    texto23 = ('\nA) A essência do tempo ⏳ \nB) O sopro invisível do vento 🌬️ \nC) O pensamento eterno 🧠')
                    digitar(texto23)

                    time.sleep(1)
                    print('\n [bold purple]Qual a sua resposta? [/bold purple]',end='')
                    resp_1 = input('').lower()

                    if resp_1 not in ("a", "b", "c"):
                        raise ValueError("❗ Opção inválida.")
                    if resp_1 == "a":
                        morte_esfinge(personagem)
                        break

                    elif resp_1 == "b":
                        personagem.andar_esfinge_completado = True
                        texto23 = ('O silêncio na Cúpula da Percepção se quebra quando o Eco profere a resposta correta. Um zumbido suave preenche o ar, e a Esfinge Negra se inclina.')
                        digitar(texto23)

                        print(f'[bold blue]"{personagem.nick}... Você sim vê a verdade "[/bold blue]')

                        texto24 = ('Sua voz ecoa, sem surpresa, mas com reconhecimento. A Esfinge então se dissolve em partículas douradas, revelando a "🎭 Máscara da inverdade". O caminho para o próximo andar se abre, e Etherion aceita sua acuidade. A jornada continua, e você carrega a máscara da inverdade.')
                        digitar(texto24)
                        personagem.inventario.append(lista_itens[11])
                        lore_4_andar(personagem)
                        break

                    elif resp_1 == "c":
                        morte_esfinge(personagem)
                        break
                except ValueError as e:
                    print(f"{e} Tente novamente.") 


def morte_esfinge(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')

    personagem.andar_esfinge_completado = True
    texto22 = ('O silêncio na Cúpula da Percepção a resposta é proferida. Um instante de suspense se estende, pesado com a expectativa da Esfinge Negra de Aethelgard. Mas a calma é logo rompida por um zumbido agudo, quase um chiado furioso. A Esfinge, antes imóvel, contorce sua forma etérea, e um brilho vermelho intenso pulsa em seus olhos. Não há mais perguntas. A indignação da entidade por ter recebido a alternativa incorreta é palpável, reverberando pelas paredes de cristal. Em um instante brutal, a cúpula se torna um vórtice de dados colapsados, e você é consumido pela fúria de uma verdade distorcida. A percepção falha selou seu destino: você se desintegra em um véu de ruído branco, e a escuridão o engole. Ao despertar, o Ponto de Início o aguarda, o vazio da planície se estendendo à sua frente, e a Torre de Etherion, indiferente, erguendo-se à distância. A lição é brutal: a falha na percepção não é um tropeço, é uma sentença de retorno forçado, uma repetição eterna até que a verdade seja finalmente alcançada.')
    digitar(texto22)
    print(f'[bold red]🩸 {personagem.nick} MORREU [/bold red]')
    lore_1_andar(personagem)


def lore_4_andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.checkpoint >= 4:
        tempo_digitar(0)
    personagem.checkpoint+=1
    texto25 = ('Você atravessa o portal e adentra uma vasta câmara mergulhada em sombras oscilantes, onde a luz parece hesitar antes de preencher o espaço. As paredes se distorcem como se fossem feitas de líquido escuro e espelhado, refletindo imagens fragmentadas de você mesmo — rostos que sorriem, que choram, que gritam, mas que não são você. O ar pulsa com um murmúrio baixo, um coro de vozes apagadas e risadas abafadas, ecos perdidos de consciências presas que se contorcem tentando manipular a realidade ao redor. No centro da sala, três figuras espectrais surgem como sombras vivas, seus rostos mudando e se rearranjando numa dança inquietante de feições falsas e distorcidas. São os Três ceifadores da Ilusão — entidades que personificam suas dúvidas, medos e inseguranças, prontas para testar a sua mente e espírito. O silêncio é cortado por um sussurro sintético, reverberando em sua mente:')
    digitar(texto25)

    print(f'[bold purple][Sistema] {personagem.nick}, neste salão, a verdade é uma arma maleável. Use sua perícia de blefar para virar o jogo, pois nem tudo aqui pode ser enfrentado pela força bruta.[/bold purple]')
    
    while True:
        try:
            texto26 = ('\n1. Iniciar combate\n2. Abrir o inventário\n3. Conferir Atributos')
            digitar(texto26)
            print('\n[bold purple] Oque você quer fazer agora?[/bold purple] ',end='')
            esc_2 = input("").strip()
            if esc_2 not in ("1", "2", "3"):
                raise ValueError("❗ Opção inválida.")
            if esc_2 == "1":
                #COMBATEEEEEEEE
                lore_recompensa003(personagem)
                lore_pos_4andar(personagem)
                break

            elif esc_2 == "2":
                inventario.interface_inv(personagem)
            elif esc_2 == "3":
                #Atributos
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa003(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    personagem.inventario[0].qtd = 2
    personagem.inventario[1].qtd = 2
    if personagem.checkpoint >= 3:
        tempo_digitar(0)
    personagem.checkpoint+=1
    item_escolhido002 = ''

    if personagem.raca == 'elfo':
        while True:
            try:
                texto27 = ("\nQual destes 3 itens você deseja levar consigo? \n 🏹[1] Arco Longo Élfico: Um arco elegante feito de madeira de altíssima qualidade, imbuído com encantamentos que melhoram a precisão da flechada. (+2 mira)\n ⚔️[2] espada fio da lua: espada forjada sob a lua cheia de Ilirien com corte preciso e detalhes em prata.(+2 mano a mano)\n 👑 Tiara da sabedoria: tiara perdida de antigos filósofos e pensadores elfos. Garante um aumento do raciocínio do usuário. (+2 percepção)")
                digitar(texto27)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa002 = input().strip()

                if recompensa002 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa002 == "1":
                    personagem.inventário.append(lista_itens[12])
                    item_escolhido002 = '🏹 Arco Longo Élfico'
                    print()

                elif recompensa002 == "2":
                    personagem.inventário.append(lista_itens[13])
                    item_escolhido002 = '⚔️ Espada fio da lua'
                    print()
                elif recompensa002 == "3":
                    personagem.inventário.append(lista_itens[15])
                    item_escolhido002 = '👑 Tiara da sabedoria'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")
    
    elif personagem.raca == 'humano':
        while True:
            try:
                texto6 = ("\nQual destes 3 itens você deseja levar consigo? \n 🏹[1] X-besta: Ferramenta humana criada para competir com os arcos encantados dos elfos. (+2 mira)\n 🩴[2] Sandálias de Hermes: Sandálias que dizem ser do próprio deus grego, mas na verdade é apenas uma sandália boa para se movimentar. (+2 acrobacia)\n 🥷[3] Capa de ladrão: capa que ajuda o personagem a passar despercebido e aumenta o saque. (+2 mãos rápidas)")
                digitar(texto6)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa002 = input().strip()

                if recompensa002 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa002 == "1":
                    personagem.inventário.append(lista_itens[14])
                    item_escolhido002 = '🏹 X-besta'
                    print()

                elif recompensa002 == "2":
                    personagem.inventario.append(lista_itens[16])
                    item_escolhido002 = '🩴 Sandálias de Hermes'
                    print()
                elif recompensa002 == "3":
                    personagem.inventario.append(lista_itens[17])
                    item_escolhido002 = '🥷 Capa de ladrão'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")

    elif personagem.raca == 'draconiano':
        while True:
            try:
                texto6 = ("\nQual destes 3 itens você deseja levar consigo? \n 🗡️[1] Lança de caça: Uma lança feita pelos draconianos para arremessar. (+1 mira).\n 🧿[2] Talismã da Fúria: Um talismã que deixa o personagem extremamente suscetível a raiva. Aumenta a força mas diminui a razão. (+1 mano a mano), (+1 resistência), (-2 percepção)\n 🥾[3] Botas de Couro: melhora a armadura e a resistência a terrenos difíceis (lama, neve, areia) fora de combate. (+2 resistência)")
                digitar(texto6)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa002 = input().strip()

                if recompensa002 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa002 == "1":
                    personagem.inventario.append(lista_itens[18])
                    item_escolhido002 = '🗡️ Lança de caça'
                    print()

                elif recompensa002 == "2":
                    personagem.inventario.append(lista_itens[19])
                    item_escolhido002 = '🧿 Talismã da Fúria'
                    print()
                elif recompensa002 == "3":
                    personagem.inventario.append(lista_itens[7])
                    item_escolhido002 = '🥾 Botas de Couro:'
                    print()
                break 
            except ValueError as e:
                print(f"{e} Tente novamente. Lembre-se de digitar apenas o dígito referente ao item.")

    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [280] \nPoção de cura [1]\nPoção de mana [1]\nItem: {item_escolhido002}[/bold purple]")
    text_inf = ('\nPressione ENTER para prosseguir...')
    digitar(text_inf)
    a = input('')

def lore_pos_4andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.checkpoint >= 4:
        tempo_digitar(0)
    texto27 = ('\nAs últimas sombras dos Três Juízes da Ilusão se desfazem em fragmentos cintilantes de luz distorcida, evaporando-se no ar pesado da câmara. O silêncio que se instala é profundo, quase palpável, como se o próprio tempo respirasse de forma suspensa. Sua respiração — ou o que a simula — parece o único som que permanece, um ritmo débil em meio ao vazio. O chão, antes espelhado e instável, começa a mudar lentamente. Os reflexos se apagam e, em seu lugar, surge um mosaico complexo de códigos fluindo, luzes pulsando e circuitos vibrando com uma energia ancestral. Cada fragmento conta uma história — pedaços de dados, memórias e realidades codificadas que se entrelaçam numa dança eterna. À sua frente, uma enorme porta translúcida se materializa, feita de vidro etéreo e linhas de código trançadas como veias de energia pura. Ela pulsa com uma luz vermelha profunda, quase viva, e em sua superfície, uma silhueta começa a emergir — uma forma colossal, uma fusão de carne, circuitos e magia. Uma voz ecoa no salão, reverberando dentro de sua mente como um trovão distante, fria e cheia de autoridade:')
    digitar(texto27)

    print('\n[bold blue]"Eu sou Kairon, o Guardião do Abismo — o elo perdido entre a essência e o código.\nVocês, ecos fragmentados, se atrevem a escalar até meu domínio, desafiando a ordem que sustenta este Labirinto.\nNão é apenas sua força que será testada, mas sua própria realidade.\nProve que sua existência é mais do que ruído corrompido.\nEnfrente-me... ou seja apagado para sempre."[/bold blue]\n')

    texto28 = ('A porta se abre lentamente, revelando uma arena circular gigantesca, onde os dados fluem como rios de energia vermelha e negra, turbulenta e imprevisível. No centro, Kairon espera, seus olhos de um azul profundo perfurando sua consciência.')
    digitar(texto28)

    print('[bold purple][Sistema] não será apenas um combate — será um teste decisivo de sua vontade, astúcia e da síntese entre sua essência e a tecnologia que o mantém vivo.[/bold purple]')

    time.sleep(3)
    lore_5_andar(personagem)

def lore_5_andar(personagem):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.checkpoint >= 5:
        tempo_digitar(0)
    texto29 = ('Você adentra o quinto andar do Labirinto Etherion, conhecido como o Abismo de Kairon — uma vastidão desolada onde a realidade se funde ao código em um cenário traiçoeiro e instável. O chão sob seus pés é uma malha vibrante de fragmentos digitais que se entrelaçam e se desfazem sem aviso, formando plataformas suspensas sobre abismos infinitos, pontes feitas de linhas de código cintilante que podem desaparecer a qualquer momento e superfícies com distorções magnéticas que interferem na sua movimentação. O ar é denso e pesado, comprimido por forças invisíveis que sugam sua energia e testam sua resistência, enquanto feixes vermelhos e negros cortam o ambiente, e ecos distorcidos de dados corrompidos zumbem em sua mente, aumentando a tensão a cada passo.')
    digitar(texto29)

    texto30 = ('O terreno exige agilidade, atenção e equilíbrio extremo, onde um deslize pode significar queda no vazio. Nesse momento, uma mensagem surge diante de você, uma advertência do sistema:')
    digitar(texto30)

    print('[bold purple][Sistema] — Aviso! Este andar apresenta terreno altamente instável e perigoso. \nEquipamentos que aumentem sua estabilidade e mobilidade, como botas magnéticas ou escudos estabilizadores, podem facilitar sua travessia e reduzir os riscos de queda.[/bold purple]')

    texto31 = ('Ciente do desafio iminente, você avança com cautela, sabendo que à frente o Guardião do Abismo, Kairon, espera para testar sua força, astúcia e capacidade de sobreviver ao caos pulsante deste labirinto fragmentado.')
    digitar(texto31)

    while True:
        try:
            texto26 = ('\n1. Iniciar combate')
            digitar(texto26)
            print('\n[bold purple]Oque você quer fazer agora?[/bold purple] ',end='')
            esc_2 = input("").strip()
            if esc_2 not in ("1"):
                raise ValueError("❗ Opção inválida.")
            if esc_2 == "1":
                #COMBATEEEEEEEE
                #Checkpoint
                break
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa004(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    if personagem.checkpoint >= 5:
        tempo_digitar(0)
    personagem.checkpoint+=1
    personagem.inventario[0].qtd = 5
    personagem.inventario[1].qtd = 5

    item_escolhido003 = ''
    
    if personagem.raca == 'elfo':
        item_escolhido003 = '🧥 Manto do caído'
        personagem.inventario.append(lista_itens[1])
            
    
    elif personagem.raca == 'humano':
        item_escolhido003 = '👹 Colar da maldade'
        personagem.inventario.append(lista_itens[1])

    elif personagem.raca == 'draconiano':
        item_escolhido003 = '🛡️ Armadura Negra Abissal:'
        personagem.inventario.append(lista_itens[1])

    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [700] \nPoção de cura [5]\nPoção de mana [5]\nItem: {item_escolhido003}[/bold purple]")
    text_inf = ('\nPressione ENTER para prosseguir...')
    digitar(text_inf)
    a = input('')


if __name__ == "__main__":
    p = Personagem()
    lore_introducao(p)