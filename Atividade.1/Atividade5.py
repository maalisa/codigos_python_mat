def consumo_combustivel(percurso, tipo_carro):
    if tipo_carro == 1:
        consumo = percurso / 8
    elif tipo_carro == 2:
        consumo = percurso / 9
    elif tipo_carro == 3:
        consumo = percurso / 12
    else:
        print("Tipo de carro inválido")
        return
    print(f"Consumo estimado de combustível: {consumo:.2f} litros")

# Exemplo de uso
percurso = float(input("Digite o percurso em quilômetros: "))
tipo_carro = int(input("Digite o tipo de carro (1, 2 ou 3): "))
consumo_combustivel(percurso, tipo_carro)