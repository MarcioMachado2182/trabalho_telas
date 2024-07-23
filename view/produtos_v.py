import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from view.carrinho_compras import CarrinhoCompras
from model.model import Model  # Importe o modelo conforme necessário
class ProdutosView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Tela produtos")
        self.root.geometry("600x600")
        self.produtos_frame = tk.Frame(self.root)
        self.produtos_frame.pack()
        self.model = Model()  # Instância do modelo (ajuste conforme o nome correto do seu modelo)

        self.criar_janela()

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.adicionar_item(produto)
        messagebox.showinfo("Sucesso", f"{produto['nome']} adicionado ao carrinho!")

    def criar_janela(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        produtos = [
            {"nome":"Camiseta  1", "img":"midia/camiseta1.PNG", "preco":"R$ 50,00"},
            {"nome":"Camiseta  2", "img":"midia/camiseta2.PNG", "preco":"R$ 55,00"},
            {"nome":"Camiseta  3", "img":"midia/camiseta3.PNG", "preco":"R$ 70,00"},
            {"nome":"Camiseta  4", "img":"midia/camiseta4.PNG", "preco":"R$ 53,00"},
            {"nome":"Camiseta  5", "img":"midia/camiseta5.PNG", "preco":"R$ 50,00"},
            {"nome":"Camiseta  6", "img":"midia/camiseta6.PNG", "preco":"R$ 55,00"}
        ]

        for i, produto in enumerate(produtos):
            nome = produto["nome"]
            imagem = produto["img"]
            preco = produto["preco"]

            self.frame = ttk.Frame(self.produtos_frame)
            self.frame.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")

            img = Image.open(imagem)
            img = img.resize((150, 150))
            img_tk = ImageTk.PhotoImage(img)

            self.label_img = ttk.Label(frame, image=img_tk)
            self.label_img.image = img_tk
            self.label_img.grid(row=0, column=0, columnspan=2)

            self.label_nome = ttk.Label(frame, text=nome)
            self.label_nome.grid(row=1, column=0, columnspan=2)

            self.label_preco = ttk.Label(frame, text=preco)
            self.label_preco.grid(row=2, column=0, columnspan=2)

            self.btn_adicionar = ttk.Button(frame, text="Adicionar ao Carrinho", command=lambda p=produto: self.adicionar_ao_carrinho(p))
            self.btn_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

        # Criando o botão "Ir para o Carrinho de Compras"
        self.frame_carrinho = ttk.Frame(self.root)
        self.frame_carrinho.pack(side="bottom")
        
        self.btn_carrinho = ttk.Button(frame_carrinho, text="Ir para o Carrinho de Compras", command=self.ir_para_carrinho)
        self.btn_carrinho.pack()

    def ir_para_carrinho(self):
        print("Indo para o Carrinho de Compras...")
        self.root.switch_frame(self.root.carrinho_v)
        # Aqui você pode adicionar a lógica para passar para a tela de carrinho de compras
