# Programa para calcular a soma dos números inteiros em um intervalo
valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))

soma = sum(range(valor_inicial, valor_final + 1))

print(f"Soma dos números inteiros entre {valor_inicial} e {valor_final}: {soma}")
