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

def rolar_dado():
    dado = random.randint(1, 6)
    critico = (dado == 6)
    return dado, critico

#Precisa adaptar pra quando for colocar o sistema de pericia
def rolar_dano(personagem, pericia):
    base = personagem.atributos[pericia]
    dado, critico = rolar_dado()
    dano_base = base + dado
    if critico:
        dano = (dado + base) * 2
        digitar(f"🎲 {personagem.nick} rola 1d6: {dado} + bônus ({base}) = {dado + base} 🎉 CRÍTICO! Dano dobrado para {dano}!")
    else:
        dano = dado + base
        digitar(f"🎲 {personagem.nick} rola 1d6: {dado} + bônus ({base}) = {dano}")
    return dano

def ataque_especial(atacante, defensor, pericia):
    if atacante.status['mana'] > 0:
        pericia_bonus = atacante.pericias[pericia]
        dado, critico = rolar_dado()
        dano_base = pericia_bonus + dado
        if critico:
            dano = dano_base * 2
            digitar(f"🎲 {atacante.nick} rola 1d6: {dado} + bônus ({pericia_bonus}) = {dado + pericia_bonus} 🎉 CRÍTICO! Dano dobrado para {dano}!")
        else:
            dano = dano_base
            digitar(f"🎲 {atacante.nick} rola 1d6: {dado} + bônus ({pericia_bonus}) = {dano}")
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


def turno_ataque(atacante, defensor):
    dano = rolar_dano(atacante, 'força')
    defensor.vida_atual -= dano
    if defensor.vida_atual < 0:
            defensor.vida_atual = 0
    digitar(f"\n⚔️  {atacante.nick} ataca {defensor.nick} causando {dano} de dano!")
    digitar(f"❤️  {defensor.nick} agora tem {defensor.vida_atual} HP.")
    time.sleep(0.5)

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

def acoes(valor, personagem, inimigo, mana_max):
    if valor == 'Atacar':
        turno_ataque(personagem, inimigo)
    elif valor == 'Ataque Especial':
        ataque_especial(personagem, inimigo, 'mano a mano')
    elif valor == 'Inventário':
        inv(personagem, mana_max)     

def inv(personagem, mana_max):
    lista_nome = [item.nome for item in personagem.inventario]
    print('-'*35)
    if len(lista_nome) != 0:
        a = inquirer.select(message='Itens no inventário', choices=lista_nome).execute()
        b = inquirer.confirm(message='Você deseja usar o item ?').execute()
        if b == True :
            num = lista_nome.index(a)
            personagem.inventario[num].qtd -= 1
            efeitos = personagem.inventario[num].efeitos
            descricao = personagem.inventario[num].descricao
            for efeito in efeitos:
                if efeito[0] == 'vida_atual':
                    personagem.vida_atual += efeito[1]
                    if personagem.vida_atual > personagem.status['hp']:
                        personagem.vida_atual = personagem.status['hp']
                    digitar(descricao)
                    time.sleep(0.5)
                else :
                    personagem.status[efeito[0]] += efeito[1]
                    digitar(descricao)
                    time.sleep(0.5)
                if personagem.status['mana'] > mana_max:
                    personagem.status['mana'] = mana_max
        else:
            pass
        print('-'*35)
    else :
        print('Não há itens no seu inventário!')
        print('-'*35)

#Interromper a luta quando o personagem ou inimigo morrer

def tentar_fugir(personagem):
    digitar(f"\n🏃 {personagem.nick} tenta fugir do combate!")
    dado = random.randint(1, 6)
    dificuldade = 4
    digitar(f"🎲 Rolagem de dado para fuga: {dado} (precisava tirar {dificuldade} ou mais)")
    if dado >= dificuldade:
        digitar("✅ Fuga bem-sucedida!")
        return True
    else:
        digitar("❌ A fuga falhou! O inimigo aproveita a abertura...")
        return False

def loop_principal(personagem, inimigo, mana_max):
    system('clear')
    acoes_inimigo = {1:'Atacar', 2:'Ataque Especial'}
    tabelas(personagem, inimigo)
    print()
    a = inquirer.select(message='Qual a sua próxima ação: ', choices=['Atacar', 'Ataque Especial', 'Inventário', 'Fugir']).execute()
    
    if personagem.vida_atual > 0:
    
        if a == 'Fugir':
            sucesso = tentar_fugir(personagem)
            if sucesso:
                return "fugiu"
        acoes(a, personagem, inimigo, mana_max) #turno jogador
    
    if inimigo.vida_atual > 0:
        #turno da IA
        if inimigo.status['mana'] > 0 :
            b = random.randint(1, 2)
            b = acoes_inimigo.get(b)
            acoes(b, inimigo, personagem, 0)
        else:
            acoes('Atacar', inimigo, personagem, 0)

def combate(p1, p2):
    digitar(f"\n🛡️  Combate iniciado entre {p1.nick} e {p2.nick}!")
    time.sleep(0.5)
    mana_max1 = p1.status['mana']
    while p1.vida_atual > 0 and p2.vida_atual > 0:
        resultado = loop_principal(p1, p2, mana_max1)
        if resultado == "fugiu":
            digitar(f"\n🏃 {p1.nick} conseguiu fugir do combate!")
            return p1
     
# Exemplo de execução direta

if __name__ == '__main__':
    from ficha import Personagem

    pocao_cura.qtd = 2
    pocao_mana.qtd = 2

    p1 = Personagem()
    p1.nick = "Artemis"
    p1.atributos["força"] = 6
    p1.status["hp"] = 50
    p1.status["mana"] = 30
    p1.pericias['mano a mano'] = 12
    p1.vida_atual = 50
    p1.inventario.append(pocao_cura)
    p1.inventario.append(pocao_mana)

    p2 = Personagem()
    p2.nick = "Gorak"
    p2.atributos["força"] = 8
    p2.status["hp"] = 50
    p2.status["mana"] = 5
    p2.pericias['mano a mano'] = 12
    p2.vida_atual = 50

    combate(p1, p2)

    #vencedor = combate(p1, p2)
    #print(f"\n🔥 Vencedor: {vencedor.nick}")