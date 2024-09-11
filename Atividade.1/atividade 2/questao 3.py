# Temperaturas acima e abaixo da média
temperaturas = []
for _ in range(7):
    temp = float(input("Digite a temperatura: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)
acima_ou_igual = sum(1 for t in temperaturas if t >= media)
abaixo = sum(1 for t in temperaturas if t < media)

print(f"Temperaturas iguais ou acima da média: {acima_ou_igual}")
print(f"Temperaturas abaixo da média: {abaixo}")
