import random
import time
import sys
import os
from InquirerPy import inquirer
import item

item.load_itens()
pocao_cura = item.lista_itens[0]
pocao_mana = item.lista_itens[1]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


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
def rolar_dano(personagem, pericia_principal, bonus_extra=0):
    base = personagem.pericias.get(pericia_principal, 0)
    dado, critico = rolar_dado()
    dano_base = base + bonus_extra + dado
    if critico:
        dano = dano_base * 2
        digitar(f"🎲 {personagem.nick} rola 1d6: {dado} + bônus ({base} + {bonus_extra}) = {dano_base} 🎉 CRÍTICO! Dano dobrado para {dano}!")
    else:
        dano = dano_base
        digitar(f"🎲 {personagem.nick} rola 1d6: {dado} + bônus ({base} + {bonus_extra}) = {dano}")
    return dano

def ataque_especial(atacante, defensor, pericia_principal):
    if atacante.status['mana'] > 0:
        # Escolher perícia extra
        pericias_disponiveis = list(atacante.pericias.keys())
        pericias_disponiveis.remove(pericia_principal)
        pericia_extra = inquirer.select(message='Escolha uma perícia extra para o ataque especial:', choices=pericias_disponiveis).execute()
        bonus_extra = atacante.pericias.get(pericia_extra, 0)
        dano = rolar_dano(atacante, pericia_principal, bonus_extra)
        defensor.vida_atual -= dano
        if defensor.vida_atual < 0:
            defensor.vida_atual = 0
        digitar(f"\n⚔️  {atacante.nick} usa um ataque especial em {defensor.nick}! causando {dano} de dano!")
        digitar(f"❤️  {defensor.nick} agora tem {defensor.vida_atual} HP.")
        atacante.status['mana'] -= 5
        time.sleep(0.8)
    else:
        print('⚠️ Mana insuficiente para ataque especial!')
        time.sleep(0.8)


def turno_ataque(atacante, defensor, pericia_principal):
    dano = rolar_dano(atacante, pericia_principal)
    defensor.vida_atual -= dano
    if defensor.vida_atual < 0:
            defensor.vida_atual = 0
    digitar(f"\n⚔️  {atacante.nick} ataca {defensor.nick} causando {dano} de dano!")
    digitar(f"❤️  {defensor.nick} agora tem {defensor.vida_atual} HP.")
    time.sleep(0.8)


def esquivar(personagem, mana_max):
    acrobacia = personagem.pericias.get('acrobacia', 0)
    dado = random.randint(1, 6)
    total = dado + acrobacia
    digitar(f"🤸 {personagem.nick} tenta se esquivar! Rolagem: {dado} + Acrobacia ({acrobacia}) = {total}")
    time.sleep(0.8)
    
    if total >= 4:
        recuperado = 5
        personagem.status['mana'] += recuperado
        if personagem.status['mana'] > mana_max:
            personagem.status['mana'] = mana_max
        digitar(f"✅ Esquiva bem-sucedida! Recuperou {recuperado} de mana.")
        time.sleep(0.8)
        return True
    else:
        digitar("❌ Esquiva falhou! Você se desequilibrou e perdeu a chance de recuperar energia.")
        time.sleep(0.8)
        return False



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
    if valor == 'Corpo a Corpo':
        turno_ataque(personagem, inimigo, 'mano a mano')
    elif valor == 'Longo Alcance':
        turno_ataque(personagem, inimigo, 'mira')
    elif valor == 'Ataque Especial Corpo a Corpo':
        ataque_especial(personagem, inimigo, 'mano a mano')
    elif valor == 'Ataque Especial Longo Alcance':
        ataque_especial(personagem, inimigo, 'mira')
    elif valor == 'Inventário':
        inv(personagem, mana_max)
    elif valor == 'Esquivar':
        esquivar(personagem, mana_max)

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
                    time.sleep(0.8)
                else :
                    personagem.status[efeito[0]] += efeito[1]
                    digitar(descricao)
                    time.sleep(0.8)
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
    limpar_tela()
    acoes_inimigo = {1:'Atacar', 2:'Ataque Especial'}
    tabelas(personagem, inimigo)
    print()

    a = inquirer.select(
        message='Qual a sua próxima ação:',
        choices=['Corpo a Corpo', 'Longo Alcance', 'Ataque Especial Corpo a Corpo', 'Ataque Especial Longo Alcance', 'Inventário', 'Esquivar', 'Fugir']
    ).execute()

    inimigo_deve_agir = True

    if personagem.vida_atual > 0:
        #turno do jogador
        if a == 'Esquivar':
            sucesso = esquivar(personagem, mana_max)
            if sucesso:
                inimigo_deve_agir = False
        else:
            acoes(a, personagem, inimigo, mana_max)

    
    if inimigo.vida_atual > 0 and inimigo_deve_agir:
        #turno da IA
        if inimigo.status['mana'] > 0 :
            b = random.randint(1, 2)
            b = acoes_inimigo.get(b)
        else:
            b = 'Corpo a Corpo'
        acoes(b, inimigo, personagem, 0)


def combate(p1, p2):
    digitar(f"\n🛡️  Combate iniciado entre {p1.nick} e {p2.nick}!")
    time.sleep(0.8)
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
    p1.vida_atual = 100
    p1.inventario.append(pocao_cura)
    p1.inventario.append(pocao_mana)

    p2 = Personagem()
    p2.nick = "Gorak"
    p2.atributos["força"] = 8
    p2.status["hp"] = 50
    p2.status["mana"] = 5
    p1.pericias['mano a mano'] = 12
    p2.vida_atual = 100

    combate(p1, p2)

    #vencedor = combate(p1, p2)
    #print(f"\n🔥 Vencedor: {vencedor.nick}")