# Solicita ao usuário os elementos da primeira lista
lista1 = [int(input(f"Digite o valor {i + 1} da primeira lista: ")) for i in range(5)]
# Solicita ao usuário os elementos da segunda lista
lista2 = [int(input(f"Digite o valor {i + 1} da segunda lista: ")) for i in range(5)]

# Verifica se as listas têm o mesmo tamanho
if len(lista1) != len(lista2):
    print("As listas devem ter o mesmo tamanho.")
else:
    # Soma os valores correspondentes das duas listas
    lista_soma = [a + b for a, b in zip(lista1, lista2)]
    
    # Exibe a lista resultante
    print(f"A lista resultante da soma é: {lista_soma}")
