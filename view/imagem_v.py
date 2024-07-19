import tkinter as tk
from PIL import Image, ImageTk

# Função para carregar a imagem
def load_image():
    # Carrega a imagem usando Pillow
    image = Image.open("midia/anjo.jpg")#tem que dar o caminho da imagem
    # Redimensiona a imagem conforme necessário
    image = image.resize((50, 50))
    # Converte a imagem para um formato que o tkinter possa exibir
    photo = ImageTk.PhotoImage(image)
    return photo

# Cria a janela principal
root = tk.Tk()

# Carrega a imagem
image = load_image()

# Cria a label com a imagem e o texto
label = tk.Label(root, text="Exemplo de imagem ao lado de uma label", image=image, compound="left")
label.pack(padx=10, pady=10)

# Executa o loop principal do tkinter
root.mainloop()

