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

usuarios = []
personagens = []
name_list = []
user = ''

class interface:
    def interface_principal():
        opcoes = {
            'Criar usuário': interface.interface_criacao,
            'Login' : interface.interface_login
        }
        os.system('clear')
        print(' Olá, seja bem vindo!')
        a = InquirerPy.inquirer.select(
            message='Escolha uma opção',
            choices=['Criar usuário', 'Login', 'Finalizar' ]
        ).execute()
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
        a = InquirerPy.inquirer.text(message='Digite o nome de usuário', validate= lambda x: x != '', invalid_message='O campo não pode estar vazio').execute()
        b = InquirerPy.inquirer.text(message='Digite a senha do usuário', validate= lambda x: x != '', invalid_message='O campo não pode estar vazio').execute()
        user.criar_user(str(a), utills.cripto(str(b)))
        usuarios.append(user)
        interface.save(usuarios, 'usuarios')
        input()
        interface.interface_principal()
    
    def interface_login():
        lista_username = []
        for i in usuarios:
            lista_username.append(i.username)
        a = InquirerPy.inquirer.text(message='Digite o nome de usuário:', validate= lambda x: x in lista_username, invalid_message='Usuário não encontrado').execute()
        b = InquirerPy.inquirer.text(message='Digite a senha do usuário:', validate= lambda x: x != '', invalid_message='O campo senha não pode estar vazio').execute()
        c = lista_username.index(a)
        if usuarios[c].password == utills.cripto(str(b)):
            print('Acesso liberado!')
            global user
            user = usuarios[c]
            load_caracter()
            input()
            interface.interface_usuário(user.username)
        else:
            print('Acesso negado!')
            input()
            interface.interface_principal()

    def criar_ficha():
        personagem = ficha.Personagem()
        personagem.criar_ficha()
        personagens.append(personagem)
        name_list.append(utills.cripto(personagem.nick))
        user.personagens = name_list
        interface.save(usuarios, 'usuarios')
        interface.save(personagens, 'personagem')
        interface.interface_usuário(user.username)

    def jogar():
        combate.tela_battle(personagens[0], personagens[1])
    
    def visualizar_ficha():
        a = []
        for i in personagens:
            a.append(i.nick)
        b = InquirerPy.inquirer.select(message='Qual o personagem desejado', choices= a).execute()
        c = a.index(b)
        personagens[c].visualizar()
        input()
        interface.interface_usuário(user.username)
    
    def logout():
        return

    def interface_usuário(user):
        os.system('clear')
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
            b = ficha.Personagem()
            b.nick = item['nick']
            b.raca = item['raca']
            b.classe = item['classe']
            b.xp = item['xp']
            b.nivel = item['nivel']
            b.atributos = item['atributos']
            b.pericias = item['pericias']
            b.inventario = item['inventario']
            b.historico = item['historico']
            b.status = item['status']
            personagens.append(b)
    except TypeError:
        pass

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

if __name__ == '__main__':
    load()
    interface.interface_principal()