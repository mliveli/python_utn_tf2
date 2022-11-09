import clase_vista


def ventana_principal(root):
    vp = clase_vista.VPrincipal(root)
    vp.tam_y_tit("Alquiler de Autos - Reservas", "860x600")

    vp.boton(490, 565, 100, 25)
