import modelo
from tkinter import Button


class VPrincipal(modelo.Modelo):
    def __init__(self, root):
        self.root = root

    def tam_y_tit(self, titulo, tam):
        """Titulo y Tamaño de la ventana"""
        self.root.title(titulo)
        self.root.geometry(tam)

    def b_reservar_v(self, x, y, w, h):
        boton_reservar = Button(
            self.root,
            text="Reservar",
            command=lambda: self.b_reservar_f(),
        )
        boton_reservar.place(x=x, y=y, w=w, h=h)

    def b_baja_v(self, x, y, w, h):
        boton_baja = Button(self.root, text="Baja", command=lambda: self.b_baja_f())
        boton_baja.place(x=x, y=y, w=w, h=h)

    def b_modificar_v(self, x, y, w, h):
        boton_modificar = Button(
            self.root,
            text="Modificar",
            command=lambda: self.b_modificar_f(),
        )
        boton_modificar.place(x=x, y=y, w=w, h=h)

    def b_salir_v(self, x, y, w, h):
        """Crea boton Salir
        Parametros: 1 - Derecha Izquierda, 2 - Arriba Abajo, 3 - Ancho,
        4 - Altura"""

        boton_salir = Button(self.root, text="Salir", command=lambda: self.b_salir_f())
        boton_salir.place(x=x, y=y, w=w, h=h)
