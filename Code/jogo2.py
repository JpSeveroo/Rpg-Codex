import time
from ficha import Personagem
import sys
import os
from rich import print
from item import lista_itens
import inventario
import jogo1

def lore_pos_5andar(personagem):
    texto1 = ('O corpo híbrido de Kairon, se contorce uma última vez antes de desintegrar em fragmentos de energia e dados flutuantes. Sua essência se despede em um último rugido metálico que ecoa até o vazio. A arena silenciosa parece respirar aliviada — ou talvez colapsar. As plataformas ao redor tremem, como se o próprio labirinto reconhecesse sua vitória. Do centro do campo de batalha, uma fenda vertical de luz pura se abre, revelando um corredor estreito e pulsante, revestido de códigos vivos em espirais azuladas. Você cambaleia, exausto, com sua ficha digital ainda em alerta vermelho. O silêncio agora é pesado, não mais opressor, mas carregado de significado. Você derrotou um guardião, um pilar da estrutura de Etherion… e há consequências por isso.')

    jogo1.digitar(texto1)

    print('[bold purple][Sistema]Boss eliminado com sucesso. Integridade do Andar 5 comprometida. Protocolo de restauração iniciado.\n[Sistema] Sua persistência é estatisticamente improvável… e perigosamente inspiradora.[/bold purple]')

    while True:
        try:
            time.sleep(1)
            texto2 = ("\nVocê pode:\n\n1. Avançar para o Andar 6\n2. Investigar inventário\n3. Conferir Atributos: ")
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

                    texto6 = ('Ao derrotar ou enganar as sentinelas, a estação inteira parece “desligar”. Um silêncio novo surge — não mais pesado, mas libertador. As luzes mudam para um tom azul suave. Um dos painéis centrais se ergue, revelando uma espiral de escadas virtuais em queda livre.')
                    jogo1.digitar(texto6)

                    lore_7_andar(personagem)
        except ValueError as e:
            print(f"{e} Tente novamente.")
            
def lore_7_andar(personagem):
    print()