from tkinter import messagebox
from model.model import Model
from view.cadastro_v import CadastroView



 




class LoginController:
    def __init__(self, view, parent):
        self.view = view
        self.parent = parent
        self.model = Model()
        self.view.botao_ir_para_cadastro.configure(command=self.ir_para_cadastro)
        self.view.botao_login.configure(command = self.login)


    def ir_para_cadastro(self):
        self.parent.switch_frame(self.parent.cadastro)

    def login(self):
        email=self.view.get_email()
        senha = self.view.get_senha()

        if self.model.check_login(email,senha):
            messagebox.showinfo("Sucesso", 'Login realizado com sucesso!')
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")

        