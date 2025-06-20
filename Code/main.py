#Atribuir os personagens criados aos respectivos usuários
#Interface de login
#Interface de interação com o usuário -> depois do login
#Alteração de usuário no login
import utills
import users
import os
import InquirerPy
import InquirerPy.inquirer

usuarios = []

class interface:
    def interface_principal():
        opcoes = {
            'Criar usuário': interface.interface_criacao,
            'Login' : interface.interface_login
        }
        os.system('clear')
        print('Olá, seja bem vindo!')
        a = InquirerPy.inquirer.select(
            message='Escolha uma opção',
            choices=['Criar usuário', 'Login', 'Finalizar' ]
        ).execute()
        opcao = opcoes.get(a)
        if opcao:
            opcao()

    def save():
        lista = []
        for user in usuarios:
            lista.append(user.__dict__)
        utills.salvar_infos('usuarios', lista)

    def interface_criacao():
        user = users.users()
        a = InquirerPy.inquirer.text(message='Digite o nome de usuário', validate= lambda x: x != '', invalid_message='O campo não pode estar vazio').execute()
        b = InquirerPy.inquirer.text(message='Digite a senha do usuário', validate= lambda x: x != '', invalid_message='O campo não pode estar vazio').execute()
        user.criar_user(str(a), utills.cripto(str(b)))
        usuarios.append(user)
        interface.save()
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
            input()
            interface.interface_usuário(usuarios[c].username)
        else:
            print('Acesso negado!')
            input()
            interface.interface_principal()

    def criar_ficha():
        return

    def jogar():
        return
    
    def visualizar_ficha():
        return
    
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

def load():
    try:
        a = utills.load_infos('usuarios')
        for item in a:
            b = users.users()
            b.criar_user(item['_username'], item['_password'])
            usuarios.append(b)
    except TypeError:
        pass

if __name__ == '__main__':
    load()
    interface.interface_principal()
