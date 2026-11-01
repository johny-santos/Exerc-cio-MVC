import psycopg2

class LivrosModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                database="BibliotecaDB",
                user="postgres",
                password="dbJOHNY#@1503125469"
            )
        except Exception as e:
            print("Erro ao conectar no banco de dados: ", e)

    def listar_livros(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                """
                    SELECT l.id, 
                            l.titulo,
                            l.ano_publicacao,
                            a.nome
                    FROM livro AS l
                    INNER JOIN autor AS a
                    ON l.autor_id = a.id
                """
            )
            livros = cursor.fetchall()
            cursor.close()

            return livros
        except Exception as e:
            print("Erro ao listar os livros: ", e)        

    def inserir_livros(self, titulo, ano_publicacao, id_autor):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                """
                    INSERT INTO livro(titulo, ano_publicacao, autor_id) 
                    VALUES(%s, %s, %s)
                """, (titulo, ano_publicacao, id_autor)
                )
            self.conexao.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Erro ao inserir/salvar livro no banco de dados do sistema: ", e)
            self.conexao.rollback()
            return False

    def atualizar_livro(self, id_livro, titulo, ano_publicacao, id_autor):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE livro SET titulo = %s, ano_publicacao = %s, autor_id = %s WHERE id = %s;", 
                (titulo, ano_publicacao, id_autor, id_livro)
            )
            self.conexao.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Erro ao atualizar dados do livro: ", e)
            self.conexao.rollback()
            #Interessante o rollback nessas operações delicadas que podem dar merda para evitar problema.
            return False

    def excluir_livro(self, id_livro):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "DELETE FROM livro WHERE id = %s;",
                (id_livro,)    
            )
            self.conexao.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Erro ao excluir livro do banco do sistema: ", e)
            self.conexao.rollback()
            return False


