import tkinter as tk
from PIL import Image, ImageTk

class CadastroView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.geometry("600x600")
        self.root.resizable(width=False, height=False)

             

        self.cadastro_frame = tk.Frame(self.root)

        self.create_cadastro_widgets()

        self.cadastro_frame.pack()

    def create_cadastro_widgets(self):
    
        self.root.title("Cadastro")
        
      # Carregar a imagem de fundo
        self.background_image = Image.open("trabalho_telas/controller/midia/anjo.jpg")
        self.background_image = self.background_image.resize((600, 600))  # Redimensiona a imagem para 600x600
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Criar uma Label para a imagem de fundo que ocupa toda a tela
        self.background_label = tk.Label(self.root, image=self.background_photo, background="yellow")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame para o formulário de cadastro
        self.cadastro_frame = tk.Frame(self.root, width=400, height=300)
        self.cadastro_frame.pack(expand=True)  # Centraliza o frame na tela

        # Widgets de entrada e rótulos
        label_nome = tk.Label(self.cadastro_frame, text="Nome:")
        label_nome.pack(pady=(10, 5))
        self.entry_nome = tk.Entry(self.cadastro_frame)
        self.entry_nome.pack(pady=5)

        label_email = tk.Label(self.cadastro_frame, text="Email:")
        label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.cadastro_frame)
        self.entry_email.pack(pady=5)

        label_senha = tk.Label(self.cadastro_frame, text="Senha:")
        label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.cadastro_frame, show='*')
        self.entry_senha.pack(pady=5)

        botao_cadastrar = tk.Button(self.cadastro_frame, text="Cadastrar", command=self.cadastrar)
        botao_cadastrar.pack(pady=(10, 5))

        botao_ir_para_login = tk.Button(self.cadastro_frame, text="Ir para Login")
        botao_ir_para_login.pack(pady=(5, 10))


    def get_nome(self):
        return self.entry_nome.get()

    def get_email(self):
        return self.entry_email.get() or self.entry_email_login.get()

    def get_senha(self):
        return self.entry_senha.get() or self.entry_senha_login.get()

    def cadastrar(self):
        if self.controller:
            self.controller.cadastrar()
