import time
from ficha import Personagem
import sys
from rich import print

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
    texto3 = (' Você não é um ser físico, mas um Eco — uma consciência fragmentada, arrancada do mundo original pela Queda do Éter, um cataclismo que destruiu a linha entre a matéria e a energia, a vida e o código. Etherion é um santuário e uma prisão: aqui, a essência das raças ancestrais — humanos, elfos, draconianos — se fundiu e se perdeu, reciclada em uma tapeçaria digital onde magia e tecnologia são indistintas. Este não é um mundo de certezas, mas de possibilidades codificadas. Cada passo é um teste, cada sombra uma lembrança, cada inimigo um fragmento do passado e um desafio do presente. À sua frente, o Labirinto se estende como um abismo infinito, pulsando com segredos e armadilhas, guardando a verdade que pode libertá-lo — ou destruí-lo. Você pode: \n')
    digitar(texto3)

    texto4 = ('1. Avançar para o primeiro andar do Labirinto, assim, iniciando sua ascensão rumo à liberdade. \n2. Investigar inventário')
    digitar(texto4)

    while True:
        try:
            esc_1 = input("\nEscolha uma opção (1 ou 2): ").strip()
            if esc_1 not in ("1", "2"):
                raise ValueError("Opção inválida.")
            if esc_1 == "1":
                lore_1_andar(personagem)

            elif esc_1 == "2":
                # Aqui você exibe o inventário
                # Exemplo: personagem.exibir_inventario()
                print("Você abriu o inventário.") 
            break 
        except ValueError as e:
            print(f"{e} Tente novamente.")

def lore_1_andar(personagem):
    print()
    texto5 = 'Você atravessa o portal que o leva do vazio da planície para dentro do Labirinto. A luz muda, tornando-se mais fria e metálica. O chão abaixo é um mosaico de placas metálicas e circuitos pulsantes, estendendo-se até onde a vista alcança. O ar é pesado com uma energia estática, e a sensação de estar sendo observado é constante. À distância, silhuetas se movem entre os pilares de luz — 3 Gárgulas de Dados, sentinelas programadas para detectar e eliminar intrusos. Suas asas de metal rangem, e seus olhos brilham com uma luz vermelha ameaçadora. Uma voz sintética, reconhecida do terminal, ecoa no ambiente:\n'
    digitar(texto5)

    print(f"[bold purple][Sistema: “{personagem.nick}, prepare-se. O primeiro teste começou.”][bold purple]\n")

    texto6 = '1. Iniciar o combate — Enfrentar as Gárgulas de Dados com as habilidades que possui, aprendendo a dominar o sistema de turnos e a usar sua força para progredir. \n2. Investigar inventário'
    digitar(texto6)

    while True:
        try:
            esc_1 = input("\nEscolha uma opção (1 ou 2): ").strip()
            if esc_1 not in ("1", "2"):
                raise ValueError("Opção inválida.")
            if esc_1 == "1":
                lore_1_andar(personagem)

            elif esc_1 == "2":
                # Aqui você exibe o inventário
                # Exemplo: personagem.exibir_inventario()
                print("Você abriu o inventário.") 
            break 
        except ValueError as e:
            print(f"{e} Tente novamente.")


if __name__ == "__main__":
    p = Personagem()
    lore_introducao(p)