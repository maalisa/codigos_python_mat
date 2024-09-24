notas = []
nota = -1

# Leitura das notas
while nota != 0:
    nota = float(input("Digite a nota do aluno (digite 0 para terminar): "))
    if nota != 0:
        notas.append(nota)

# Cálculo da média
media = sum(notas) / len(notas) if notas else 0

# Contando alunos com nota acima da média
alunos_acima_media = sum(1 for n in notas if n > media)

print("Quantidade de alunos com notas acima da média:", alunos_acima_media)
