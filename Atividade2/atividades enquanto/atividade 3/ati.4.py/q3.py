eventos = []

while True:
    print("\nEventos agendados:", eventos)
    acao = input("Digite 'adicionar' para adicionar um evento, 'remover' para remover, ou 'sair' para encerrar: ").strip().lower()
    
    if acao == 'adicionar':
        evento = input("Digite o evento a ser adicionado: ")
        eventos.append(evento)
    elif acao == 'remover':
        evento = input("Digite o evento a ser removido: ")
        if evento in eventos:
            eventos.remove(evento)
        else:
            print("Evento não encontrado.")
    elif acao == 'sair':
        break
    else:
        print("Ação inválida.")

print("Eventos finais:", eventos)
