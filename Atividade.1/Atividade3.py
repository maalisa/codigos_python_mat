def verificar_financiamento(salario, financiamento):
    if financiamento <= 5 * salario:
        print("Financiamento Concedido")
    else:
        print("Financiamento Negado")
    print("Obrigado por nos consultar")

# Exemplo de uso
salario = float(input("Digite o salário da pessoa: "))
financiamento = float(input("Digite o valor do financiamento: "))
verificar_financiamento(salario, financiamento)