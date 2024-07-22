import tkinter as tk

class TelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tela Principal")
        self.geometry("600x400")
        self.resizable(width=False, height=False)

        self.menu_opcoes = tk.Menu(self, tearoff=False)
        self.menu_opcoes.add_command(label="Opção 1", command=self.opcao1)
        self.menu_opcoes.add_command(label="Opção 2", command=self.opcao2)
        self.menu_opcoes.add_separator()
        self.menu_opcoes.add_command(label="Sair", command=self.quit)

        self.config(menu=self.menu_opcoes)

    def opcao1(self):
        print("Executando a Opção 1")

    def opcao2(self):
        print("Executando a Opção 2")

if __name__ == "__main__":
    app = TelaPrincipal()
    app.mainloop()
