def calcular_desconto(preco, percentual):
    return preco - (preco * (percentual / 100))

def desconto_produtos():
    precos_com_desconto = []
    
    for _ in range(5):
        preco = float(input("Digite o valor do produto: "))
        percentual = float(input("Digite o percentual de desconto: "))
        preco_final = calcular_desconto(preco, percentual)
        precos_com_desconto.append(preco_final)
        print(f"Preço final com desconto: {preco_final:.2f}")

    print("\nLista de preços finais com desconto:")
    for valor in precos_com_desconto:
        print(f"R$ {valor:.2f}")

desconto_produtos()
