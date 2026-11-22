from dataclasses import dataclass, field


@dataclass(eq=False)
class Usuario:
    username: str
    senha_hash: str = field(repr=False)
    personagens: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.username = self.username.strip()

        if not self.username:
            raise ValueError("O nome de usuário não pode estar vazio.")

        if not self.senha_hash:
            raise ValueError("O hash da senha não pode estar vazio.")
