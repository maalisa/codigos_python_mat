# Contagem de múltiplos de 7 e 11 entre a e b
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

contagem = sum(1 for x in range(a, b + 1) if x % 7 == 0 and x % 11 == 0)

print(f"Total de números entre {a} e {b} que são múltiplos de 7 e 11: {contagem}")
