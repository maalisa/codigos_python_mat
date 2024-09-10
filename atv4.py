valor_inicial = int(input("Informe um valor inicial: "))
valor_final = int(input("Informe um valor final: "))

soma = 0 # inicializando a variável
for contador in range(valor_inicial, valor_final+1):
    soma = soma + contador

print(f"A soma do intevalo de {valor_inicial} até {valor_final} é {soma}")