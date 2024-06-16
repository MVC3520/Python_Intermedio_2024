from .conneciondb_v2 import ConeccionDB

def crear_tabla():
    conn = ConeccionDB()

    sql = '''
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

def listar_editoriales():
    conn = ConeccionDB()
    listar_editoriales = []
    sql = """
            SELECT * FROM Editoriales
         """
    
    try:
        conn.cursor.execute(sql)
        listar_editoriales = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_editoriales
    except Exception as e:
        print(f"Error al listar editoriales: {e}")
        return []

def guardar_editorial(editorial):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Editoriales (nombre, pais, ciudad)
            VALUES ('{editorial.nombre}', '{editorial.pais}', '{editorial.ciudad}');
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al guardar editorial: {e}")

def editar_editorial(editorial, id):
    conn = ConeccionDB()

    sql = f"""
            UPDATE Editoriales
            SET nombre = '{editorial.nombre}', pais = '{editorial.pais}', ciudad = '{editorial.ciudad}'
            WHERE id = {id};
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al editar editorial: {e}")

def borrar_editorial(id):
    conn = ConeccionDB()

    sql = f"""
            DELETE FROM Editoriales
            WHERE id = {id};
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al borrar editorial: {e}")

class Editorial:
    def __init__(self, nombre, pais, ciudad):
        self.id_editorial = None
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad

    def __str__(self):
        return f'Editorial[{self.nombre}, {self.pais}, {self.ciudad}]'
