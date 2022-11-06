import sqlite3


class Reserva:
    def __init__(self, tree, con):
        self.tree = tree
        self.con = con

    def crear_base(self):
        # ********************************************************************
        # funcion CREAR base de datos                                        *
        # ********************************************************************
        self.con = sqlite3.connect("reservas.db")
        print("Conectado")
        return self.con

    def crear_tabla(self):
        # ********************************************************************
        # funcion CREAR tabla principal (unica en este caso)                 *
        # e inicializar treeview                                             *
        # ********************************************************************
        cursor = self.con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS reservas(\
            id integer PRIMARY KEY,\
            nombre VARCHAR(128),\
            direccion VARCHAR(128),\
            telefono VARCHAR(128),\
            mail VARCHAR(128),\
            vehiculo VARCHAR(128),\
            inicio VARCHAR(128),\
            fin VARCHAR(128))"
        cursor.execute(sql)
        self.con.commit()

    def f_boton_baja(
        self,
    ):
        # ****************************************************************
        # Funcion del boton Baja
        # ****************************************************************
        global id_datos
        cursor = self.con.cursor()
        mi_id = int(id_datos)
        data = (mi_id,)
        sql = "DELETE FROM reservas WHERE id=?;"
        cursor.execute(sql, data)
        self.con.commit()

        self.inicializar_treview()

    def inicializar_treview(self):
        # ****************************************************************
        # Inicializa el treeview cargando desde la base de datos
        # ****************************************************************
        for item in self.tree.get_children():
            self.tree.delete(item)
        cursor = self.con.execute("select id,vehiculo, inicio,fin from reservas")
        for fila in cursor:
            self.tree.insert("", "end", values=(fila[0], fila[1], fila[2], fila[3]))
