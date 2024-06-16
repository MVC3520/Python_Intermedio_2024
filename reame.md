# Gestor de Biblioteca

Este proyecto es una aplicación de escritorio para gestionar una biblioteca, permitiendo la administración de autores, libros y editoriales. La aplicación está construida con Python y utiliza `Tkinter` para la interfaz gráfica de usuario y `sqlite3` para la base de datos.

## Requisitos

* Python 3.x
* `tkinter` (incluido en la instalación estándar de Python)
* `sqlite3` (incluido en la instalación estándar de Python)

## Instalación

No se requiere instalación adicional de paquetes si ya tienes Python instalado. `tkinter` y `sqlite3` vienen incluidos con Python.

## Uso

1. **Ejecuta la aplicación:** Abre una terminal y ejecuta el script `main.py`.
2. **Interfaz de Usuario:**
   * La aplicación tiene tres pestañas principales: `Autores`, `Libros`, y `Editoriales`.
   * Cada pestaña permite utilizar los botones principales (`Nuevo`, `Guardar`, `Editar`, `Borrar` y `Cancelar`) para gestionar los registros en la base de datos. Además, se puede navegar hacia atrás utilizando el menú que se muestra en la vista ("Atrás a la página de inicio").

## Librerías Utilizadas tros en la base de datos.

### Tkinter

`tkinter` es la biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). Proporciona un conjunto de herramientas para construir aplicaciones con ventanas, botones, cuadros de texto y otros widgets.

### SQLite3

`sqlite3` es una biblioteca estándar de Python que proporciona una interfaz para interactuar con bases de datos SQLite. Es una base de datos ligera y fácil de usar, adecuada para pequeñas aplicaciones y prototipos.

## Estructura del Proyecto

* `main.py`: El archivo principal que contiene el código de la aplicación.
* `README.md`: Este archivo de documentación.
* `biblioteca.db`: Archivo de base de datos SQLite que se crea al ejecutar la aplicación.

## Funcionalidades

* **Autores:** Permite agregar, editar, guardar y eliminar registros de autores, con campos como nombre, apellido, nacionalidad y fecha de nacimiento.
* **Libros:** Permite agregar, editar, guardar y eliminar registros de libros, con campos como título, género, año de publicación e ID del autor.
* **Editoriales:** Permite agregar, editar, guardar y eliminar registros de editoriales, con campos como nombre, país y ciudad.
