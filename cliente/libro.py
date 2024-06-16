import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao_libro import Libro, listar_autores, listar_editoriales, listar_libros, guardar_libro, editar_libro, borrar_libro

def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu=barra, width=300, height=300)
    menu_inicio = tk.Menu(barra, tearoff=0)
    
    # Principal
    barra.add_cascade(label='Inicio', menu=menu_inicio)
    barra.add_cascade(label='Consultas')
    barra.add_cascade(label='Acerca de..')
    barra.add_cascade(label='Ayuda')
    # Botón "Atrás"
    barra.add_cascade(label='Atrás a la pagina de inicio', command=lambda: regresar_principal(root))

    # Submenú
    menu_inicio.add_command(label='Conectar DB')
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)
    


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_libro = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_titulo = tk.Label(self, text="Título: ")
        self.label_titulo.config(font=('Arial', 12, 'bold'))
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text="Género: ")
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=1, column=0, padx=10, pady=10)

        self.label_ano_publicacion = tk.Label(self, text="Año Publicación: ")
        self.label_ano_publicacion.config(font=('Arial', 12, 'bold'))
        self.label_ano_publicacion.grid(row=2, column=0, padx=10, pady=10)

        self.label_autor = tk.Label(self, text="Autor: ")
        self.label_autor.config(font=('Arial', 12, 'bold'))
        self.label_autor.grid(row=3, column=0, padx=10, pady=10)

        self.label_editorial = tk.Label(self, text="Editorial: ")
        self.label_editorial.config(font=('Arial', 12, 'bold'))
        self.label_editorial.grid(row=4, column=0, padx=10, pady=10)
    
    def input_form(self):
        self.titulo = tk.StringVar()
        self.entry_titulo = tk.Entry(self, textvariable=self.titulo)
        self.entry_titulo.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_titulo.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.genero)
        self.entry_genero.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_genero.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.ano_publicacion = tk.StringVar()
        self.entry_ano_publicacion = tk.Entry(self, textvariable=self.ano_publicacion)
        self.entry_ano_publicacion.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_ano_publicacion.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Autores
        autores = listar_autores()
        self.autores = ['Seleccione uno'] + [f"{autor[1]} {autor[2]}" for autor in autores]
        self.entry_autor = ttk.Combobox(self, state="readonly")
        self.entry_autor['values'] = self.autores
        self.entry_autor.current(0)
        self.entry_autor.config(width=25, state='disabled', font=('Arial', 12))
        self.entry_autor.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        # Editoriales
        editoriales = listar_editoriales()
        self.editoriales = ['Seleccione uno'] + [editorial[1] for editorial in editoriales]
        self.entry_editorial = ttk.Combobox(self, state="readonly")
        self.entry_editorial['values'] = self.editoriales
        self.entry_editorial.current(0)
        self.entry_editorial.config(width=25, state='disabled', font=('Arial', 12))
        self.entry_editorial.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=5, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000', state='disabled')
        self.btn_modi.grid(row=5, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000', state='disabled')
        self.btn_cance.grid(row=5, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_titulo.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_ano_publicacion.config(state='normal')
        self.entry_autor.config(state='normal')
        self.entry_editorial.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_titulo.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_ano_publicacion.config(state='disabled')
        self.entry_autor.config(state='disabled')
        self.entry_editorial.config(state='disabled')
        self.entry_autor.current(0)
        self.entry_editorial.current(0)
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.titulo.set('')
        self.genero.set('')
        self.ano_publicacion.set('')
        self.id_libro = None # Reseteamos el ID luego de eliminar
        self.btn_alta.config(state='normal')

    def guardar_campos(self):
        libro = Libro(
            self.titulo.get(),
            self.genero.get(),
            self.ano_publicacion.get(),
            self.entry_autor.current(),
            self.entry_editorial.current()
        )

        if self.id_libro is None:
            guardar_libro(libro)
        else:
            editar_libro(libro, int(self.id_libro))

        self.mostrar_tabla()
        self.bloquear_campos()

    def mostrar_tabla(self):
        self.lista_l = listar_libros()
        self.lista_l.reverse() # Invertimos el orden
        self.tabla = ttk.Treeview(self, columns=('Título', 'Género', 'Año Publicación', 'Autor', 'Editorial'))
        self.tabla.grid(row=6, column=0, columnspan=4, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Título')
        self.tabla.heading('#2', text='Género')
        self.tabla.heading('#3', text='Año Publicación')
        self.tabla.heading('#4', text='Autor')
        self.tabla.heading('#5', text='Editorial')
       
        for l in self.lista_l:
            self.tabla.insert('', 0, text=l[0], values=(l[1], l[2], l[3], l[4], l[5]))
       
        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_registro)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=7, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(self, text='Borrar', command=self.eliminar_registro)
        self.btn_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_delete.grid(row=7, column=1, padx=10, pady=10)

    def editar_registro(self):
        try:
            self.id_libro = self.tabla.item(self.tabla.selection())['text']

            self.titulo_libro_e = self.tabla.item(self.tabla.selection())['values'][0]
            self.genero_libro_e = self.tabla.item(self.tabla.selection())['values'][1]
            self.ano_publicacion_libro_e = self.tabla.item(self.tabla.selection())['values'][2]
            self.autor_libro_e = self.tabla.item(self.tabla.selection())['values'][3]
            self.editorial_libro_e = self.tabla.item(self.tabla.selection())['values'][4]

            self.habilitar_campos()
            self.titulo.set(self.titulo_libro_e)
            self.genero.set(self.genero_libro_e)
            self.ano_publicacion.set(self.ano_publicacion_libro_e)
            self.entry_autor.current(self.autores.index(self.autor_libro_e))
            self.entry_editorial.current(self.editoriales.index(self.editorial_libro_e))

        except:
            pass
    
    def eliminar_registro(self):
        try:
            self.id_libro = self.tabla.item(self.tabla.selection())['text']
            borrar_libro(int(self.id_libro))
            self.mostrar_tabla()
            self.id_libro = None # Reseteamos el ID luego de eliminar
        except:
            pass
        
def regresar_principal(root):
    root.destroy()
    import principal
    principal.main()       

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Gestión de Libros')
    barrita_menu(root)
    app = Frame(root=root)
    app.mainloop()
