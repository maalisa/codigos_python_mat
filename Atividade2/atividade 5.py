def calcular_pagamento(horas_trabalhadas, valor_por_hora):
    if horas_trabalhadas > 40:
        horas_extras = horas_trabalhadas - 40
        pagamento_extra = horas_extras * valor_por_hora * 1.5
        salario = (40 * valor_por_hora) + pagamento_extra
    else:
        salario = horas_trabalhadas * valor_por_hora
    print(f"Salário a pagar: R$ {salario:.2f}")

# Exemplo de uso
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))
calcular_pagamento(horas_trabalhadas, valor_por_hora)
