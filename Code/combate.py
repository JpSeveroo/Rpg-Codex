from os import system
from InquirerPy import inquirer
from time import sleep
from rich.console import Console

def main_battle(personagem, inimigo):
    max_life = 20
    #proporção_inimigo = max_life/inimigo.status['hp']
    #proporção_pers = max_life/personagem.status['hp']
    barra = '█'*max_life
    print(f'{personagem.nick}'.ljust(20) + '|' + f'{personagem.status['hp']} {barra}'.ljust(20) + '|')
    print(f'{inimigo.nick}'.ljust(20) + '|' + f'{inimigo.status['hp']} {barra}'.ljust(20) + '|')
    print()
    a = inquirer.select(message='O que você deseja fazer :', choices=['Atacar', 'Defender', 'Inventário', 'Fugir']).execute()
    return a

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