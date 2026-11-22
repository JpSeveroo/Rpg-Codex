
from InquirerPy import inquirer


def solicitar_cadastro(
    nomes_existentes: set[str],
) -> tuple[str, str]:
    username = inquirer.text(
        message="Digite o nome de usuário",
        validate=lambda nome: (
            bool(nome.strip())
            and nome.strip() not in nomes_existentes
        ),
        invalid_message=(
            "O campo não pode estar vazio "
            "ou o nome já existir"
        ),
    ).execute()

    senha = inquirer.text(
        message="Digite a senha do usuário",
        validate=lambda valor: valor != "",
        invalid_message="O campo não pode estar vazio",
        is_password=True,
    ).execute()

    return username.strip(), senha


def solicitar_login(
    nomes_existentes: set[str],
) -> tuple[str, str]:
    username = inquirer.text(
        message="Digite o nome de usuário:",
        validate=lambda nome: nome in nomes_existentes,
        invalid_message="Usuário não encontrado",
    ).execute()

    senha = inquirer.text(
        message="Digite a senha do usuário:",
        validate=lambda valor: valor != "",
        invalid_message=(
            "O campo senha não pode estar vazio"
        ),
        is_password=True,
    ).execute()

    return username, senha
