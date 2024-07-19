import tkinter as tk
from PIL import Image, ImageTk
from main import MainApp

class LoginView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title(("Tela login"))
        self.root.geometry("600x600")
        self.root.resizable(width=False, height=False)

             
        

        self.login_frame = tk.Frame(self.root)

        self.create_login_widgets()
        self.login_frame.pack()


    def create_login_widgets(self):
        label_email = tk.Label(self.login_frame, text="Email:")
        label_email.pack(pady=(10, 5))
        self.entry_email_login = tk.Entry(self.login_frame)
        self.entry_email_login.pack(pady=5)

        label_senha = tk.Label(self.login_frame, text="Senha:")
        label_senha.pack(pady=5)
        self.entry_senha_login = tk.Entry(self.login_frame, show='*')
        self.entry_senha_login.pack(pady=5)

        botao_login = tk.Button(self.login_frame, text="Login")
        botao_login.pack(pady=(10, 5))

        botao_ir_para_cadastro = tk.Button(self.login_frame, text="Ir para Cadastro")
        botao_ir_para_cadastro.pack(pady=(5, 10))

    def get_nome(self):
        return self.entry_nome.get()

    def get_email(self):
        return self.entry_email.get() or self.entry_email_login.get()

    def get_senha(self):
        return self.entry_senha.get() or self.entry_senha_login.get()



    def login(self):
            if self.controller:
                self.controller.login()