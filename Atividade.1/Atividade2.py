def calcular_aumento(salario):
    if salario < 600:
        salario_reajustado = salario * 1.30
        print(f"Salário reajustado: R${salario_reajustado:.2f}")
    else:
        print("O salário não tem direito ao aumento")

# Exemplo de uso
salario = float(input("Digite o salário do funcionário: "))
calcular_aumento(salario)