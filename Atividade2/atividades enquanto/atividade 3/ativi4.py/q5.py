import random

resultados = []

while True:
    resultado = random.choice(['cara', 'coroa'])
    resultados.append(resultado)
    print("Resultado do lançamento:", resultado)
    
    repetir = input("Deseja lançar a moeda novamente? (s/n): ").strip().lower()
    if repetir != 's':
        break

print("Resultados de todos os lançamentos:", resultados)
