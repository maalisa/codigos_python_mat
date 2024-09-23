import time

def cronometro(segundos):
    for i in range(1, segundos + 1):
        print(i, end='... ')
        time.sleep(1)
    print("Fim!")

# Entrada do usuário
tempo = int(input("Tempo em segundos: "))
cronometro(tempo)
