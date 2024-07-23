import tkinter as tk
from tkinter import messagebox
from cliente_model import ClienteModel
from carrinho_compras import CarrinhoCompras

class Aplicacao(tk.Tk):
    def __init__(self, cliente_id, cliente_model):
        super().__init__()
        self.cliente_id = cliente_id
        self.cliente_model = cliente_model
        self.selected_items = []
        self.title("Loja de Camisetas")

        self.camisetas = [
            {"nome": "Camiseta 1", "img": "midia/camiseta1.PNG", "preco": "R$ 50,00"},
            {"nome": "Camiseta 2", "img": "midia/camiseta2.PNG", "preco": "R$ 55,00"},
            {"nome": "Camiseta 3", "img": "midia/camiseta3.PNG", "preco": "R$ 70,00"},
            {"nome": "Camiseta 4", "img": "midia/camiseta4.PNG", "preco": "R$ 53,00"},
            {"nome": "Camiseta 5", "img": "midia/camiseta5.PNG", "preco": "R$ 50,00"},
            {"nome": "Camiseta 6", "img": "midia/camiseta6.PNG", "preco": "R$ 55,00"},
            {"nome": "Camiseta 7", "img": "midia/camiseta7.PNG", "preco": "R$ 58,00"},
            {"nome": "Camiseta 8", "img": "midia/camiseta8.PNG", "preco": "R$ 60,00"},
            {"nome": "Camiseta 9", "img": "midia/camiseta9.PNG", "preco": "R$ 57,00"},
            {"nome": "Camiseta 10", "img": "midia/camiseta10.PNG", "preco": "R$ 60,00"},
            {"nome": "Camiseta 11", "img": "midia/camiseta11.PNG", "preco": "R$ 50,00"},
            {"nome": "Camiseta 12", "img": "midia/camiseta12.PNG", "preco": "R$ 55,00"},
            {"nome": "Camiseta 13", "img": "midia/camiseta13.PNG", "preco": "R$ 50,00"}
        ]
        
        self.camisetas_vars = []
        self.carrinho = CarrinhoCompras(self)
        self.carrinho.pack(pady=10)

        self.show_menu_window()

    def show_menu_window(self):
        self.clear_window()

        tk.Label(self, text="Escolha suas camisetas").pack(pady=10)

        for item in self.camisetas:
            var = tk.IntVar()
            tk.Checkbutton(self, text=f"{item['nome']} - {item['preco']}", variable=var, command=lambda item=item: self.adicionar_ao_carrinho(item, var)).pack()
            self.camisetas_vars.append((item, var))

        tk.Button(self, text="Ir para o Resumo do Pedido", command=self.show_summary_window).pack(pady=10)

    def adicionar_ao_carrinho(self, item, var):
        if var.get() == 1:
            self.carrinho.adicionar_item(item)
        else:
            self.carrinho.remover_item()

    def show_summary_window(self):
        if not self.carrinho.carrinho_items:
            messagebox.showwarning("Atenção!", "Selecione pelo menos uma camiseta antes de visualizar o resumo do pedido.")
            return
        
        self.clear_window()
        total_price = self.carrinho.total_price

        self.payment_var = tk.StringVar(value='Dinheiro')

        tk.Label(self, text="Resumo do Pedido").pack(pady=10)
        tk.Label(self, text=f"Camisetas: {', '.join(item['nome'] for item in self.carrinho.carrinho_items)}").pack(pady=5)
        tk.Label(self, text=f"Valor Total: R$ {total_price:.2f}").pack(pady=5)
        
        tk.Label(self, text="Selecione a forma de pagamento:").pack(pady=5)
        tk.Radiobutton(self, text="Dinheiro", variable=self.payment_var, value='Dinheiro').pack()
        tk.Radiobutton(self, text="Cartão de Crédito", variable=self.payment_var, value='Cartão de Crédito').pack()
        tk.Radiobutton(self, text="PIX", variable=self.payment_var, value='PIX').pack()

        tk.Button(self, text="Finalizar Pedido", command=self.show_address_window).pack(pady=10)
        tk.Button(self, text="Voltar ao Menu", command=self.show_menu_window).pack(pady=10)

    def show_address_window(self):
        self.clear_window()
        self.address_entry = tk.Entry(self)

        tk.Label(self, text="Endereço de Entrega").pack(pady=5)
        self.address_entry.pack(pady=5)
        tk.Label(self, text=f"Custo de Envio: R$ 10,00").pack(pady=5)
        tk.Label(self, text=f"Valor Total: R$ {self.carrinho.total_price + 10:.2f}").pack(pady=5)

        tk.Button(self, text="Finalizar Pedido", command=self.validate_and_confirm_order).pack(pady=20)

    def validate_and_confirm_order(self):
        address = self.address_entry.get()
        payment_method = self.payment_var.get()
        final_price = self.carrinho.total_price + 10

        if not address:
            messagebox.showerror("Erro", "É necessário inserir o endereço para entrega. Por favor, insira um endereço válido.")
            return
        
        items = ', '.join(item['nome'] for item in self.carrinho.carrinho_items)
        if self.cliente_model.inserir_pedido(self.cliente_id, items, final_price, payment_method, address,
