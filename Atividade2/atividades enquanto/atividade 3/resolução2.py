import random

def jogar():
    escolhas = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
    computador = random.randint(1, 3)

    usuario = int(input("Escolha: 1 para Pedra, 2 para Papel, 3 para Tesoura: "))
    
    print(f"Você escolheu: {escolhas[usuario]}")
    print(f"Computador escolheu: {escolhas[computador]}")

    if usuario == computador:
        return "Empate!"
    elif (usuario == 1 and computador == 3) or (usuario == 2 and computador == 1) or (usuario == 3 and computador == 2):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

while True:
    resultado = jogar()
    print(resultado)
    if input("Deseja jogar novamente? (s/n): ").lower() != 's':
        break
