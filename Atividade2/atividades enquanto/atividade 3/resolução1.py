def calcular_multa(velocidade, limite):
    if velocidade <= limite:
        return "Sem multa"
    elif 0 < (velocidade - limite) <= 10:
        return "Valor da multa: R$ 50,00"
    elif 10 < (velocidade - limite) <= 20:
        return "Valor da multa: R$ 100,00"
    else:
        return "Valor da multa: R$ 200,00"

# Entrada do usuário
velocidade = float(input("Qual foi a velocidade registrada do veículo? "))
limite = float(input("Qual é o limite de velocidade da via? "))

# Cálculo e saída da multa
resultado = calcular_multa(velocidade, limite)
print(resultado)
