import random
import time
import sys
from InquirerPy import inquirer
import item
import utills
import ficha
import inimigos
import inventario

"""=== FUNÇÕES UTILITARIAS ==="""


pocao_cura = item.lista_itens[0]
pocao_mana = item.lista_itens[1]

def get_nome(personagem):
    if type(personagem) == ficha.Personagem:
        return personagem.nick
    elif type(personagem) == inimigos.Inimigo:
        return personagem.nome

def rolar_dado():
    dado = random.randint(1, 6)
    condicao = random.randint(1, 6)
    critico = False
    if condicao==dado: critico = True
    return dado, critico

""" === DANO E AÇÕES === """

#Precisa adaptar pra quando for colocar o sistema de pericia
def calc_dano(personagem, pericia_principal, bonus_extra=False): #FUNÇÃO OK    
        multiplicador = equip(personagem, pericia_principal)
        base = int((personagem.pericias.get(pericia_principal, 0)) * 2 * multiplicador)
        dado, critico = rolar_dado()
        dano_base = base - ((base//(dado+1))+2)
        dano = dano_base
        if bonus_extra:
            dano += dano_base//2
        if critico:
            dano += dano_base//2
            utills.digitar(f"🎲 {personagem.nick} rola 1d6: {dado}; dano = {dano} 🎉 QUE SORTE, DEU CRÍTICO!")
        else:
            utills.digitar(f"🎲 {personagem.nick} rola 1d6: {dado}; dano = {dano}")
        return dano

def _executar_ataque(atacante, defensor, pericia_principal, custo_mana, bonus_extra=False, pericia_secundaria=None):

    if atacante.status['mana'] < custo_mana:
        utills.digitar('⚠️ Mana insuficiente! Tente outra ação.')
        time.sleep(1.5)
        return False
    

    atacante.status['mana'] -= custo_mana

    if pericia_secundaria:
        utills.digitar(f'⚔️ {atacante.nick} usou a perícia {pericia_secundaria} no ataque especial!')
        if bonus_extra:
             utills.digitar(f'🎯 A perícia escolhida ({pericia_secundaria}) é eficaz contra {defensor.nome}!')
        else:
             utills.digitar(f'💨 A perícia escolhida ({pericia_secundaria}) não teve efeito')

    dano = calc_dano(atacante, pericia_principal, bonus_extra)

    if atacante == inimigos:
        dano-= (defensor.pericias.get('resistencia', 0))//4

    defensor.vida_atual -= dano
    if defensor.vida_atual < 0:
        defensor.vida_atual = 0

    tipo_de_ataque = 'um ataque especial' if pericia_secundaria else 'ataca'
    utills.digitar(f'\n⚔️  {get_nome(atacante)} fez um {tipo_de_ataque} em {get_nome(defensor)}! causando {dano} de dano!')
    utills.digitar(f'❤️  {get_nome(defensor)} agora tem {defensor.vida_atual} HP.')
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
    utills.digitar(f"🤸 {personagem.nick} tenta se esquivar! Rolagem: {dado} + Acrobacia: ({acrobacia}) = {total}")
    time.sleep(2)
    
    if total >= 15: # sucesso na esquiva
        recuperado = 5
        personagem.status['mana'] += recuperado
        if personagem.status['mana'] > mana_max:
            personagem.status['mana'] = mana_max
        utills.digitar(f"✅ Esquiva bem-sucedida! você recuperou {recuperado} de mana.")
        time.sleep(2)
        return True
    else:
        utills.digitar("❌ Esquiva falhou! Você não foi agil o suficiente e nem conseguiu recuperar mana.")
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

    def write2(info, info1, info2, info3):
        print('|'+ f'{info} : {info2}'.center(33) + '|' + ' '*25 + '|'+ f'{info1} : {info3}'.center(33) + '|')

    def show_life(a, b):
        barra_a = barra(a)
        barra_b = barra(b)
        print('|'+ f"Vida : {barra_a}  {a.vida_atual}/{a.status['hp']}".center(33) + '|' + ' '*25 + '|'+ f"Vida : {barra_b}  {b.vida_atual}/{b.status['hp']}".center(33) + '|')
    print('-'*35 + ' '*25 + '-'*35)
    write('Nome', get_nome(personagem), get_nome(inimigo))
    show_life(personagem, inimigo)
    write2('Mana', 'Poder', personagem.status['mana'], inimigo.dano)
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
                        utills.digitar(f"💊 {personagem.nick} recuperou {efeito[1]} de HP!")
                        if personagem.vida_atual > personagem.status['hp']:
                            personagem.vida_atual = personagem.status['hp']
                        utills.digitar(descricao)
                        time.sleep(2)
                    else :
                        personagem.status[efeito[0]] += efeito[1]
                        utills.digitar(descricao)
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
        
        elif a == 'Inventário':
            inv(personagem, mana_max)
            break

        else:
            valor_acao = a
        
        sucesso = acoes(valor_acao, personagem, inimigo, mana_max)
        if sucesso:
            break
        else:
            utills.digitar("⚠️ Ação inválida ou mana insuficiente. Escolha outra ação.")
            time.sleep(2)
    
    if inimigo.vida_atual > 0: #turno da IA
        adv_IA(inimigo, personagem)


def combate(personagem, inimigo):

    personagem.vida_atual = personagem.vida_atual if personagem.vida_atual > 0 else personagem.status.get('hp', 100)
    personagem.status['mana'] = personagem.status.get('mana', 100) if personagem.status.get('mana', None) is not None else 100

    inimigo.vida_atual = inimigo.vida
    inimigo.status['mana'] = inimigo.status.get('mana', 100) if inimigo.status.get('mana', None) is not None else 100

    print(f"\n⚔️ Começando combate: {get_nome(personagem)} VS {get_nome(inimigo)}!\n")
    time.sleep(2)

    while personagem.vida_atual > 0 and inimigo.vida_atual > 0:
        loop_principal(personagem, inimigo, 100)

    if personagem.vida_atual > 0:
        utills.digitar(f"\n🏆 {personagem.nick} venceu o combate!")
        xp(personagem, inimigo)
        time.sleep(3)
        utills.limpar_tela()
        return personagem
    elif inimigo.vida_atual > 0:
        utills.digitar(f"\n💀 {personagem.nick} foi derrotado na torre...")
        time.sleep(3)
        utills.limpar_tela()
        return inimigo

'''===FUNÇÕES INTERATIVAS DO COMBATE==='''

def equip(personagem, pericia_principal):

    if not hasattr(personagem, 'equipamento'):
        return 1

    arma = inventario.equipamento.itens['Mãos']['equipado']
    pericias_que_exigem_arma = {'mano a mano', 'mira'}
    if pericia_principal not in pericias_que_exigem_arma:
        return 1
    if arma is False:
        return 0.5
    else:
        return 1

def xp(personagem, inimigo):
    xp_ganho = inimigo.xp
    personagem.xp += xp_ganho
    utills.digitar(f'Você ganhou {xp_ganho} de xp')

def adv_IA(inimigo, jogador):

    ataque(inimigo, jogador, 'mano a mano')

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
    p1.pericias['mano a mano'] = 40
    p1.pericias['mira'] = 8   
    p1.pericias['acrobacia'] = 5 
    p1.vida_atual = 100
    p1.xp = 0
    p1.xp_para_proximo_nivel = 100
    p1.equipamento = {
        "maos": item.lista_itens[2],  # Arma corpo a corpo
    }
    p1.inventario.append(pocao_cura)
    p1.inventario.append(pocao_mana)
    p1.inventario.append(item.lista_itens[4])
    p1.is_player = True

    inimigo = inimigos.lista_inimigos[0]

    vencedor = combate(p1, inimigo)
