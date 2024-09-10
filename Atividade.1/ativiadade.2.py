# Programa para contar quantas das 5 pessoas têm 18 anos ou mais
contador_maioridade = 0

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    if idade >= 18:
        contador_maioridade += 1

print(f"Quantidade de pessoas com idade maior ou igual a 18 anos: {contador_maioridade}")
