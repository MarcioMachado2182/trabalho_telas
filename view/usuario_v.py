import tkinter as tk

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro e Login")
        self.root.geometry("300x250")
        
        self.controller = None

        self.cadastro_frame = tk.Frame(self.root)
        self.login_frame = tk.Frame(self.root)

        self.create_cadastro_widgets()
        self.create_login_widgets()

        self.cadastro_frame.pack()

    def set_controller(self, controller):
        self.controller = controller

    def create_cadastro_widgets(self):
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

        botao_ir_para_login = tk.Button(self.cadastro_frame, text="Ir para Login", command=self.switch_to_login)
        botao_ir_para_login.pack(pady=(5, 10))

    def create_login_widgets(self):
        label_email = tk.Label(self.login_frame, text="Email:")
        label_email.pack(pady=(10, 5))
        self.entry_email_login = tk.Entry(self.login_frame)
        self.entry_email_login.pack(pady=5)

        label_senha = tk.Label(self.login_frame, text="Senha:")
        label_senha.pack(pady=5)
        self.entry_senha_login = tk.Entry(self.login_frame, show='*')
        self.entry_senha_login.pack(pady=5)

        botao_login = tk.Button(self.login_frame, text="Login", command=self.login)
        botao_login.pack(pady=(10, 5))

        botao_ir_para_cadastro = tk.Button(self.login_frame, text="Ir para Cadastro", command=self.switch_to_cadastro)
        botao_ir_para_cadastro.pack(pady=(5, 10))

    def get_nome(self):
        return self.entry_nome.get()

    def get_email(self):
        return self.entry_email.get() or self.entry_email_login.get()

    def get_senha(self):
        return self.entry_senha.get() or self.entry_senha_login.get()

    def cadastrar(self):
        if self.controller:
            self.controller.cadastrar()

    def login(self):
        if self.controller:
            self.controller.login()

    def switch_to_login(self):
        if self.controller:
            self.controller.switch_to_login()

    def switch_to_cadastro(self):
        if self.controller:
            self.controller.switch_to_cadastro()

    def show_cadastro_frame(self):
        self.login_frame.pack_forget()
        self.cadastro_frame.pack()

    def show_login_frame(self):
        self.cadastro_frame.pack_forget()
        self.login_frame.pack()
