import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ProdutosView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Tela produtos")
        self.root.geometry("600x600")
        self.root.resizable(width=False, height=False)
        self.produtos_frame = tk.Frame(self.root)

        self.criar_janela()

    def adicionar_ao_carrinho(self, produto):
        print(f"{produto} adicionado ao carrinho!")

    def criar_janela(self):
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        produtos = [
            {"nome":"Camiseta  1", "img":"midia/camiseta1.PNG", "valor":"R$ 50,00"},
            {"nome":"Camiseta  2", "img":"midia/camiseta2.PNG", "valor":"R$ 50,00"},
            {"nome":"Camiseta  3", "img":"midia/camiseta3.PNG", "valor":"R$ 50,00"},
            {"nome":"Camiseta  4", "img":"midia/camiseta4.PNG", "valor":"R$ 50,00"},
            {"nome":"Camiseta  5", "img":"midia/camiseta5.PNG", "valor":"R$ 50,00"},
            {"nome":"Camiseta  6", "img":"midia/camiseta6.PNG", "valor":"R$ 50,00"}
        ]

        for i, produto in enumerate(produtos):
            nome = produto["nome"]
            imagem = produto["img"]
            preco = produto["valor"]

            frame = ttk.Frame(self.root)
            frame.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")

            img = Image.open(imagem)
            img = img.resize((150, 150))
            img_tk = ImageTk.PhotoImage(img)

            label_img = ttk.Label(frame, image=img_tk)
            label_img.image = img_tk
            label_img.grid(row=0, column=0, columnspan=2)

            label_nome = ttk.Label(frame, text=nome)
            label_nome.grid(row=1, column=0, columnspan=2)

            label_preco = ttk.Label(frame, text=preco)
            label_preco.grid(row=2, column=0, columnspan=2)

            btn_adicionar = ttk.Button(frame, text="Adicionar ao Carrinho", command=lambda n=nome: self.adicionar_ao_carrinho(n))
            btn_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

        # Criando o botão "Ir para o Carrinho de Compras"
        frame_carrinho = ttk.Frame(self.root)
        frame_carrinho.grid(row=len(produtos) // 3 + 1, column=1, pady=10)
        
        btn_carrinho = ttk.Button(frame_carrinho, text="Ir para o Carrinho de Compras", command=self.ir_para_carrinho)
        btn_carrinho.pack()

    def ir_para_carrinho(self):
        print("Indo para o Carrinho de Compras...")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProdutosView(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()