def comparar_idades(idade1, idade2):
    if idade1 > idade2:
        return "A primeira pessoa é mais velha."
    elif idade1 < idade2:
        return "A segunda pessoa é mais velha."
    else:
        return "Ambas têm a mesma idade."

def idade_comparacao():
    while True:
        idade1 = int(input("Digite a idade da primeira pessoa (ou 0 para sair): "))
        if idade1 == 0:
            break
        idade2 = int(input("Digite a idade da segunda pessoa: "))
        resultado = comparar_idades(idade1, idade2)
        print(resultado)

idade_comparacao()
