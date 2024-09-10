def verificar_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

# Exemplo de uso
ano = int(input("Digite um ano: "))
verificar_bissexto(ano)
