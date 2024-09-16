def cadastrar_usuario():
    while True:
        login = input("Digite o login desejado: ")
        senha = input("Digite a senha desejada: ")
        if login != senha:
            return login, senha
        print("O login e a senha não podem ser iguais. Tente novamente.")

# Cadastro do primeiro usuário
print("Cadastro do primeiro usuário:")
login1, senha1 = cadastrar_usuario()

# Cadastro do segundo usuário
print("Cadastro do segundo usuário:")
while True:
    login2, senha2 = cadastrar_usuario()
    if login2 != login1:
        break
    print("O login do segundo usuário não pode ser igual ao do primeiro usuário. Tente novamente.")

print("\nCadastro concluído com sucesso!")
print(f"Usuário 1 - Login: {login1}, Senha: {senha1}")
print(f"Usuário 2 - Login: {login2}, Senha: {senha2}")


def contar_impares():
    cont_impares = 0
    while True:
        valor = int(input("Digite um valor (0 para parar): "))
        if valor == 0:
            break
        if valor % 2 != 0:
            cont_impares += 1
    return cont_impares

# Executa a função e exibe o resultado
impares = contar_impares()
print(f"Quantidade de valores ímpares digitados: {impares}")


def processar_valores():
    soma_positivos = 0
    quantidade_negativos = 0
    for i in range(10):
        valor = int(input(f"Digite o {i+1}º valor inteiro: "))
        if valor > 0:
            soma_positivos += valor
        elif valor < 0:
            quantidade_negativos += 1
    return soma_positivos, quantidade_negativos

# Executa a função e exibe o resultado
soma_positivos, quantidade_negativos = processar_valores()
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de valores negativos: {quantidade_negativos}")


def pedir_nome():
    while True:
        nome = input("Digite um nome (deve ter mais de 15 letras): ")
        if len(nome) > 15:
            return nome
        print("Nome deve ter mais de 15 letras. Tente novamente.")

# Executa a função e exibe o resultado
nome = pedir_nome()
print(f"Nome aceito: {nome}")


