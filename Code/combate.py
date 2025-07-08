import random
import time
import sys
from InquirerPy import inquirer
import item
import utills
import ficha

pocao_cura = item.lista_itens[0]
pocao_mana = item.lista_itens[1]

"""=== FUNÇÕES UTILITARIAS ==="""

def digitar(texto, delay=0.03):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rolar_dado():
    dado = random.randint(1, 6)
    condicao = random.randint(1, 6)
    critico = False
    if condicao==dado: critico = True
    return dado, critico

""" === DANO E AÇÕES === """

#Precisa adaptar pra quando for colocar o sistema de pericia
def calc_dano(personagem, pericia_principal, bonus_extra=False): #FUNÇÃO OK
        base = (personagem.pericias.get(pericia_principal, 0))*2
        dado, critico = rolar_dado()
        dano_base = base - ((base//(dado+1))+2)
        dano = dano_base
        if bonus_extra:
            dano += dano_base//2
        if critico:
            dano += dano_base//2
            digitar(f"🎲 {personagem.nick} rola 1d6: {dado}; dano = {dano} 🎉 QUE SORTE, DEU CRÍTICO!")
        else:
            digitar(f"🎲 {personagem.nick} rola 1d6: {dado}; dano = {dano}")
        return dano

def _executar_ataque(atacante, defensor, pericia_principal, custo_mana, bonus_extra=False, pericia_secundaria=None):

    if atacante.status['mana'] < custo_mana:
        digitar('⚠️ Mana insuficiente! Tente outra ação.')
        time.sleep(1.5)
        return False
    
    atacante.status['mana'] -= custo_mana

    if pericia_secundaria:
        digitar(f'⚔️ {atacante.nick} usou a perícia {pericia_secundaria} no ataque especial!')
        if bonus_extra:
             digitar(f'🎯 A perícia escolhida ({pericia_secundaria}) é eficaz contra {defensor.nick}!')
        else:
             digitar(f'💨 A perícia escolhida ({pericia_secundaria}) não teve efeito')

    dano = calc_dano(atacante, pericia_principal, bonus_extra)

    defensor.vida_atual -= dano
    if defensor.vida_atual < 0:
        defensor.vida_atual = 0

    tipo_de_ataque = 'um ataque especial' if pericia_secundaria else 'ataca'
    digitar(f'\n⚔️  {atacante.nick} {tipo_de_ataque} em {defensor.nick}! causando {dano} de dano!')
    digitar(f'❤️  {defensor.nick} agora tem {defensor.vida_atual} HP.')
    time.sleep(2)
    return True

def ataque(atacante, defensor, pericia_principal):
    custo_mana = 5
    return _executar_ataque(atacante, defensor, pericia_principal, custo_mana)

def ataque_especial(atacante, defensor, pericia_principal, pericia_secundaria):
    custo_especial = 10
    
    acertou_fraqueza = pericia_secundaria in getattr(defensor, 'fraquezas', [])
    
    return _executar_ataque(atacante, defensor, pericia_principal, custo_especial, bonus_extra=acertou_fraqueza, pericia_secundaria=pericia_secundaria)

# fazer o calculo de pericias do ataque especial

def esquivar(personagem, mana_max):
    acrobacia = personagem.pericias.get('acrobacia', 0)
    dado = random.randint(1, 20)
    total = dado + acrobacia
    digitar(f"🤸 {personagem.nick} tenta se esquivar! Rolagem: {dado} + Acrobacia ({acrobacia}) = {total}")
    time.sleep(2)
    
    if total >= 15: # sucesso na esquiva
        recuperado = 3
        personagem.status['mana'] += recuperado
        if personagem.status['mana'] > mana_max:
            personagem.status['mana'] = mana_max
        digitar(f"✅ Esquiva bem-sucedida! Recuperou {recuperado} de mana.")
        time.sleep(2)
        return True
    else:
        digitar("❌ Esquiva falhou! Você se desequilibrou e perdeu a chance de recuperar energia.")
        time.sleep(2)
        return False

def acoes(valor, personagem, inimigo, mana_max):
    if isinstance(valor, tuple):
        tipo_acao, alcance, pericia = valor

        if tipo_acao == 'Ataque Especial':
            if alcance == 'Corpo a Corpo':
                return ataque_especial(personagem, inimigo, 'mano a mano', pericia)
            elif alcance == 'Longo Alcance':
                return ataque_especial(personagem, inimigo, 'mira', pericia)
            else:
                return False
    else:
        # valor é string simples
        if valor == 'Corpo a Corpo':
            return ataque(personagem, inimigo, 'mano a mano')
        elif valor == 'Longo Alcance':
            return ataque(personagem, inimigo, 'mira')
        elif valor == 'Inventário':
            inv(personagem, mana_max)
            return True
        elif valor == 'Esquivar':
            return esquivar(personagem, mana_max)
        else:
            return False

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
        print('|'+ f"Vida : {barra_a}  {a.vida_atual}/{a.status['hp']}".center(33) + '|' + ' '*25 + '|'+ f"Vida : {barra_b}  {b.vida_atual}/{b.status['hp']}".center(33) + '|')
    print('-'*35 + ' '*25 + '-'*35)
    write('Nome', personagem.nick, inimigo.nick)
    show_life(personagem, inimigo)
    write('Mana', personagem.status['mana'], inimigo.status['mana'])
    print('-'*35 + ' '*25 + '-'*35)

def inv(personagem, mana_max):
    lista_nome = [item.nome for item in personagem.inventario]
    print('-'*35)
    if len(lista_nome) != 0:
        a = inquirer.select(message='Itens no inventário: ', choices=lista_nome).execute()
        b = inquirer.confirm(message='Você deseja usar o item ?').execute()
        if b == True :
            num = lista_nome.index(a)
            if personagem.inventario[num].categoria == 'Utilizaveis':
                personagem.inventario[num].qtd -= 1
                efeitos = personagem.inventario[num].efeitos
                descricao = personagem.inventario[num].descricao
                for efeito in efeitos:
                    if efeito[0] == 'vida_atual':
                        personagem.vida_atual += efeito[1]
                        digitar(f"💊 {personagem.nick} recuperou {efeito[1]} de HP!")
                        if personagem.vida_atual > personagem.status['hp']:
                            personagem.vida_atual = personagem.status['hp']
                        digitar(descricao)
                        time.sleep(2)
                    else :
                        personagem.status[efeito[0]] += efeito[1]
                        digitar(descricao)
                        time.sleep(2)
                    if personagem.status['mana'] > mana_max:
                        personagem.status['mana'] = mana_max
            else :
                print('Este item não é um utilizavel!')
                input('Pressione enter para voltar...')
                inv(personagem, mana_max)
        else:
            pass
        print('-'*35)
    else :
        print('Não há itens no seu inventário!')
        print('-'*35)

#Interromper a luta quando o personagem ou inimigo morrer
def loop_principal(personagem, inimigo, mana_max):
    utills.limpar_tela()
    tabelas(personagem, inimigo)
    print()

    while True:
        a = inquirer.select(
            message='Qual a sua próxima ação:',

            choices=['Ataque', 'Ataque Especial', 'Inventário', 'Esquivar']
        ).execute()

        if personagem.vida_atual <= 0:
            print('Seu personagem foi reduzido a um amontoado de código.')
            return #personagem morreu
        
        if a == 'Ataque':
            a2 = inquirer.select(
                message='Qual a sua próxima ação:',

                choices=['Corpo a Corpo', 'Longo Alcance', 'Voltar']
            ).execute()
            if a2 == 'Voltar':
                continue
            valor_acao = a2

        elif a == 'Ataque Especial':
            a2 = inquirer.select(
                message='Qual a sua próxima ação:',
                choices=['Corpo a Corpo', 'Longo Alcance', 'Voltar']
            ).execute()
            if a2 == 'Voltar':
                continue
            a3 = inquirer.select(
                message='Escolha qual perícia vc quer usar para melhorar o ataque:',
                choices=['acrobacia', "blefar", "mira", "diplomacia", "furtividade", "percepção", "maos rapidas", "mano a mano", "resistencia", "Voltar"]
            ).execute()
            if a3 == 'Voltar':
                continue
            valor_acao = (a, a2, a3)

        elif a == 'Esquivar':
            sucesso = esquivar(personagem, mana_max)
            if sucesso:
                digitar("Você pode agir novamente após esquivar!")
                time.sleep(2)
                return # volta para escolha de ação
            else:
                digitar("Você falhou na esquiva e perdeu seu turno!")
                time.sleep(2)
                break #perdeu o turno
        
        elif a == 'Inventário':
            inv(personagem, mana_max)
            break

        else:
            valor_acao = a
        
        sucesso = acoes(valor_acao, personagem, inimigo, mana_max)
        if sucesso:
            break
        else:
            digitar("⚠️ Ação inválida ou mana insuficiente. Escolha outra ação.")
            time.sleep(2)
    
    if inimigo.vida_atual > 0: #turno da IA
        acao_ia = 'Corpo a Corpo'
        acoes(acao_ia, inimigo, personagem, 9999)

def combate(p1, p2):
    digitar(f"\n🛡️  Combate iniciado entre {p1.nick} e {p2.nick}!")
    time.sleep(2)
    mana_max1 = p1.status['mana']
    while p1.vida_atual > 0 and p2.vida_atual > 0:
        loop_principal(p1, p2, mana_max1)
    
    if p1.vida_atual > 0:
        digitar(f"\n🏆 {p1.nick} venceu o combate!")
        time.sleep(3)
        utills.limpar_tela()
        return p1
    elif p2.vida_atual > 0:
        digitar(f"\n🏆 {p2.nick} venceu o combate!")
        time.sleep(3)
        utills.limpar_tela()
        return p2

'''===FUNÇÕES INTERATIVAS DO COMBATE==='''


#função de caso o jogador não tenha uma arma de corpo a corpo e ou longa distancia

#função de puxar os inimigos da lista 

#função que relaciona os atributos da lista com as funções que gerenciam o "p2"

#ver como a gente vai relacionar os itens

def equip():
    #função que vai dizer se tem item de corpo a corpo ou longo alcance equipado
    #quando não tiver atacar com metade da pericia
    ...

def ene():
    #isso daqui eu vejo oq eu faço
    ...

def adv_IA():
    #IA dos inimigos
    ...

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
    p1.xp = 0
    p1.xp_para_proximo_nivel = 100
    p1.inventario.append(pocao_cura)
    p1.inventario.append(pocao_mana)
    p1.inventario.append(item.lista_itens[4])
    p1.is_player = True

    p2 = Personagem()
    p2.nick = "Gorak"
    p2.atributos["força"] = 8
    p2.status["hp"] = 100
    p2.status["mana"] = 100
    p2.pericias['mano a mano'] = 12
    p2.pericias['mira'] = 6
    p2.pericias['acrobacia'] = 3
    p2.vida_atual = 1
    p2.is_player = False
    p2.fraquezas = ['mano a mano']

    vencedor = combate(p1, p2)

    if vencedor == p1:
        xp_ganho = 100
        p1.xp += xp_ganho
        digitar(f"\n🎉 {p1.nick} ganhou {xp_ganho} de XP!")
        if p1.xp >= p1.xp_para_proximo_nivel:
            p1.evoluir_nivel()
    p1.visualizar()