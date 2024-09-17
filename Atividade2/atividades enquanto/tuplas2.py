# Cria uma lista para armazenar os 10 valores
valores = []

# Solicita ao usuário 10 valores inteiros
for i in range(10):
    valor = int(input(f"Digite o valor {i + 1}: "))
    valores.append(valor)

# Verifica e mostra as posições onde o valor 10 aparece
posicoes = [i for i, x in enumerate(valores) if x == 10]

if posicoes:
    print(f"O valor 10 aparece nas posições: {posicoes}")
else:
    print("O valor 10 não foi encontrado na lista.")
