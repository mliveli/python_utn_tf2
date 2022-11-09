import modelo


class VPrincipal:
    def __init__(self, root):
        self.root = root

    def tam_y_tit(self, titulo, tam):
        """Titulo y Tamaño de la ventana"""
        self.root.title(titulo)
        self.root.geometry(tam)

    def boton(self, x, y, w, h):
        """Crea botones"""
        from tkinter import Button

        objm = modelo.Modelo()

        boton_salir = Button(
            self.root, text="Salir", command=lambda: objm.b_salir(self.root)
        )
        boton_salir.place(x=x, y=y, w=w, h=h)
