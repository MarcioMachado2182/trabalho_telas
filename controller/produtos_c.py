from tkinter import messagebox
from model.model import Model
class ProdutosController:
    def __init__(self, view, parent):
        self.view = view
        self.parent = parent
        self.model = Model()

        