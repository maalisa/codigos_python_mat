# Programa para calcular a soma e a média aritmética dos valores pares entre 50 e 70
soma = 0
contador = 0

for numero in range(50, 71):
    if numero % 2 == 0:
        soma += numero
        contador += 1

if contador > 0:
    media = soma / contador
else:
    media = 0

print(f"Soma dos valores pares: {soma}")
print(f"Média dos valores pares: {media}")
print(f"Total de números lidos: {contador}")
