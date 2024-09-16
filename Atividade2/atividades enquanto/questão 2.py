def contar_impares():
    cont_impares = 0
    while True:
        valor = int(input("Digite um valor (0 para parar): "))
        if valor == 0:
            break
        if valor % 2 != 0:
            cont_impares += 1
    return cont_impares

# Executa a função e exibe o resultado
impares = contar_impares()
print(f"Quantidade de valores ímpares digitados: {impares}")
