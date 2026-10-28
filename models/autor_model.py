import psycopg2

class AutorModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                database="BibliotecaDB",
                user="postgres",
                password=""
            )
        except Exception as e:
            print("Erro ao conectar no banco de dados: ", e)

    def listar_autor(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "SELECT * FROM autor"
            )
            autor = cursor.fetchall()
            cursor.close()
            return autor
        
        except Exception as e:
            print("Erro ao listar os autores dos livros do sistema: ", e)        

    def inserir_autor(self, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                """
                    INSERT INTO autor(nome, nacionalidade) 
                    VALUES(%s, %s)
                """, (nome, nacionalidade)
                )
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao inserir/salvar autor no banco de dados do sistema: ", e)
            self.conexao.rollback()

    def atualizar_autor(self, id_autor, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE autor SET nome = %s, nacionalidade = %s WHERE id_autor = %s;", 
                (nome, nacionalidade, id_autor)
            )
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao atualizar dados do autor: ", e)
            self.conexao.rollback()
            #Interessante o rollback nessas operações delicadas que podem dar merda para evitar problema.

    def excluir_autor(self, id_autor):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "DELETE FROM autor WHERE id_autor = %s;",
                (id_autor,)    
            )
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao excluir autor, tente novamente mais tarde!\nErro: ", e)
            self.conexao.rollback()


