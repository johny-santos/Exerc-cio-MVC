import models.autor_model
import views.autor_view

class AutorController:
    def __init__(self, autor_model, autor_view):
        self.autor_model = autor_model
        self.autor_view = autor_view

    def gerenciar_autores(self):
        while True:
            opcao = self.autor_view.menu_autor()

            if opcao == "1":
                self.cadastrar_autor()

            elif opcao == "2":
                self.listar_autor()

            elif opcao == "3":
                self.atualizar_autor()

            elif opcao == "4": 
                self.excluir_autor()

            elif opcao == "5":
                break

            else:
                print("Opção inválida!\nTente com os exatos números das opções do menu!")