from tkinter import messagebox
from model.usuario_m import Model

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model()
        self.view.set_controller(self)
    
    def cadastrar(self):
        nome = self.view.get_nome()
        email = self.view.get_email()
        senha = self.view.get_senha()
        login = self.view.get_login()
        
        if nome and email and senha and login:
            self.model.add_user(nome, email, senha, login)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")
    
    def login(self):
        login = self.view.get_login()
        senha = self.view.get_senha()
        
        if self.model.check_login(login, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Login ou senha incorretos!")
            x

