import tkinter as tk
from view.usuario_v import View
from controller.usuario_c import Controller

def main():
    root = tk.Tk()
    view = View(root)
    controller = Controller(view)
    root.mainloop()

if __name__ == "__main__":
    main()