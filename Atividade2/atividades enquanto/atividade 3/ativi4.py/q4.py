import random

# Lista de palavras
palavras = ['leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 
            'hipopotamo', 'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 
            'pinguim', 'lobo']

# Embaralhar a lista de palavras
random.shuffle(palavras)

# Escolher uma palavra aleatória
palavra_escolhida = random.choice(palavras)
indice_correto = palavras.index(palavra_escolhida)

print("A lista de palavras foi embaralhada.")
print("Você deve adivinhar a posição da palavra escolhida.")
print("As posições vão de 0 a 14.")

tentativas = 3

while tentativas > 0:
    palpite = int(input(f"Qual é a posição da palavra '{palavra_escolhida}'? (Tentativas restantes: {tentativas}) "))
    
    if palpite == indice_correto:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1
        print(f"Você errou. Tente novamente! Tentativas restantes: {tentativas}")

if tentativas == 0:
    print(f"Você não acertou. A posição correta era {indice_correto}.")

# Exibir a lista embaralhada
print("Lista embaralhada de palavras:", palavras)
