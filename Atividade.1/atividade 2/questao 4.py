# Maior número entre 5 informados
maior_numero = None
for _ in range(5):
    num = int(input("Digite um número inteiro: "))
    if maior_numero is None or num > maior_numero:
        maior_numero = num

print(f"O maior número informado é: {maior_numero}")
