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
        
        if nome and email and senha:
            self.model.add_user(nome, email, senha)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")
    
    def login(self):
        email = self.view.get_email()
        senha = self.view.get_senha()
        
        if self.model.check_login(email, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")
    
    def switch_to_login(self):
        self.view.show_login_frame()
    
    def switch_to_cadastro(self):
        self.view.show_cadastro_frame()


