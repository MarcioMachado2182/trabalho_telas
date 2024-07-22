import tkinter as tk
from PIL import Image, ImageTk

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

    # Carregar a imagem de fundo
        self.background_image = Image.open("midia/anjo.jpg")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

    def create_login_widgets(self):
        self. label_email = tk.Label(self.login_frame, text="Email:")
        self.label_email.pack(pady=(10, 5))
        self.entry_email_login = tk.Entry(self.login_frame)
        self.entry_email_login.pack(pady=5)

        self.label_senha = tk.Label(self.login_frame, text="Senha:")
        self.label_senha.pack(pady=5)
        self.entry_senha_login = tk.Entry(self.login_frame, show='*')
        self.entry_senha_login.pack(pady=5)

        self.botao_login = tk.Button(self.login_frame, text="Login")
        self.botao_login.pack(pady=(10, 5))

        self.botao_ir_para_cadastro = tk.Button(self.login_frame, text="Ir para Cadastro")
        self.botao_ir_para_cadastro.pack(pady=(5, 10))

    def get_nome(self):
        return self.entry_nome.get()

    def get_email(self):
        return self.entry_email.get() or self.entry_email_login.get()

    def get_senha(self):
        return self.entry_senha.get() or self.entry_senha_login.get()

    def login(self):
            if self.controller:
                self.controller.login()