from .conneciondb_v2 import ConeccionDB

def crear_tabla():
    conn = ConeccionDB()

    sql = '''
            CREATE TABLE IF NOT EXISTS Autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                nacionalidad TEXT NOT NULL,
                fecha_nacimiento TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Editoriales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                pais TEXT NOT NULL,
                ciudad TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                ano_publicacion TEXT NOT NULL,
                autor_id INTEGER NOT NULL,
                editorial_id INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES Autores(id),
                FOREIGN KEY (editorial_id) REFERENCES Editoriales(id)
            );
            '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()

    except Exception as e:
        print(f"Error al crear las tablas: {e}")

def listar_autores():
    conn = ConeccionDB()
    listar_autores = []
    sql = """
            SELECT * FROM Autores
         """
    
    try:
        conn.cursor.execute(sql)
        listar_autores = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_autores
    except Exception as e:
        print(f"Error al listar autores: {e}")
        return []

def guardar_autor(autor):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Autores (nombre, apellido, nacionalidad, fecha_nacimiento)
            VALUES ('{autor.nombre}', '{autor.apellido}', '{autor.nacionalidad}', '{autor.fecha_nacimiento}');
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al guardar autor: {e}")

def editar_autor(autor, id):
    conn = ConeccionDB()

    sql = f"""
            UPDATE Autores
            SET nombre = '{autor.nombre}', apellido = '{autor.apellido}', nacionalidad = '{autor.nacionalidad}', fecha_nacimiento = '{autor.fecha_nacimiento}'
            WHERE id = {id};
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al editar autor: {e}")

def borrar_autor(id):
    conn = ConeccionDB()

    sql = f"""
            DELETE FROM Autores
            WHERE id = {id};
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al borrar autor: {e}")

class Autor:
    def __init__(self, nombre, apellido, nacionalidad, fecha_nacimiento):
        self.id_autor = None
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f'Autor[{self.nombre} {self.apellido}, {self.nacionalidad}, {self.fecha_nacimiento}]'

