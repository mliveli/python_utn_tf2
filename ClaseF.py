class Reserva:
    def __init__(self,tree,con):
        self.tree=tree
        self.con=con


    def f_boton_baja(self,tree,con):
        # ****************************************************************
        # Funcion del boton Baja
        # ****************************************************************
        global id_datos
        cursor = con.cursor()
        mi_id = int(id_datos)
        data = (mi_id,)
        sql = "DELETE FROM reservas WHERE id=?;"
        cursor.execute(sql, data)
        con.commit()

        inicializar_treview(tree,con)
    
