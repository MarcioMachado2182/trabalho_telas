
from view.cadastro_v import CadastroView
from model.model import Model
from view.login_v import LoginView
import  tkinter as tk
class CadastroController:
    def __init__(self,parent, view:CadastroView, model:Model):
        self.view = view
        self.model = model
        self.view.botao_cadastrar.config(command=self.cadastrar_usuario)

    def cadastrar_usuario(self):
        nome = self.view.get_nome()
        email = self.view.get_email()
        senha = self.view.get_senha()
        if nome and email and senha.isdigit():
            self.model.cadastrar_usuario(nome, email, senha)
            self.view.nome_entry.delete(0, tk.END)
            self.view.email_entry.delete(0, tk.END)
            self.view.senha_entry.delete(0, tk.END)
            self.view.cadastrar_listbox.delete(0, tk.END)


