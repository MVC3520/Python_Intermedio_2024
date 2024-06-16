import sqlite3

class ConeccionDB():
    def __init__(self):
        self.base_datos = 'ddbb/biblioteca.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    
    def cerrar_con(self):
        self.conexion.commit()
        self.conexion.close()


