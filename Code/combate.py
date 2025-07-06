from os import system
from InquirerPy import inquirer
from time import sleep
from rich.console import Console

def main_battle(personagem, inimigo):
    tabelas(personagem, inimigo)
    print()
    a = inquirer.select(message='O que você deseja fazer :', choices=['Atacar', 'Defender', 'Inventário', 'Fugir']).execute()
    return a

def tabelas(personagem, inimigo):
    print('-'*35 + ' '*35 + '-'*35)
    print('|' + f'{personagem.nick}'.center(33) + '|')
    return inimigo
    
def attack():
    return

def tela_battle(personagem, inimigo):
    system('clear')
    print(f'Você se deparou com {inimigo.nick}')
    sleep(1.0)
    system('clear')
    a = main_battle(personagem, inimigo)
    if a == 'Atacar':
        attack()
    input()


if __name__ == '__main__':
    tabelas()