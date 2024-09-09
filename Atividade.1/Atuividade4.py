def calcular_peso_ideal(altura, sexo):
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido")
        return
    print(f"Peso ideal: {peso_ideal:.2f}")

# Exemplo de uso
altura = float(input("Digite a altura da pessoa (em metros): "))
sexo = input("Digite o sexo da pessoa (M para masculino e F para feminino):")
calcular_peso_ideal(altura, sexo)