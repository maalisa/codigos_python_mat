def verificar_aprovacao(nota, frequencia):
    if nota >= 7 and frequencia >= 75:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

# Exemplo de uso
nota = float(input("Digite a nota final: "))
frequencia = float(input("Digite a frequência (%): "))
verificar_aprovacao(nota, frequencia)
