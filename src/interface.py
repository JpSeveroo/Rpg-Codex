
from time import sleep

from InquirerPy import inquirer

from models.personagem import Personagem
from models.usuario import Usuario
from persistencia import (
    carregar_personagens,
    carregar_usuarios,
    salvar_personagens,
    salvar_usuarios,
)
from ui.autenticacao import solicitar_cadastro, solicitar_login
from ui.ficha import criar_personagem, mostrar_ficha
from utills import cripto, limpar_tela


usuarios: list[Usuario] = []
personagens: list[Personagem] = []
personagens_usuario: list[Personagem] = []

usuario_logado: Usuario | None = None
personagem_escolhido: Personagem | None = None


def load() -> None:
    usuarios[:] = carregar_usuarios()
    personagens[:] = carregar_personagens()
    personagens_usuario.clear()


def load_pers_users(lista_pers: list[str]) -> None:
    personagens_usuario[:] = [
        personagem
        for personagem in personagens
        if cripto(personagem.nick) in lista_pers
    ]


def _usuario_autenticado() -> Usuario:
    if usuario_logado is None:
        raise RuntimeError("Nenhum usuário está autenticado.")

    return usuario_logado


class Interface:
    @staticmethod
    def interface_principal() -> None:
        while True:
            limpar_tela()
            print(" Olá, seja bem vindo!")

            escolha = inquirer.select(
                message="Escolha uma opção",
                choices=["Criar usuário", "Login", "Finalizar"],
            ).execute()

            if escolha == "Finalizar":
                print("Encerrando o programa")
                return

            if escolha == "Criar usuário":
                Interface.interface_criacao()

            elif escolha == "Login":
                finalizar = Interface.interface_login()

                if finalizar:
                    return

    @staticmethod
    def interface_criacao() -> None:
        nomes_existentes = {
            usuario.username for usuario in usuarios
        }

        username, senha = solicitar_cadastro(nomes_existentes)

        novo_usuario = Usuario(
            username=username,
            senha_hash=cripto(senha),
        )

        usuarios.append(novo_usuario)
        salvar_usuarios(usuarios)

        sleep(1)

    @staticmethod
    def interface_login() -> bool:
        if not usuarios:
            print("Não há usuários cadastrados.")
            input("Pressione Enter para voltar...")
            return False

        nomes_existentes = {
            usuario.username for usuario in usuarios
        }

        username, senha = solicitar_login(nomes_existentes)

        usuario = next(
            (
                usuario
                for usuario in usuarios
                if usuario.username == username
            ),
            None,
        )

        if usuario is None or usuario.senha_hash != cripto(senha):
            print("Acesso negado!")
            input("Pressione Enter para voltar...")
            return False

        global usuario_logado
        usuario_logado = usuario

        load_pers_users(usuario.personagens)

        print("Acesso liberado!")
        input("Pressione Enter para seguir...")

        return Interface.interface_usuario(usuario.username)

    @staticmethod
    def criar_ficha() -> None:
        usuario = _usuario_autenticado()

        nomes_existentes = {
            personagem.nick for personagem in personagens
        }

        personagem = criar_personagem(nomes_existentes)

        personagens.append(personagem)
        personagens_usuario.append(personagem)

        usuario.personagens.append(cripto(personagem.nick))

        salvar_personagens(personagens)
        salvar_usuarios(usuarios)

    @staticmethod
    def jogar() -> None:
        if not personagens_usuario:
            print("Não há nenhum personagem criado!")
            input("Pressione Enter para voltar ao menu...")
            return

        limpar_tela()

        nomes = [
            personagem.nick
            for personagem in personagens_usuario
        ]

        escolha = inquirer.select(
            message="Qual o personagem desejado",
            choices=[*nomes, "Sair"],
        ).execute()

        if escolha == "Sair":
            sleep(0.5)
            return

        global personagem_escolhido
        personagem_escolhido = next(
            personagem
            for personagem in personagens_usuario
            if personagem.nick == escolha
        )

        # Importação adiada para evitar dependências circulares.
        from story.jogo1 import lore_introducao

        lore_introducao(personagem_escolhido)

    @staticmethod
    def visualizar_ficha() -> None:
        if not personagens_usuario:
            usuario = _usuario_autenticado()
            print(
                f"Não há personagens criados "
                f"no usuário {usuario.username}\n"
            )
            input("Pressione Enter para voltar...")
            return

        nomes = [
            personagem.nick
            for personagem in personagens_usuario
        ]

        escolha = inquirer.select(
            message="Qual o personagem desejado",
            choices=[*nomes, "Sair"],
        ).execute()

        if escolha == "Sair":
            return

        personagem = next(
            personagem
            for personagem in personagens_usuario
            if personagem.nick == escolha
        )

        mostrar_ficha(personagem)

        input("Pressione Enter para voltar...")

    @staticmethod
    def logout() -> bool:
        confirmar = inquirer.confirm(
            message="Você deseja deslogar desse usuário?"
        ).execute()

        if not confirmar:
            return False

        global usuario_logado, personagem_escolhido

        usuario_logado = None
        personagem_escolhido = None
        personagens_usuario.clear()

        sleep(0.5)
        return True

    @staticmethod
    def interface_usuario(username: str) -> bool:
        while True:
            limpar_tela()
            print(f"Seja bem vindo {username}")
            print()

            escolha = inquirer.select(
                message="Qual das opções você deseja?",
                choices=[
                    "Jogar",
                    "Criar Ficha",
                    "Visualizar fichas",
                    "Logout",
                    "Finalizar",
                ],
            ).execute()

            if escolha == "Finalizar":
                return True

            if escolha == "Jogar":
                Interface.jogar()

            elif escolha == "Criar Ficha":
                Interface.criar_ficha()

            elif escolha == "Visualizar fichas":
                Interface.visualizar_ficha()

            elif escolha == "Logout":
                if Interface.logout():
                    return False
