import random

# Simulação de lançamento de dados
contagem = {i: 0 for i in range(1, 7)}

for _ in range(10):
    lancamento = random.randint(1, 6)
    contagem[lancamento] += 1

for valor, quantidade in contagem.items():
    print(f"Valor {valor} foi sorteado {quantidade} vezes.")
