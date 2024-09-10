def classificar_idade(idade):
    if idade < 12:
        print("Criança")
    elif 12 <= idade <= 18:
        print("Adolescente")
    elif 18 <= idade <= 60:
        print("Adulto")
    else:
        print("Idoso")

# Exemplo de uso
idade = int(input("Digite a idade: "))
classificar_idade(idade)
