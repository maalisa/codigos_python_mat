# Programa para calcular o peso médio e a idade média de 5 jogadores
soma_pesos = 0
soma_idades = 0

for i in range(5):
    peso = float(input(f"Digite o peso do jogador {i+1}: "))
    idade = int(input(f"Digite a idade do jogador {i+1}: "))
    soma_pesos += peso
    soma_idades += idade

peso_medio = soma_pesos / 5
idade_media = soma_idades / 5

print(f"Peso médio do time: {peso_medio:.2f}")
print(f"Idade média do time: {idade_media:.2f}")
