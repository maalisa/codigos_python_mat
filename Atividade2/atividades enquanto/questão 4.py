def pedir_nome():
    while True:
        nome = input("Digite um nome (deve ter mais de 15 letras): ")
        if len(nome) > 15:
            return nome
        print("Nome deve ter mais de 15 letras. Tente novamente.")

# Executa a função e exibe o resultado
nome = pedir_nome()
print(f"Nome aceito: {nome}")
