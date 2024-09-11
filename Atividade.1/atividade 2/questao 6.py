# Verificação de número perfeito
n = int(input("Digite um número inteiro: "))

def eh_perfeito(num):
    soma_divisores = sum(i for i in range(1, num) if num % i == 0)
    return soma_divisores == num

if eh_perfeito(n):
    print(f"{n} é um número perfeito.")
else:
    print(f"{n} não é um número perfeito.")
