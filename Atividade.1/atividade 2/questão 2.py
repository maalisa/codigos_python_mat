# Contagem de números negativos e soma dos positivos
numeros = []
for _ in range(8):
    num = int(input("Digite um número: "))
    numeros.append(num)

negativos = sum(1 for x in numeros if x < 0)
soma_positivos = sum(x for x in numeros if x > 0)

print(f"Quantidade de números negativos: {negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
