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

    def cadastrar_autor(self): 
        nome, nacionalidade = self.autor_view.solicitar_dados_autor()

        sucesso = self.autor_model.inserir_autor(nome, nacionalidade)

        if sucesso:
            self.autor_view.exibir_mensagem("Autor Cadastrado com sucesso!")
        else: 
            self.autor_view.exibir_mensagem("Não foi possível cadastrar o Autor...")            

    def listar_autor(self):
        autores = self.autor_model.listar_autor()

        self.autor_view.exibir_autores(autores)

    def atualizar_autor(self):
        id_autor, novo_nome, nova_nacionalidade = self.autor_view.atualizar_dados_autor()

        sucesso =  self.autor_model.atualizar_autor(id_autor, novo_nome, nova_nacionalidade)

        if sucesso:
            self.autor_view.exibir_mensagem("Dados do Autor atualizados com sucesso!")
        else:
            self.autor_view.exibir_mensagem("Não foi possível aualizar os dados do Autor...")

    def excluir_autor(self):
        id_autor = self.autor_view.excluir_autor()

        sucesso = self.autor_model.excluir_autor(id_autor)

        if sucesso:
            self.autor_view.exibir_mensagem("Autor excluído com sucesso!")
        else:
            self.autor_view.exibir_mensagem("Não foi possível excluir o Autor...")