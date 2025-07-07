import random
import time
import sys
import os
from InquirerPy import inquirer
import item

item.load_itens()
pocao_cura = item.lista_itens[0]
pocao_mana = item.lista_itens[1]

"""=== FUNÇÕES UTILITARIAS ==="""

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

""" === DANO E AÇÕES === """

#Precisa adaptar pra quando for colocar o sistema de pericia
def calc_dano(personagem, pericia_principal, bonus_extra=0, custo_mana=0):
    if personagem.status['mana'] >= custo_mana:    

        base = personagem.pericias.get(pericia_principal, 0)
        dado, critico = rolar_dado()
        dano_base = base + bonus_extra + dado
        if critico:
            dano = dano_base * 2
            digitar(f"🎲 {personagem.nick} rola 1d6: {dado} + bônus ({base} + {bonus_extra}) = {dano_base} 🎉 CRÍTICO! Dano dobrado para {dano}!")
        else:
            dano = dano_base
            digitar(f"🎲 {personagem.nick} rola 1d6: {dado} + bônus ({base} + {bonus_extra}) = {dano}")

        personagem.status['mana'] -= custo_mana
        if personagem.status['mana'] < 0:
            personagem.status['mana'] = 0
        return dano

    else:
        digitar(f"⚠️ {personagem.nick} não tem mana suficiente para atacar!")
        return 0

def ataque(atacante, defensor, pericia_principal):
    dano = calc_dano(atacante, pericia_principal, custo_mana=5)
    defensor.vida_atual -= dano
    if defensor.vida_atual < 0:
            defensor.vida_atual = 0
    digitar(f"\n⚔️  {atacante.nick} ataca {defensor.nick} causando {dano} de dano!")
    digitar(f"❤️  {defensor.nick} agora tem {defensor.vida_atual} HP.")
    time.sleep(0.8)

def ataque_especial(atacante, defensor, pericia_principal):
    custo_especial = 10
    
    if getattr(atacante, "is_player", True):
        pericia_extra = inquirer.select(
            message='Escolha uma perícia extra para o ataque especial:',
            choices=list(atacante.pericias.keys())
        ).execute()
    else:
        pericia_extra = max(
            atacante.pericias,
            key=lambda p: atacante.pericias[p],
            default=pericia_principal  # fallback caso só tenha uma
        )
        digitar(f"⚔️ {atacante.nick} usa a perícia extra '{pericia_extra}' no ataque especial!")
    
    if atacante.status['mana'] < custo_especial:
        digitar("⚠️ Mana insuficiente para ataque especial! Tente outra ação.")
        time.sleep(0.8)
        return False  # não conseguiu atacar
        
    # calculo de dano extra
    bonus_extra = atacante.pericias.get(pericia_extra, 0)

    dano = calc_dano(atacante, pericia_principal, bonus_extra, custo_mana=custo_especial)
    defensor.vida_atual -= dano
    if defensor.vida_atual < 0:
        defensor.vida_atual = 0

    digitar(f"\n⚔️  {atacante.nick} usa um ataque especial em {defensor.nick}! causando {dano} de dano!")
    digitar(f"❤️  {defensor.nick} agora tem {defensor.vida_atual} HP.")
    time.sleep(0.8)
    return True

#fazer o calculo de pericias do ataque especial

def esquivar(personagem, mana_max):
    acrobacia = personagem.pericias.get('acrobacia', 0)
    dado = random.randint(1, 20)
    total = dado + acrobacia
    digitar(f"🤸 {personagem.nick} tenta se esquivar! Rolagem: {dado} + Acrobacia ({acrobacia}) = {total}")
    time.sleep(0.8)
    
    if total >= 12: # Sucesso na esquiva
        recuperado = 3
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

def acoes(valor, personagem, inimigo, mana_max):
    if valor == 'Corpo a Corpo':
        ataque(personagem, inimigo, 'mano a mano')
        return True
    elif valor == 'Longo Alcance':
        ataque(personagem, inimigo, 'mira')
        return True
    elif valor == 'Ataque Especial Corpo a Corpo':
        return ataque_especial(personagem, inimigo, 'mano a mano')
    elif valor == 'Ataque Especial Longo Alcance':
        return ataque_especial(personagem, inimigo, 'mira')
    elif valor == 'Inventário':
        inv(personagem, mana_max)
        return True
    elif valor == 'Esquivar':
        return esquivar(personagem, mana_max)
    return False  # ação inválida ou não reconhecida

"""=== PARTE VISUAL ==="""

def barra(life):
        hp_max = life.status.get('hp', 1)
        if hp_max == 0:
            hp_max = 1
        preenchido = int((life.vida_atual/hp_max)*10)
        vazio = 10 - preenchido 
        return ('#' * preenchido) + ('-' * vazio)

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
def loop_principal(personagem, inimigo, mana_max, mana_max_inimigo):
    limpar_tela()
    acoes_inimigo = {
    1: 'Corpo a Corpo',
    2: 'Longo Alcance',
    3: 'Ataque Especial Corpo a Corpo',
    4: 'Ataque Especial Longo Alcance'
}
    tabelas(personagem, inimigo)
    print()

    while True:
        a = inquirer.select(
            message='Qual a sua próxima ação:',

            choices=['Corpo a Corpo', 'Longo Alcance', 'Ataque Especial Corpo a Corpo', 'Ataque Especial Longo Alcance', 'Inventário', 'Esquivar']
        ).execute()

        if personagem.vida_atual <= 0:
            return #personagem morreu
        
        if a == 'Esquivar':
            sucesso = esquivar(personagem, mana_max)
            if sucesso:
                digitar("Você pode agir novamente após esquivar!")
                time.sleep(0.8)
                continue # volta para escolha de ação
            else:
                digitar("Você falhou na esquiva e perdeu seu turno!")
                time.sleep(0.8)
                break #perdeu o turno
        
        sucesso = acoes(a, personagem, inimigo, mana_max)
        if sucesso:
            break
        else:
            digitar("⚠️ Ação inválida ou mana insuficiente. Escolha outra ação.")
            time.sleep(0.8)
    
    if inimigo.vida_atual > 0: #turno da IA
        if inimigo.status['mana'] >= 10:
            b = random.randint(1, 4)  # pode usar qualquer ataque
            acao_ia = acoes_inimigo.get(b)
        elif inimigo.status['mana'] >= 5:
            b = random.randint(1, 2) # só ataques corpo a corpo ou longo alcance
            acao_ia = acoes_inimigo.get(b)
        else:
            acao_ia = 'Esquivar'

        if acao_ia == 'Esquivar':
            sucesso = esquivar(inimigo, mana_max_inimigo)
            if not sucesso:
                return
            else:
                if inimigo.status['mana'] >= 10:
                    b = random.randint(1, 4)
                    acao_ia = acoes_inimigo.get(b)
                elif inimigo.status['mana'] >= 5:
                    b = random.randint(1, 2)
                    acao_ia = acoes_inimigo.get(b)

        acoes(acao_ia, inimigo, personagem, mana_max_inimigo)


def combate(p1, p2):
    digitar(f"\n🛡️  Combate iniciado entre {p1.nick} e {p2.nick}!")
    time.sleep(0.8)
    mana_max1 = p1.status['mana']
    mana_max2 = p2.status['mana']
    while p1.vida_atual > 0 and p2.vida_atual > 0:
        loop_principal(p1, p2, mana_max1, mana_max2)
    
    if p1.vida_atual > 0:
        digitar(f"\n🏆 {p1.nick} venceu o combate!")
        time.sleep(1.5)
        limpar_tela()
        return p1
    elif p2.vida_atual > 0:
        digitar(f"\n🏆 {p2.nick} venceu o combate!")
        time.sleep(1.5)
        limpar_tela()
        return p2
     
"""=== EXEMPLO DE EXECUÇÃO ==="""

if __name__ == '__main__':
    from ficha import Personagem

    pocao_cura.qtd = 2
    pocao_mana.qtd = 2

    p1 = Personagem()
    p1.nick = "Artemis"
    p1.atributos["força"] = 6
    p1.status["hp"] = 100
    p1.status["mana"] = 100
    p1.pericias['mano a mano'] = 12
    p1.pericias['mira'] = 8   
    p1.pericias['acrobacia'] = 5 
    p1.vida_atual = 100
    p1.inventario.append(pocao_cura)
    p1.inventario.append(pocao_mana)
    p1.is_player = True

    p2 = Personagem()
    p2.nick = "Gorak"
    p2.atributos["força"] = 8
    p2.status["hp"] = 100
    p2.status["mana"] = 100
    p2.pericias['mano a mano'] = 12
    p2.pericias['mira'] = 6
    p2.pericias['acrobacia'] = 3
    p2.vida_atual = 100
    p2.is_player = False

    combate(p1, p2)