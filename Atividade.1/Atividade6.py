def valores_divisiveis_por_2(a, b, c, d):
    for valor in [a, b, c, d]:
        if valor % 2 == 0:
            print(valor)

# Exemplo de uso
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
d = float(input("Digite o valor de D: "))
valores_divisiveis_por_2(a, b, c, d)