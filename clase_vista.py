class VPrincipal:
    def __init__(self, root):
        self.root = root

    def tam_y_tit(self, titulo, tam):
        """Titulo y Tamaño de la ventana"""
        self.root.title(titulo)
        self.root.geometry(tam)

    def boton(self, x, y, w, h, comando):
        """Crea botones"""

        from tkinter import Button

        boton_salir = Button(self.root, text="Salir", command=lambda: comando)
        boton_salir.place(x=x, y=y, w=w, h=h)
