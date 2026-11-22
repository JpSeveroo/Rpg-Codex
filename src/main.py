
from catalogos import carregar_catalogos
from interface import Interface, load


def main() -> None:
    carregar_catalogos()
    load()
    Interface.interface_principal()


if __name__ == "__main__":
    main()
