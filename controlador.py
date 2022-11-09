from tkinter import Tk
import vista
from os import system


if __name__ == "__main__":
    system("cls")

    root = Tk()
    vista.ventana_principal(root)
    root.mainloop()
