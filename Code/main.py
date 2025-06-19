#Atribuir os personagens criados aos respectivos usuários
#Interface de login
#Interface de interação com o usuário -> depois do login
#Alteração de usuário no login
import utills

usuarios = []

def interface():
    a = int(input())
    if a == 1 :
        user = users()
        user.criar_user()
        usuarios.append(user)
        users.save()
        interface()
    if a == 2:
        users.login_user(usuarios)
        interface()
    if a == 3:
        input()

class users:
    def __init__(self):
        self._username = ''
        self._password = ''
        self.personagens = []
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, dado):
        self._username = dado

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, dado):
        self._password = dado

    def save():
        lista = []
        for user in usuarios:
            lista.append(user.__dict__)
        utills.salvar_infos('usuarios', lista)

    def criar_user(self):
        print('digite o nome do usuário : ')
        a = input()
        print('Digite a senha do usuário: ')
        b = input()
        self._username = a
        self._password = b

    def login_user(users):
        b = input('Digite o username: ')
        lista_username = []
        def senha():
            c = input('Digite a senha do usuário:')
            if usuarios[a].password == c:
                print('Acesso liberado')
            else :
                print('Senha incorreta')
                senha()
        for i in usuarios:
            lista_username.append(i.username)
        try:
            a = lista_username.index(b)
            senha()
        except ValueError:
            print('Usuário não encontrado')
            interface()

def load():
    a = utills.load_infos('usuarios')
    for item in a:
        b = users()
        b.username = item['_username']
        b.password = item['_password']
        usuarios.append(b)

if __name__ == '__main__':
    load()
    interface()