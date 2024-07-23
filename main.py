import tkinter as tk
from view.usuario_v import UsuarioView
from view.cadastro_v import CadastroView
from view.login_v import LoginView
from view.produtos_v import ProdutosView
from controller.login_c import LoginController
from view.carrinho_compras import CarrinhoCompras


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("adicionar usuário")
        self.login_v = LoginView
        self.cadastro_v = CadastroView
        self.produtos_v = ProdutosView
        self.carrinho_v = CarrinhoCompras
        self.switch_frame(self.produtos_v)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if frame_class == LoginView:
            controller = LoginController(new_frame, self)




        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill = tk.BOTH, expand = True)


        


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
