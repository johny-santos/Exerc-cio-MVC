class MainController:
    def __init__(self, menu_view, autor_controller, livro_controller):
        self.menu_view = menu_view
        self.autor_controller = autor_controller
        self.livro_controller = livro_controller


    def iniciar(self):
        while True:
            opcao = self.menu_view.menu_principal()

            if opcao == "1":
                self.autor_controller.gerenciar_autores()

            elif opcao == "2":
                self.livro_controller.gerenciar_livros()

            elif opcao == "3":
                print("Saindo...")
                break

            else:
                print("Opção inválida!\nTente novamente com uma das opções disponívei no MENU!")