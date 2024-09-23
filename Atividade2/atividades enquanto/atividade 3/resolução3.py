def calcular_bono(salario, anos):
    if anos <= 5:
        bonus = salario * 0.05
    elif 6 <= anos <= 10:
        bonus = salario * 0.10
    else:
        bonus = salario * 0.15
    return bonus, salario + bonus

# Entrada do usuário
salario = float(input("Digite o salário atual: "))
anos = int(input("Digite o número de anos de serviço: "))

bonus, salario_final = calcular_bono(salario, anos)
print(f"Valor do bônus: R$ {bonus:.2f}")
print(f"Salário final com bônus: R$ {salario_final:.2f}")
