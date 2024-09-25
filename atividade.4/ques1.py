def catalogo_de_livros():
    catalogo = {}

    while True:
        print("\nMenu:")
        print("1. Adicionar um novo livro")
        print("2. Remover um livro")
        print("3. Exibir o catálogo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            catalogo[titulo] = autor
            print(f'Livro "{titulo}" adicionado com sucesso.')
            
        elif opcao == '2':
            titulo = input("Digite o título do livro a ser removido: ")
            if titulo in catalogo:
                del catalogo[titulo]
                print(f'Livro "{titulo}" removido com sucesso.')
            else:
                print("Livro não encontrado.")
                
        elif opcao == '3':
            print("\nCatálogo de Livros:")
            for titulo, autor in catalogo.items():
                print(f'Título: {titulo} | Autor: {autor}')
            print(f'Total de livros cadastrados: {len(catalogo)}')
        
        elif opcao == '4':
            print("Saindo do programa...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

catalogo_de_livros()
