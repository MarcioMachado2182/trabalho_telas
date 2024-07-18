import tkinter as tk

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro")
        self.root.geometry("300x250")
        
        self.controller = None

        self.label_nome = tk.Label(self.root, text="Nome:")
        self.label_nome.pack(pady=(10, 5))
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack(pady=5)

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack(pady=5)

        self.label_senha = tk.Label(self.root, text="Senha:")
        self.label_senha.pack(pady=5)
        self.entry_senha = tk.Entry(self.root, show='*')
        self.entry_senha.pack(pady=5)

        self.label_login = tk.Label(self.root, text="Login:")
        self.label_login.pack(pady=5)
        self.entry_login = tk.Entry(self.root)
        self.entry_login.pack(pady=5)

        self.botao_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.botao_cadastrar.pack(pady=(10, 5))

        self.botao_login = tk.Button(self.root, text="Login", command=self.login)
        self.botao_login.pack(pady=(5, 10))

    def set_controller(self, controller):
        self.controller = controller

    def get_nome(self):
        return self.entry_nome.get()

    def get_email(self):
        return self.entry_email.get()

    def get_senha(self):
        return self.entry_senha.get()

    def get_login(self):
        return self.entry_login.get()

    def cadastrar(self):
        if self.controller:
            self.controller.cadastrar()

    def login(self):
        if self.controller:
            self.controller.login()
x