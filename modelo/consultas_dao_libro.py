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

def listar_libros():
    conn = ConeccionDB()
    listar_libros = []
    sql = """
            SELECT l.id, l.titulo, l.genero, l.ano_publicacion, a.nombre || ' ' || a.apellido AS autor, e.nombre AS editorial
            FROM Libros l
            INNER JOIN Autores a ON l.autor_id = a.id
            INNER JOIN Editoriales e ON l.editorial_id = e.id;
         """
    
    try:
        conn.cursor.execute(sql)
        listar_libros = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_libros
    except Exception as e:
        print(f"Error al listar libros: {e}")
        return []

class Libro:
    def __init__(self, titulo, genero, ano_publicacion, autor_id, editorial_id):
        self.id_libro = None
        self.titulo = titulo
        self.genero = genero
        self.ano_publicacion = ano_publicacion
        self.autor_id = autor_id
        self.editorial_id = editorial_id

    def __str__(self):
        return f'Libro[{self.titulo}, {self.genero}, {self.ano_publicacion}, {self.autor_id}, {self.editorial_id}]'

def guardar_libro(libro):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Libros (titulo, genero, ano_publicacion, autor_id, editorial_id)
            VALUES('{libro.titulo}', '{libro.genero}', '{libro.ano_publicacion}', {libro.autor_id}, {libro.editorial_id});
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al guardar libro: {e}")

def editar_libro(libro, id):
    conn = ConeccionDB()

    sql = f"""
            UPDATE Libros
            SET titulo = '{libro.titulo}', genero = '{libro.genero}', ano_publicacion = '{libro.ano_publicacion}', autor_id = {libro.autor_id}, editorial_id = {libro.editorial_id}
            WHERE id = {id};
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al editar libro: {e}")

def borrar_libro(id):
    conn = ConeccionDB()

    sql = f"""
            DELETE FROM Libros
            WHERE id = {id};
            """
    
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error al borrar libro: {e}")
