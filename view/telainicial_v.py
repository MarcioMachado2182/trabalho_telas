import tkinter as tk
from PIL import Image, ImageTk
from login_v import LoginView
from cadastro_v import CadastroView


class TelaInicial(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tela Inicial")
        self.geometry("800x600")
        self.resizable(width=False, height=False)

        self.background_image = Image.open("midia/Py-Shirts.jpg")
        self.background_image = self.background_image.resize((800, 600))
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_view = LoginView(self)
        self.login_view.place(relx=0.1, rely=0.2, anchor=tk.CENTER)

        self.cadastro_view = CadastroView(self)
        self.cadastro_view.place(relx=0.9, rely=0.2, anchor=tk.CENTER)

if __name__ == "__main__":
    app = TelaInicial()
    app.mainloop()
