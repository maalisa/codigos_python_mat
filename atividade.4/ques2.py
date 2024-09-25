def notas_dos_alunos():
    alunos = {}

    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        nota = float(input("Digite a nota do aluno: "))
        alunos[nome] = nota

    if alunos:
        media = sum(alunos.values()) / len(alunos)
        print(f"\nMédia da turma: {media:.2f}")
        print("Alunos com notas acima da média:")
        for aluno, nota in alunos.items():
            if nota > media:
                print(aluno)

notas_dos_alunos()
