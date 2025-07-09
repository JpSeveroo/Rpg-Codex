#Atribuir os personagens criados aos respectivos usuários
#Fazer com que seja possivel visualizar apenas os personagens criados pelos usuários
#Alteração de usuário no login
#Não permitir nomes iguais em personagens

import utills
import users
import os
import InquirerPy
import InquirerPy.inquirer
import ficha
import combate
import jogo1
from time import sleep

usuarios = []
personagens = []
personagens_usuario = []
name_list = []
user = ''
personagem_escolhido = ''

class interface:

    def interface_principal():
        opcoes = {
            'Criar usuário': interface.interface_criacao,
            'Login' : interface.interface_login
        }
        os.system('cls' if os.name == 'nt' else 'clear')
        print(' Olá, seja bem vindo!')

        a = InquirerPy.inquirer.select(
            message='Escolha uma opção',
            choices=['Criar usuário', 'Login', 'Finalizar' ]
        ).execute()

        if a == 'Finalizar':
            print('Encerrando o programa')
            return
        
        opcao = opcoes.get(a)
        if opcao:
            opcao()
 
    def save(info, path):
        lista = []
        for user in info:
            lista.append(user.__dict__)
        utills.salvar_infos(path, lista)

    def interface_criacao():
        user = users.users()
        nomes_existentes = [u.username for u in usuarios]
        a = InquirerPy.inquirer.text(message='Digite o nome de usuário', validate= lambda x: x != '' and x not in nomes_existentes, invalid_message='O campo não pode estar vazio ou o nome já existir').execute()    
        b = InquirerPy.inquirer.text(message='Digite a senha do usuário', validate= lambda x: x != '', invalid_message='O campo não pode estar vazio', is_password=True).execute()
        user.criar_user(str(a), utills.cripto(str(b)))
        usuarios.append(user)
        interface.save(usuarios, 'usuarios')
        sleep(1.0)
        interface.interface_principal()
    
    def interface_login():
        lista_username = []
        for i in usuarios:
            lista_username.append(i.username)
        a = InquirerPy.inquirer.text(message='Digite o nome de usuário:', validate= lambda x: x in lista_username, invalid_message='Usuário não encontrado').execute()
        b = InquirerPy.inquirer.text(message='Digite a senha do usuário:', validate= lambda x: x != '', invalid_message='O campo senha não pode estar vazio', is_password=True).execute()
        c = lista_username.index(a)
        if usuarios[c].password == utills.cripto(str(b)):
            print('Acesso liberado!')
            global user
            user = usuarios[c]
            load_pers_users(user.personagens)
            input('Pressione enter para seguir...')
            interface.interface_usuário(user.username)
        else:
            print('Acesso negado!')
            input('Pressione enter para voltar...')
            interface.interface_principal()

    def verify(personagem):
        c = False
        nomes = [item.nick for item in personagens]
        while c == False:
            if personagem.nick in nomes:
                print('O nome escolhido para o personagem não está disponível')
                personagem.nick = input('Digite outro nome: ')
            else:
                c = True

    def criar_ficha():
        personagem = ficha.Personagem()
        personagem.criar_ficha()
        interface.verify(personagem)
        personagens.append(personagem)
        personagens_usuario.append(personagem)
        name_list.append(utills.cripto(personagem.nick))
        user.personagens = name_list
        interface.save(usuarios, 'usuarios')
        interface.save(personagens, 'personagem')
        interface.interface_usuário(user.username)

    def jogar():
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            pers = [i.nick for i in personagens_usuario]
            pers.append('Sair')
            b = InquirerPy.inquirer.select(message='Qual o personagem desejado', choices= pers).execute()
            if b == 'Sair':
                sleep(0.5)
                interface.interface_usuário(user.username)
                return
            c = pers.index(b)
            global personagem_escolhido
            personagem_escolhido = personagens[c]
        except:
            print('Não há nenhum personagem criado!')
            input('Pressione qualquer tecla para voltar ao menu...')
            interface.interface_usuário(user.username)
            return
        jogo1.lore_1_andar(personagem_escolhido)
    
    def visualizar_ficha():
        a = []
        for i in personagens_usuario:
            a.append(i.nick)
        a.append('Sair')
        if len(a) > 1 :
            b = InquirerPy.inquirer.select(message='Qual o personagem desejado', choices= a).execute()
            if b == 'Sair':
                interface.interface_usuário(user.username)
                return
            c = a.index(b)
            personagens_usuario[c].visualizar()
        else :
            print(f'Não há personagens criados no usuário {user.username} \n')
        input('Pressione qualquer tecla para voltar...')
        interface.interface_usuário(user.username)
    
    def logout():
        a = InquirerPy.inquirer.confirm(message='Você deseja deslogar desse usuário ?').execute()
        global user
        global personagens_usuario
        global name_list
        if a == True:
            user = ''
            personagens_usuario = []
            name_list = []
            interface.interface_principal()
            sleep(0.5)
        else :
            interface.interface_usuário(user)
            sleep(0.5)

    def interface_usuário(user):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Seja bem vindo {user}')
        print()
        opcoes = {
            'Jogar': interface.jogar,
            'Criar Ficha': interface.criar_ficha,
            'Visualizar fichas': interface.visualizar_ficha,
            'Logout': interface.logout
        }
        a = InquirerPy.inquirer.select(
            message='Qual das opções você deseja ?',
            choices= ['Jogar', 'Criar Ficha', 'Visualizar fichas', 'Logout', 'Finalizar']
        ).execute()
        b = opcoes.get(a)
        if b:
            b()

def load_caracter():
    try:
        a = utills.load_infos('personagem')
        for item in a:
            name_list.append(utills.cripto(item['nick']))
            b = ficha.Personagem()
            b.nick = item['nick']
            b.raca = item['raca']
            b.classe = item['classe']
            b.xp = item['xp']
            b.nivel = item['nivel']
            b.xp_para_proximo_nivel = item['xp_para_proximo_nivel']
            b.atributos = item['atributos']
            b.pericias = item['pericias']
            b.inventario = item['inventario']
            b.fraquezas = item['fraquezas']
            b.status = item['status']
            b.vida_atual = item['vida_atual']
            b.equipamento = item['equipamento']
            b.andar_esfinge_completado = item['andar_esfinge_completado']
            b.andar_cupula_completado = item['andar_cupula_completado']
            b.checkpoint = item['checkpoint']
            personagens.append(b)
    except TypeError:
        pass

def load_pers_users(lista_pers):
    for i in personagens:
        if utills.cripto(i.nick) in lista_pers:
            personagens_usuario.append(i)

def load():
    try:
        a = utills.load_infos('usuarios')
        for item in a:
            b = users.users()
            b.criar_user(item['_username'], item['_password'])
            b.personagens = item['personagens']
            usuarios.append(b)
    except TypeError:
        pass

load_caracter()