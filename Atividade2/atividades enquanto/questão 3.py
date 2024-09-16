def processar_valores():
    soma_positivos = 0
    quantidade_negativos = 0
    for i in range(10):
        valor = int(input(f"Digite o {i+1}º valor inteiro: "))
        if valor > 0:
            soma_positivos += valor
        elif valor < 0:
            quantidade_negativos += 1
    return soma_positivos, quantidade_negativos

# Executa a função e exibe o resultado
soma_positivos, quantidade_negativos = processar_valores()
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de valores negativos: {quantidade_negativos}")
