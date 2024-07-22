import tkinter as tk
from tkinter import ttk

class CarrinhoCompras(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        
        self.carrinho_listbox = tk.Listbox(self)
        self.carrinho_listbox.pack(fill=tk.BOTH, expand=True)