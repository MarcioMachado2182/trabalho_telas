import tkinter as tk
from tkinter import messagebox

class CarrinhoCompras(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.carrinho_items = []
        self.total_price = 0.0

        self.carrinho_listbox = tk.Listbox(self, width=40, height=10)
        self.carrinho_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.lbl_total = tk.Label(self, text="Total: R$ 0.00")
        self.lbl_total.pack(pady=5)

        self.btn_remover = tk.Button(self, text="Remover Item", command=self.remover_item)
        self.btn_remover.pack(pady=5)

    def adicionar_item(self, item):
        self.carrinho_items.append(item)
        self.atualizar_lista_carrinho()

    def remover_item(self):
        try:
            index = self.carrinho_listbox.curselection()[0]
            item_removido = self.carrinho_items.pop(index)
            self.atualizar_lista_carrinho()
            messagebox.showinfo("Item Removido", f"Item '{item_removido}' removido do carrinho.")
        except IndexError:
            messagebox.showwarning("Nenhum Item Selecionado", "Selecione um item para remover.")

    def atualizar_lista_carrinho(self):
        self.carrinho_listbox.delete(0, tk.END)
        for item in self.carrinho_items:
            self.carrinho_listbox.insert(tk.END, item['nome'] + " - " + item['preco'])
        self.calcular_total()

    def calcular_total(self):
        self.total_price = sum(float(item['preco'][3:].replace(",", ".")) for item in self.carrinho_items)
        self.lbl_total.config(text=f"Total: R$ {self.total_price:.2f}")

    def limpar_carrinho(self):
        self.carrinho_items = []
        self.atualizar_lista_carrinho()
