class AutorView:
    def menu_autor(self):
        print("\n====== GERENCIAR AUTORES ======\n")
        print("1 - Cadastrar Autor")
        print("2 - Listar Autor")
        print("3 - Atualizar Autor")
        print("4 - Excluir Autor")
        print("5 - Voltar ao menu principal")

        return input("\nEscolha uma opção: \n")

    def solicitar_dados_autor(self):
        print("Cadastro Autor")
        print()

        nome = input("\nDigite o nome do autor: \n")
        nacionalidade = input("\nDigite a nacionalidade do Autor: \n")
        
        return nome, nacionalidade

    def exibir_autores(self, autores):  
        if not autores:
            print("Não foi encontrado nenhum Autor!")
        else:
            print("Autores dos Livros da Biblioteca")
            for autor in autores:
                print(f"Identificador do Autor: {autor[0]}\n")
                print(f"Nome do Autor: {autor[1]}\n")
                print(f"Nacionalidade do Autor: {autor[2]}")
                print("=================================================") 
               #Em tuplas, acessamos os valores pelos índices!!!

    def atualizar_dados_autor(self):
        print("Atualização dos dados do Autor")
        print()

        id_autor = int(input("\nDigite o ID do Autor que você vai atualizar os dados: \n"))

        novo_nome = input("\nDigite o novo nome do Autor: \n")
        nova_nacionalidade = input("\nDigite a nova nacionalidade do Autor: \n")

        return id_autor, novo_nome, nova_nacionalidade

    def excluir_autor(self):
        print("Excluir Autor:")
        print()

        id_autor = int(input("\nDigite o ID do autor na qual você quer excluir do sistema: \n"))

        return id_autor

    def exibir_mensagem(self, mensagem):
        print(mensagem)