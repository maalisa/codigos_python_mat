# Leitura da primeira lista
lista1 = list(map(int, input("Digite os números da primeira lista, separados por espaço: ").split()))

# Leitura da segunda lista
lista2 = list(map(int, input("Digite os números da segunda lista, separados por espaço: ").split()))

# Encontrando a interseção
intersecao = sorted(set(lista1) & set(lista2))

# Exibindo o resultado
print("Números em comum:", intersecao)
