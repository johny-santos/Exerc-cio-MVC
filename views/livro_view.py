class LivroView:
    def menu_livro(self):
        print("\n======GERENCIAR LIVROS ======\n")
        print("1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Atualizar Livro")
        print("4 - Excluir Livro")
        print("5 - Voltar ao menu principal")

        return input("\nEscolha uma opção: \n")

    def solicitar_dados_livro(self):
        print("Cadastro novo Livro")
        print()

        titulo = input("\nDigite o nome do Livro: \n")
        ano_publicacao = int(input("\nDigite o ano de lançamento do Livro: \n"))
        id_autor = int(input("\nDigite o ID do Autor: \n"))

        return titulo, ano_publicacao, id_autor

    def exibir_livros(self, livros):
        if not livros:
           print("Não foi encontrado nenhum livro no sistema!")
        else:
            print("\nLivros da biblioteca: \n")

            for livro in livros:
                print(f"ID do livro: {livro[0]}\n")
                print(f"Título do livro: {livro[1]}\n")
                print(f"Ano de publicação: {livro[2]}\n")    
                print(f"Nome do Autor do livro: {livro[3]}")

    def atualizar_dados_livro(self):
        print("Atualização dos dados do Livro")
        print()

        id_livro = int(input("\nDigite o ID do livro na qual vai atualizar os dados: \n"))

        novo_titulo = input("\nDigite o novo Título do livro: \n")
        novo_ano_publicacao = int(input("\nDigite o novo ano de publicação do livro: \n"))
        novo_id_autor = int(input("\nDigite o novo ID do Autor: \n"))
        
        return id_livro, novo_titulo, novo_ano_publicacao, novo_id_autor

    def excluir_livro(self):
        print("Excluir Livro")
        print()

        id_livro_exclusao = int(input("\nDigite o ID do livro que você quer excluir: \n"))
        
        return id_livro_exclusao

    def exibir_mensagem(self, mensagem):
        print(mensagem)