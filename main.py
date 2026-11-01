from models.livros_model import LivrosModel
from views.livro_view import LivroView
from controllers.livro_controller import LivroController
from models.autor_model import AutorModel
from views.autor_view import AutorView
from controllers.autor_controller import AutorController
from views.menu_view import MenuView
from controllers.menu_controller import MainController

livro_model = LivrosModel()
livro_view = LivroView()

livro_controller = LivroController(
    livro_model,
    livro_view
)

autor_model = AutorModel()
autor_view = AutorView()

autor_controller = AutorController(
    autor_model,
    autor_view
)

menu_view = MenuView()

main_controller = MainController(
    menu_view,
    autor_controller,
    livro_controller
)

main_controller.iniciar()