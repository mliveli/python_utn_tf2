import modelo


class VPrincipal(modelo.Modelo):
    def __init__(self, root):
        self.root = root

    def tam_y_tit(self, titulo, tam):
        """Titulo y Tamaño de la ventana"""
        self.root.title(titulo)
        self.root.geometry(tam)

    def boton_salir_vista(self, x, y, w, h):
        """Crea boton Salir
        Parametros: 1 - Derecha Izquierda, 2 - Arriba Abajo, 3 - Ancho,
        4 - Altura"""
        from tkinter import Button

        boton_salir = Button(self.root, text="Salir", command=lambda: self.b_salir())
        boton_salir.place(x=x, y=y, w=w, h=h)
