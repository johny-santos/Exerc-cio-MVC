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