import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from cliente.autor import Frame as FrameAutor
from cliente.editor import Frame as FrameEditorial
from cliente.libro import Frame as FrameLibro
from cliente.autor import barrita_menu as barrita_menu_autor
from cliente.editor import barrita_menu as barrita_menu_editor
from cliente.libro import barrita_menu as barrita_menu_libro

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f'+{x}+{y}')

def main():
    ventana = tk.Tk()
    ventana.title('Gestión de Biblioteca')
    ventana.iconbitmap('img/libro.ico')
    ventana.resizable(0, 0)

    # Cargar y configurar imagen de fondo
    imagen_fondo = Image.open('fondo.png')
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
    fondo_label = tk.Label(ventana, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Estilo para los widgets de ttk
    estilo = ttk.Style()
    estilo.configure('TButton', background='#1C500B', foreground='#FFFFFF', font=('Arial', 12, 'bold'))
    estilo.map('TButton', background=[('active', '#3FD83F')], foreground=[('active', '#000000')])

    # Configurar barra de menú
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)

    # Menú Autores
    menu_autores = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Autores', menu=menu_autores)
    menu_autores.add_command(label='Gestionar Autores', command=lambda: abrir_frame(FrameAutor, barrita_menu_autor))

    # Menú Editoriales
    menu_editoriales = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Editoriales', menu=menu_editoriales)
    menu_editoriales.add_command(label='Gestionar Editoriales', command=lambda: abrir_frame(FrameEditorial, barrita_menu_editor))

    # Menú Libros
    menu_libros = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Libros', menu=menu_libros)
    menu_libros.add_command(label='Gestionar Libros', command=lambda: abrir_frame(FrameLibro, barrita_menu_libro))

    # Función para abrir el frame correspondiente
    def abrir_frame(Frame, barrita_menu_func):
        # Limpiar ventana antes de abrir un nuevo frame
        for widget in ventana.winfo_children():
            widget.destroy()

        # Llamar a la función de barrita_menu correspondiente
        barrita_menu_func(ventana)

        # Crear instancia del frame y mostrarlo
        frame = Frame(ventana)
        frame.pack(expand=True, fill='both')

        # Centrar la ventana después de mostrar el frame
        center_window(ventana)

    # Centrar la ventana inicialmente
    center_window(ventana)

    ventana.mainloop()

if __name__ == '__main__':
    main()
