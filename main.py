import tkinter as tk
from view.usuario_v import View
from view.cadastro_v import CadastroView
from view.login_v import LoginView


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("adicionar usuário")
        self.login= LoginView
        self.cadastro = CadastroView
        self.switch_frame(self.login)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        # if frame_class ==  UsuarioView:
        #     model =  UsuarioModel()
        #     UsuarioController(new_frame,model)
        # elif frame_class == DeleteView:
        #     model =  UsuarioModel()
        #     DeleteController(new_frame, model)
        # elif frame_class == AtualizaView:
        #     model =  UsuarioModel()
        #     AtualizaController(new_frame, model)

        if hasattr(self, "current_frame"):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
