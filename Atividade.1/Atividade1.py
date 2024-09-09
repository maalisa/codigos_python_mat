def verificar_intervalo(numero):
    if 100 <= numero <= 200:
        print("Este valor está entre 100 e 200")
    else:
        print("Este valor não está entre 100 e 200")

# Exemplo de uso
numero = float(input("Digite um número: "))
verificar_intervalo(numero)