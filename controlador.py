from tkinter import Tk
from vista import ventana_principal
from os import system


if __name__ == "__main__":
    system("cls")

    root = Tk()
    ventana_principal(root)
    root.mainloop()
