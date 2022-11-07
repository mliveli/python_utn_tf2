from tkinter import messagebox
from datetime import timedelta
import datetime
from datetime import date
import re

reserva = []
id_datos = 0
lista_de_autos = [
    "Vehiculos",
    "Volkswagen",
    "Fiat",
    "Chevrolet",
    "Toyota",
    "Renault",
    "Ford",
]
cont = 0

# ****************************************************************
# Funcion del Boton Disponibilidad
# ****************************************************************
def test_disponibilidad(variable_autos, fecha_inicio, fecha_fin, con):

    lista_de_autos = variable_autos["value"]

    a = fecha_inicio.get().split("/")
    b = fecha_fin.get().split("/")
    x, y, z = a[2], a[1], a[0]
    f_inicio = date(int("20" + x), int(y), int(z))

    f, j, q = b[2], b[1], b[0]
    f_fin = date(int("20" + f), int(j), int(q))

    dias = (f_fin - f_inicio).days
    f_inicio = f_inicio - timedelta(days=1)

    for _ in range(dias + 1):
        f_inicio = f_inicio + timedelta(days=1)

        cursor = con.execute("select vehiculo, inicio, fin from reservas")
        for fila in cursor:
            a = fila[1].split("/")
            b = fila[2].split("/")

            x, y, z = a[2], a[1], a[0]
            base_fecha_inicio = date(int("20" + x), int(y), int(z))

            f, j, q = b[2], b[1], b[0]
            base_fecha_fin = date(int("20" + f), int(j), int(q))

            if f_inicio >= base_fecha_inicio and f_inicio <= base_fecha_fin:
                pos = ""
                for posauto in range(len(lista_de_autos)):
                    if lista_de_autos[posauto] == fila[0]:
                        pos = lista_de_autos[posauto]
                if pos != "":
                    nueva = list()
                    for c in lista_de_autos:
                        if c != pos:
                            nueva.append(c)
                    lista_de_autos = tuple(nueva)

    variable_autos["value"] = lista_de_autos


# ***************************************************************
# Funcion del boton reservar
# ***************************************************************
def f_boton_reservar(
    tree,
    fecha_inicio,
    fecha_fin,
    variable_autos,
    e_telefono,
    e_mail,
    e_nombre,
    e_direccion,
    cal,
    con,
):
    if fecha_inicio.get() == "":
        messagebox.showinfo(
            message="Seleccione una fecha de inicio",
            title="Fecha",
        )
        return

    if fecha_fin.get() == "":
        messagebox.showinfo(
            message="Seleccione una fecha de finalizacion",
            title="Fecha",
        )
        return

    if variable_autos.get() == "Vehiculos":
        messagebox.showinfo(
            message="Seleccione un vehiculo de la lista de vehiculos",
            title="Vehiculo no seleccionado",
        )
        return

    if not test_telefono(e_telefono.get()):
        return

    if not test_mail(e_mail.get()):
        return

    ultimo_id = 0

    cursor = con.cursor()
    datos_reserva = (
        e_nombre.get(),
        e_telefono.get(),
        e_direccion.get(),
        e_mail.get(),
        variable_autos.get(),
        fecha_inicio.get(),
        fecha_fin.get(),
    )
    sql = "INSERT INTO reservas(nombre, direccion, telefono, mail, vehiculo, inicio, fin) VALUES (?,?,?,?,?,?,?)"
    cursor.execute(sql, datos_reserva)
    con.commit()

    # ************ carga de treeview *******************
    cursor = con.cursor()
    cursor.execute("SELECT * FROM reservas")
    for _ in cursor:
        ultimo_id = ultimo_id + 1

    inicializar_treview(tree,con)
    inicializar_calendario(cal,con)
    test_disponibilidad(variable_autos, fecha_inicio, fecha_fin,con)
    e_nombre.delete(0, 710)
    e_telefono.delete(0, 710)
    e_direccion.delete(0, 710)
    e_mail.delete(0, 710)
    fecha_inicio.delete(0, 8)
    fecha_fin.delete(0, 8)

    nueva = list()
    for c in variable_autos["values"]:

        if c != variable_autos.get():
            nueva.append(c)

    tuple(nueva)
    variable_autos["values"] = nueva
    variable_autos.set("Vehiculos")





# ****************************************************************
# Funcion del boton Modificar
# ****************************************************************
def f_boton_modificar(
    tree,
    variable_autos,
    e_telefono,
    e_mail,
    e_nombre,
    e_direccion,
    fecha_inicio,
    fecha_fin,
    con,
):
    if variable_autos.get() == "Vehiculos":
        messagebox.showinfo(
            message="Seleccione un vehiculo de la lista de vehiculos",
            title="Vehiculo no seleccionado",
        )
        return
    global id_datos
    if not test_telefono(e_telefono.get()):
        return

    if not test_mail(e_mail.get()):
        return

    cursor = con.cursor()
    mi_id = int(id_datos)
    datos_reserva = (
        e_nombre.get(),
        e_telefono.get(),
        e_direccion.get(),
        e_mail.get(),
        variable_autos.get(),
        fecha_inicio.get(),
        fecha_fin.get(),
        mi_id,
    )

    sql = "UPDATE reservas SET nombre=?, direccion=?, telefono=?, mail=?, vehiculo=?, inicio=?, fin=? WHERE id=?;"
    cursor.execute(sql, datos_reserva)
    con.commit()

    inicializar_treview(tree,con)


# ****************************************************************
# Funcion del boton Salir
# ****************************************************************
def f_boton_salir(root):
    if messagebox.askyesno("Salir", "Desea Salir?"):
        root.destroy()











# ********************************************************************
# funcion inicializar calendario                                     *
# ********************************************************************
def inicializar_calendario(cal,con):

    fechas = []
    fechas_temporales = []

    cursor = con.execute("select vehiculo, inicio,fin from reservas")
    for fila in cursor:
        a = fila[1].split("/")
        b = fila[2].split("/")

        x, y, z = a[2], a[1], a[0]
        fecha_inicio = date(int("20" + x), int(y), int(z))

        f, j, q = b[2], b[1], b[0]
        fecha_fin = date(int("20" + f), int(j), int(q))

        dias = (fecha_fin - fecha_inicio).days
        fechas_temporales.clear()
        for i in range(dias + 1):
            fechas_temporales.append(
                (fecha_inicio + timedelta(days=i)).strftime("%Y-%m-%d")
            )

        entrada = len(fechas)
        flag = 0
        for t1 in range(dias + 1):
            flag = 0

            for t2 in range(entrada):
                if fechas_temporales[t1] == fechas[t2].split(" ")[0]:
                    fechas[t2] = fechas[t2] + " " + fila[0]
                    flag = 1
            if flag == 0:
                fechas.append(fechas_temporales[t1] + " " + fila[0])

    cal.calevent_remove("all")

    for t1 in range(len(fechas)):
        if len(fechas[t1].split(" ")) == len(lista_de_autos):
            fdesc = fechas[t1].split(" ")
            f = fdesc[0].split("-")

            day = datetime.date(int(f[0]), int(f[1]), int(f[2]))
            cal.calevent_create(day, "", tags="5")
            cal.tag_config("5", background="red")


# ********************************************************************
# Controladores                                                      *
# ********************************************************************


def test_fechas(fecha_inicio, fecha_fin):
    a = fecha_inicio.get().split("/")
    b = fecha_fin.get().split("/")
    x, y, z = a[2], a[1], a[0]
    f_inicio = date(int("20" + x), int(y), int(z))

    x, y, z = b[2], b[1], b[0]

    f_fin = date(int("20" + x), int(y), int(z))

    if f_inicio > f_fin:
        messagebox.showinfo(
            message="La fecha final es anterior a la fecha de inicio",
            title="Fecha erronea",
        )
        return False
    else:
        return True


def test_telefono(tel):
    patron = re.compile(
        r"([+]?\d{7,20})"
    )  # obliga telefono y permite posterior descripcion. opcional "+" antes del telefono.

    if patron.match(tel) is None:
        messagebox.showinfo(
            message="Formato de telefono erroneo",
            title="Error en Telefono",
        )
        return False
    return True


def test_mail(mail):
    patron = re.compile(r".+[@].+[.].+")

    if patron.match(mail) is None:
        messagebox.showinfo(
            message="Formato de e-mail erroneo",
            title="Error en e-mail",
        )
        return False
    return True


# ****************************************************************
# Funcion al seleccionar un tree
# ****************************************************************
def bind_accion(
    tree,
    e_nombre,
    e_telefono,
    e_direccion,
    e_mail,
    fecha_inicio,
    fecha_fin,
    variable_autos,
    boton_reservar,
    con,
):
    global id_datos
    item = tree.focus()
    contenido = tree.item(item)

    if len(contenido.get("values")) > 0:
        id_datos = contenido.get("values")[0]

        cursor = con.cursor()
        cursor = cursor.execute("select * from reservas where id=?", (int(id_datos),))

        fila = cursor.fetchone()

        e_nombre.delete(0, 710)
        e_nombre.insert(0, fila[1])
        e_telefono.delete(0, 710)
        e_telefono.insert(0, fila[2])
        e_direccion.delete(0, 710)
        e_direccion.insert(0, fila[3])
        e_mail.delete(0, 710)
        e_mail.insert(0, fila[4])
        fecha_inicio.delete(0, 8)

        fecha_inicio.insert(0, fila[6])
        fecha_fin.delete(0, 8)
        fecha_fin.insert(0, fila[7])

        test_disponibilidad(variable_autos, fecha_inicio, fecha_fin,con)
        nueva = list()
        for c in variable_autos["values"]:
            nueva.append(c)
        nueva.append(fila[5])
        tuple(nueva)
        variable_autos["values"] = nueva
        variable_autos.set(fila[5])

        boton_reservar.configure(state="disabled")
