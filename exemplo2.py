nome = input("Informe seu nome: ")
end = input("Informe seu endereço: ")
idade = input("Informe sua idade: ")

#Exibindo dados das variáveis
#print(nome, end, idade)

#1ª forma de concatenação
print("\nOlá ",nome," seu endereço é ",end," sua idade é ", idade)

#2ª forma de concatenação
print("\nOlá {} seu endereço é {} e sua idade é {}".format(nome, end, idade))

#3ª forma de concatenação - f string
print(f"Bem vinda {nome}, você mora na {end} e tem {idade} anos")


