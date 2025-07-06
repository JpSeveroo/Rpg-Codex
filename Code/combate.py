import random
import time
import sys

def digitar(texto, delay=0.03):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rolar_dano(personagem):
    base = personagem.atributos["força"]
    dado = random.randint(1, 6)
    return base + dado

def turno(atacante, defensor):
    dano = rolar_dano(atacante)
    defensor.status["hp"] -= dano
    if defensor.status["hp"] < 0:
        defensor.status["hp"] = 0
    digitar(f"\n⚔️  {atacante.nick} ataca {defensor.nick} causando {dano} de dano!")
    digitar(f"❤️  {defensor.nick} agora tem {defensor.status['hp']} HP.")

def combate(p1, p2):
    digitar(f"\n🛡️  Combate iniciado entre {p1.nick} e {p2.nick}!")
    turno_atual = 0
    while p1.status["hp"] > 0 and p2.status["hp"] > 0:
        atacante = p1 if turno_atual % 2 == 0 else p2
        defensor = p2 if turno_atual % 2 == 0 else p1
        turno(atacante, defensor)
        if defensor.status["hp"] <= 0:
            digitar(f"\n🏆 {atacante.nick} venceu o combate!")
            return atacante
        turno_atual += 1
        time.sleep(1.5)

# Exemplo de execução direta

if __name__ == '__main__':
    from ficha import Personagem

    p1 = Personagem()
    p1.nick = "Artemis"
    p1.atributos["força"] = 6
    p1.status["hp"] = 50

    p2 = Personagem()
    p2.nick = "Gorak"
    p2.atributos["força"] = 8
    p2.status["hp"] = 50

    vencedor = combate(p1, p2)
    print(f"\n🔥 Vencedor: {vencedor.nick}")
