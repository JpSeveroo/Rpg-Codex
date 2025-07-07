import time
from ficha import Personagem
import sys
import os
from rich import print
from item import lista_itens
import inventario

def digitar(texto, delay=0.00):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(delay)
    print()

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
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_1_andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')

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
                time.sleep(8)
                lore_pos_1andar(personagem)
                break
                print()

            elif esc_1 == "2":
                inventario.interface_inv(personagem)
            break 
        except ValueError as e:
            print(f"{e} Tente novamente.")


def lore_recompensa001(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    item_escolhido001 = ''

    personagem.inventario.append(lista_itens[0])
    personagem.inventario.append(lista_itens[1])#Alterar a quantidade com extend dps

    if personagem.raca == 'elfo':
        while True:
            try:
                texto6 = ("\nQual destes 3 itens você deseja levar consigo? \n 🏹[1] Arco Simples: Um arco leve, resistente, símbolo do treinamento élfico. Não mágico e um pouco velho, mas usável. (vai poder usar mira)\n 🍃[2] Broche da Folha: broche simples que pode ajudar em interações sociais. (+1 diplomacia)\n 🧤[3] Luvas Élficas surradas: leves e confortáveis, oferecem vantagem em tarefas delicadas. (+1 mãos rápidas) ")
                digitar(texto6)
                time.sleep(1)

                print(f"[bold purple][Sistema: “{personagem.nick}, Escolha com sabedoria... ”][/bold purple]", end='')
                recompensa001 = input().strip()

                if recompensa001 not in ("1", "2","3"):
                    raise ValueError("❗ Opção inválida.")
                if recompensa001 == "1":
                    personagem.inventário.append(lista_itens[2])
                    item_escolhido001 = '🏹 Arco Simples'
                    print()

                elif recompensa001 == "2":
                    personagem.inventário.append(lista_itens[3])
                    item_escolhido001 = '🍃 Broche da Folha'
                    print()
                elif recompensa001 == "3":
                    personagem.inventário.append(lista_itens[4])
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
                    personagem.inventário.append(lista_itens[5])
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
    text_inf = ('\nItens sendo computados...')
    digitar(text_inf)

def lore_pos_1andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')

    texto7 = ('\nCom o último golpe, a última Gárgula de Dados desmorona numa cascata de fragmentos de código, dissipando-se no ar frio do Labirinto. O silêncio retorna, pesado e cheio de expectativa. Sua ficha digital pulsa com uma luz verde, sinalizando o progresso — um novo degrau conquistado na escalada rumo ao último andar. Uma mensagem aparece diante de seus olhos:')
    digitar(texto7)

    print(f'[bold purple]\n[Sistema]: “Parabéns, {personagem.nick}. Andar 1 conquistado. \nLembre-se, agora não há mais volta, o que lhe resta é continuar persistindo até alcançar um ponto seguro, \nse falhar no caminho antes de alcançar um ponto seguro você terá problemas com as gárgulas novamente” [/bold purple]\n')

    texto8 = ('À frente, o caminho se abre para um corredor iluminado por fios de energia azul que serpenteiam pelas paredes metálicas. O ar vibra com uma tensão diferente — mais densa, como se algo mais antigo e complexo estivesse aguardando. Você dá um passo à frente, consciente de que cada andar é um passo mais perto da liberdade — ou do abismo.')  
    digitar(texto8)

    while True:
        try:
            texto9 = ('\n 1. Avançar para o Andar 2\n2. Abrir o inventário\n3. Conferir Atributos: ')
            digitar(texto9)
            print('[bold purple] Oque você quer fazer agora?[/bold purple] ',end='')
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
    texto10 = ('Ao cruzar o limiar do primeiro andar, a estrutura muda. A luz branca e fria cede espaço a um ambiente opaco, repleto de tons azul-escuros e verdes foscos. O chão agora parece instável — como vidro rachado — refletindo sua imagem distorcida a cada passo. Fragmentos de memória flutuam ao seu redor como pedaços de dados corrompidos: rostos sem nome, vozes sem origem, sentimentos desconectados. Este é o Mar de Fragmentos — um andar onde os resíduos de antigas consciências e dados quebrados se acumulam, gerando distorções no espaço e criando ameaças imprevisíveis. Você caminha entre os escombros flutuantes quando uma nova mensagem se sobrepõe à sua visão:')
    digitar(texto10)

    print('[bold purple][Sistema: “Este andar não testa sua força, mas sua estabilidade. Fragmentos instáveis detectados. Hostilidade: Alta.”]:[/bold purple]')

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
            texto12 = ('Você pode: \n1.Enfrentar o Anomalian — Confrontar a distorção com foco e resistência, dominando o combate contra uma entidade instável.\n2.Tentar Estabilizar o ambiente — Usar parte da sua energia para reconfigurar o campo ao seu redor, reduzindo a agressividade do inimigo. [Pontos de diplomacia necessários: 12]\n')
            digitar(texto12)

            print('[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_3 = input(" ").strip()
            if esc_3 not in ("1", "2"):
                raise ValueError("❗ Opção inválida.")
            if esc_3 == "1":
                #Inicia o combate contra o anomalian
                print()

            elif esc_3 == "2" and personagem.atributos['diplomacia'] >= 12:
                #Vantagem para o personagem
                print()
            break 
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_recompensa002(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(8)
    personagem.inventario.append(lista_itens[0])
    personagem.inventario.append(lista_itens[1])

    print(f"[bold purple][Sistema] 🪙   RECOMPENSAS: \nXp: [150] \nPoção de cura [1]\nPoção de mana [1]")
    text_inf = ('\nItens sendo computados...')
    digitar(text_inf)

def lore_pos_2andar(personagem):
    texto13 = ('O corpo disforme do Anomalian se retorce uma última vez antes de desintegrar em uma explosão silenciosa de luz azulada e linhas quebradas. Os fragmentos de memória que flutuavam ao redor cessam seu giro caótico e, por um breve instante, o Mar de Fragmentos parece calmo. As distorções cessam. A corrupção regride. Você respira — ou simula respirar. A sensação de alívio é estranhamente real. Uma nova linha de código começa a se desenhar no chão à sua frente, como uma serpente de luz, guiando-o até um anel flutuante de dados, que pulsa lentamente.')
    digitar(texto13)

    texto13 = ('\nO corpo disforme do Anomalian se retorce uma última vez antes de desintegrar em uma explosão silenciosa de luz azulada e linhas quebradas. Os fragmentos de memória que flutuavam ao redor cessam seu giro caótico e, por um breve instante, o Mar de Fragmentos parece calmo. As distorções cessam. A corrupção regride. Você respira — ou simula respirar. A sensação de alívio é estranhamente real. Uma nova linha de código começa a se desenhar no chão à sua frente, como uma serpente de luz, guiando-o até um anel flutuante de dados, que pulsa lentamente.')
    digitar(texto13)

    print('\n[bold purple][Sistema: Instabilidade contida.”] \n[Sistema: Setor de Memória Intermediária desbloqueado. Andar 3 liberado.][/bold purple]\n')

    while True:
        try:
            time.sleep(1)
            texto14 = ("\nVocê pode:\n\n 1. Avançar para o Andar 3\n2. Investigar inventário\n3. Conferir Atributos: ")
            digitar(texto14)
            print('[bold purple]Qual a sua escolha? [/bold purple]',end='')
            esc_4 = input('')

            if esc_4 not in ("1", "2", "3"):
                raise ValueError("❗ Opção inválida.")
            if esc_4 == "1":
                texto13 = ('Conforme você atravessa o anel, tudo ao redor se desfaz como uma tela sendo reinicializada. Por instantes, existe apenas escuridão e um sussurro distante — a mesma voz misteriosa de antes, ainda fragmentada, mas um pouco mais clara:')
                digitar(texto13)

                print('"[bold blue]...Eles nos dividem por camadas... mas somos inteiros... ainda somos inteiros..."[/bold blue]')

                texto15 = ('Você não tem tempo para responder.\nA escuridão dá lugar a uma nova paisagem: O Andar 3.')
                digitar(texto15)
                time.sleep(1)
                lore_3_andar()
                print()
            elif esc_4 == "2":
                inventario.interface_inv(personagem)
            elif esc_4 == "3":
                #Atributos
                print()
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_3_andar(personagem):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    texto16 = ('\nVocê atravessa o portal do Andar 3 e se encontra em uma cúpula colossal. As paredes circulares são revestidas por inúmeros cristais de dados, cada um pulsando com uma luz tênue em diferentes frequências, como batimentos digitais. O chão, liso e polido, reflete sua imagem como um espelho de mercúrio, distorcendo levemente a realidade. Não há sinal de inimigos, nem som que quebre o silêncio, exceto por um sutil zumbido de ruído branco. Contudo, uma sensação incômoda de que algo está fundamentalmente errado paira no ar. No centro da cúpula, uma estrutura imponente se ergue: uma esfinge negra, etérea e flutuante, sua forma absorvendo a pouca luz do ambiente.Uma mensagem espectral se materializa à sua frente: ')
    digitar(texto16)

    print(f'\n[bold purple][Sistema] "Desafio de Integridade Perceptiva iniciado."\n [Sistema] Qualquer erro lógico nesta sala desencadeará uma reinicialização forçada do {personagem.nick}.]\n [Sistema] Recompensa única detectada [/bold purple]\n')

    texto17 = ('A voz da esfinge ecoa pela cúpula, grave e ressonante, parecendo vir de todos os lugares e de lugar nenhum ao mesmo tempo:')
    digitar(texto17)

    print('\n[bold blue]"Viajante... Você sente a anomalia? O véu da realidade tremula aqui. Para avançar, seus olhos devem ver além do óbvio, sua mente deve discernir a desarmonia."[/bold blue]\n')

    texto18 = ('Ela se inclina ligeiramente, como se o observasse com atenção.')
    digitar(texto18)

    print('\n[bold blue]"Um único erro. Uma falha em perceber o que se esconde à plena vista... e esta existência será reescrita. Mas para aquele que enxerga a verdade, uma recompensa aguarda." [/bold blue]\n')

    texto19 = ('Para superar este desafio, você precisará ser perspicaz o suficiente. É um teste de acuidade, um confronto direto com a ilusão.')
    digitar(texto19)

    while True:
        try:
            texto20 = ("\nVocê pode:\n\n1. Enfrentar o Enigma Sua capacidade de percepção determinará a dificuldade do desafio. Quanto mais aguçada sua percepção, mais claro será o caminho para a solução.\n2. Seguir em frente e Desistir: Você abandona o enigma sem tentar, perde a chance de obter a recompensa única, mas avança para o próximo andar sem sofrer penalidades.")
            digitar(texto20)
            
            print('[bold purple]Qual a sua escolha? [/bold purple]',end='')
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


#TERMINAR A PARTE ABAIXO 
#FAZER A PARTE DE SAIR DO INVENTARIO COLOCAR PRA VOLTAR PRA ESCOLHA
#ATRIBUTOS
#ADICIONAR POÇOES NO INV
#FAZER A VERIFICAÇÃO DO PERSONAGEM PRA VER QUAL ENIGMA ELE VAI PEGAR
def lore_1_enigma(personagem):
    if personagem.atributos['percepcao'] >= 18:
        while True:
            try:
                print('[bold purple]\033"Sempre sigo você, \nMas não tenho vida,\n Só apareço quando a luz me permite."\033[0m[/bold purple]\n')
                texto21 = ('Alternativas:\n A) Um animal domesticado 🐕 \nB) Sua sombra 🌑 \nC) Um reflexo no espelho 🪞')
                digitar(texto21)

                print('\n [bold purple]Qual a sua resposta? [/bold purple]',end='')
                resp_1 = input('').lower()

                if resp_1 not in ("a", "b", "c"):
                    raise ValueError("❗ Opção inválida.")
                if resp_1 == "a":

                    #DEPOIS EU AJEITO FDP
                    O silêncio na Cúpula da Percepção prevalece enquanto o Eco [PLAYER] profere sua resposta. Um instante de suspense se estende, pesado com a expectativa da Esfinge Negra de Aethelgard. Mas a calma é logo rompida por um zumbido agudo, quase um chiado furioso. A Esfinge, antes imóvel, contorce sua forma etérea, e um brilho vermelho intenso pulsa em seus olhos. Não há mais perguntas. A indignação da entidade por ter recebido a alternativa incorreta é palpável, reverberando pelas paredes de cristal. Em um instante brutal, a cúpula se torna um vórtice de dados colapsados, e o Eco é consumido pela fúria de uma verdade distorcida. A percepção falha selou seu destino: o Eco se desintegra em um véu de ruído branco, e a escuridão o engole. Ao despertar, o Ponto de Início o aguarda, o vazio da planície se estendendo à sua frente, e a Torre de Etherion, indiferente, erguendo-se à distância. A lição é brutal: a falha na percepção não é um tropeço, é uma sentença de retorno forçado, uma repetição eterna até que a verdade seja finalmente alcançada.
                    lore_1_enigma(personagem)

                elif resp_1 == "b":
                    lore_4_andar(personagem)
                
                elif resp_1 == "c":
                    lore_4_andar(personagem)
                break 
            except ValueError as e:
                print(f"{e} Tente novamente.")
                

    
    elif 12 <= personagem.atributos['percepcao'] <18:
     print('[bold purple]\033"Não sou vivo, mas cresço, \nNão tenho pulmões, mas respiro,\n Não tenho boca, mas devoro tudo."\033[0m[/bold purple]\n')
     texto22 = ('Alternativas: \nA) O fogo 🔥 \nB) A sombra 🌑 \nC) O tempo ⏳')
     digitar(texto22)
    
    elif personagem.atributos['percepcao'] <12:
        print('[bold purple]\033"Não tenho forma, nem sombra que me prenda,\n Sou a força que molda e que desvenda, \nEm silêncio corro, sem deixar vestígio, \nTransformo o sólido em poeira, \nE ainda que eu jamais seja tocado, \nSem mim, nada se move, nada existe."\033[0m[/bold purple]\n')
        texto23 = ('\nA) A essência do tempo ⏳ \nB) O sopro invisível do vento 🌬 \nC) O pensamento eterno 🧠')
        digitar(texto23)





def lore_4_andar(personagem):
    print()
    



if __name__ == "__main__":
    p = Personagem()
    lore_introducao(p)