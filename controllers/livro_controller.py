class LivroController:
    def __init__(self, livro_model, livro_view):
        self.livro_model = livro_model
        self.livro_view = livro_view

    def gerenciar_livros(self):
        while True:
            opcao = self.livro_view.menu_livro()

            if opcao == "1":
                self.cadastrar_livro()

            elif opcao == "2":
                self.listar_livros()

            elif opcao == "3":
                self.atualizar_livro()

            elif opcao == "4": 
                self.excluir_livro()

            elif opcao == "5":
                break

            else:
                print("Opção inválida!\nTente com os exatos números das opções do menu!")

    def cadastrar_livro(self):
        titulo, ano_publicacao, id_autor = self.livro_view.solicitar_dados_livro()

        sucesso =  self.livro_model.inserir_livros(titulo, ano_publicacao, id_autor)

        if sucesso: 
            self.livro_view.exibir_mensagem("Livro cadastrado com sucesso!")
        else:
            self.livro_view.exibir_mensagem("Não foi possível cadastrar o livro...")

    def listar_livros(self):
        livros = self.livro_model.listar_livros()

        self.livro_view.exibir_livros(livros)

    def atualizar_livro(self):
        id_livro, novo_titulo, novo_ano_publicacao, novo_id_autor = self.livro_view.atualizar_dados_livro()

        sucesso = self.livro_model.atualizar_livro(id_livro, novo_titulo, novo_ano_publicacao, novo_id_autor)

        if sucesso:
            self.livro_view.exibir_mensagem("Dados do livro atualizados com sucesso!")

        else:
            self.livro_view.exibir_mensagem("Não foi possível atualizar os dados do livro...")            

    def excluir_livro(self):
        id_livro_exclusao = self.livro_view.excluir_livro()

        sucesso = self.livro_model.excluir_livro(id_livro_exclusao)

        if sucesso:
            self.livro_view.exibir_mensagem("Livro excluído com sucesso!")

        else:
            self.livro_view.exibir_mensagem("Não foi possível excluir o livro...") 
