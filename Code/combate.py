import random
import time
import sys
from os import system
from InquirerPy import inquirer
import item

item.load_itens()
pocao_cura = item.lista_itens[0]
pocao_mana = item.lista_itens[1]

def digitar(texto, delay=0.03):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#Precisa adaptar pra quando for colocar o sistema de pericia
def rolar_dano(personagem, pericia):
    base = personagem.atributos[pericia]
    dado = random.randint(1, 6)
    return base + dado

def turno_ataque(atacante, defensor):
    dano = rolar_dano(atacante, 'força')
    defensor.vida_atual -= dano
    if defensor.vida_atual < 0:
            defensor.vida_atual = 0
    digitar(f"\n⚔️  {atacante.nick} ataca {defensor.nick} causando {dano} de dano!")
    digitar(f"❤️  {defensor.nick} agora tem {defensor.vida_atual} HP.")

def barra(life):
        preenchido = int((life.vida_atual/life.status['hp'])*10)
        vazio = 10 - preenchido 
        barra_de_life = ('#' * preenchido) + ('-' * vazio)
        return barra_de_life

def tabelas(personagem, inimigo):
    def write(info, info1, info2):
        print('|'+ f'{info} : {info1}'.center(33) + '|' + ' '*25 + '|'+ f'{info} : {info2}'.center(33) + '|')
    def show_life(a, b):
        barra_a = barra(a)
        barra_b = barra(b)
        print('|'+ f'Vida : {barra_a}  {a.vida_atual}/{a.status['hp']}'.center(33) + '|' + ' '*25 + '|'+ f'Vida : {barra_b}  {b.vida_atual}/{b.status['hp']}'.center(33) + '|')
    print('-'*35 + ' '*25 + '-'*35)
    write('Nome', personagem.nick, inimigo.nick)
    show_life(personagem, inimigo)
    write('Mana', personagem.status['mana'], inimigo.status['mana'])
    print('-'*35 + ' '*25 + '-'*35)

def ataque_especial(atacante, defensor, pericia):
    if atacante.status['mana'] > 0:
        dano = atacante.pericias[pericia] + rolar_dano(atacante, 'força')
        defensor.vida_atual -= dano
        if defensor.vida_atual < 0:
            defensor.vida_atual = 0
        digitar(f"\n⚔️  {atacante.nick} usa um ataque especial em {defensor.nick}! causando {dano} de dano!")
        digitar(f"❤️  {defensor.nick} agora tem {defensor.vida_atual} HP.")
        atacante.status['mana'] -= 5
        time.sleep(0.5)
    else:
        print('Mana insuficiente!')
        time.sleep(0.5)

def acoes(valor, personagem, inimigo):
    if valor == 'Atacar':
        turno_ataque(personagem, inimigo)
    elif valor == 'Ataque Especial':
        ataque_especial(personagem, inimigo, 'mano a mano')
    elif valor == 'Inventário':
        inv(personagem)

def inv(personagem):
    lista_nome = [item.nome for item in personagem.inventario]
    print('-'*35)
    a = inquirer.select(message='Itens no inventário', choices=lista_nome, show_cursor='*').execute()
    b = inquirer.confirm(message='Você deseja usar o item ?').execute()
    if b == True :
        num = lista_nome.index(a)
        personagem.inventario[num].qtd -= 1
        efeitos = personagem.inventario[num].efeitos
        for efeito in efeitos:
            if efeito[0] == 'vida_atual':
                personagem.vida_atual += efeito[1]
                if personagem.vida_atual > personagem.status['hp']:
                    personagem.vida_atual = personagem.status['hp']
            else :
                personagem.status[efeito[0]] += efeito[1]
    else:
        pass
    print('-'*35)
        
#Interromper a luta quando o personagem ou inimigo morrer

def loop_principal(personagem, inimigo):
    system('clear')
    acoes_inimigo = {1:'Atacar', 2:'Ataque Especial'}
    tabelas(personagem, inimigo)
    print()
    a = inquirer.select(message='Qual a sua próxima ação: ', choices=['Atacar', 'Ataque Especial', 'Inventário', 'Fugir']).execute()
    #turno jogador
    acoes(a, personagem, inimigo)
    #turno da IA
    if inimigo.status['mana'] > 0 :
        b = random.randint(1, 2)
        b = acoes_inimigo.get(b)
        acoes(b, inimigo, personagem)
    else:
        acoes('Atacar', inimigo, personagem)


def combate(p1, p2):
    digitar(f"\n🛡️  Combate iniciado entre {p1.nick} e {p2.nick}!")
    while p1.vida_atual > 0 and p2.vida_atual > 0:
        loop_principal(p1, p2)
        
     
# Exemplo de execução direta

if __name__ == '__main__':
    from ficha import Personagem

    pocao_cura.qtd = 2

    p1 = Personagem()
    p1.nick = "Artemis"
    p1.atributos["força"] = 6
    p1.status["hp"] = 50
    p1.status["mana"] = 30
    p1.pericias['mano a mano'] = 12
    p1.vida_atual = 50
    p1.inventario.append(pocao_cura)

    p2 = Personagem()
    p2.nick = "Gorak"
    p2.atributos["força"] = 8
    p2.status["hp"] = 50
    p2.status["mana"] = 5
    p1.pericias['mano a mano'] = 12
    p2.vida_atual = 50

    combate(p1, p2)

    #vencedor = combate(p1, p2)
    #print(f"\n🔥 Vencedor: {vencedor.nick}")
