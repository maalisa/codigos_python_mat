# Cria uma lista para armazenar as temperaturas dos 12 meses
temperaturas = []

# Solicita ao usuário as temperaturas de cada mês
for i in range(12):
    temperatura = float(input(f"Digite a temperatura média do mês {i + 1} (em °C): "))
    temperaturas.append(temperatura)

# Calcula a média anual das temperaturas
media_anual = sum(temperaturas) / len(temperaturas)

# Exibe a média anual
print(f"A média anual das temperaturas é: {media_anual:.2f}°C")

# Meses do ano
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Mostra as temperaturas abaixo da média com o mês correspondente
for i, temp in enumerate(temperaturas):
    if temp < media_anual:
        print(f"A temperatura em {meses[i]} ({temp:.2f}°C) está abaixo da média anual.")
