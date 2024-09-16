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
