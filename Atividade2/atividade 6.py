def calcular_parcela(valor_compra, parcelas):
    if parcelas > 12:
        juros_mensal = 0.015
    else:
        juros_mensal = 0

    valor_parcela = valor_compra * (1 + juros_mensal) ** parcelas / parcelas
    valor_total = valor_parcela * parcelas
    print(f"Valor total a pagar: R$ {valor_total:.2f}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")

# Exemplo de uso
valor_compra = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas (1 a 24): "))
if 1 <= parcelas <= 24:
    calcular_parcela(valor_compra, parcelas)
else:
    print("Quantidade de parcelas inválida.")
