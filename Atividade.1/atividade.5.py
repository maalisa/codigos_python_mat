# Programa para determinar o maior valor e sua posição em uma lista de N valores
N = int(input("Digite o número de valores: "))

maior_valor = float('-inf')
posicao_maior = -1

for i in range(N):
    valor = int(input(f"Digite o valor {i+1}: "))
    if valor > maior_valor:
        maior_valor = valor
        posicao_maior = i + 1

print(f"O maior valor é {maior_valor} e está na posição {posicao_maior}")
