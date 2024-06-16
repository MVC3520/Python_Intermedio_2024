import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao_autor import Autor, listar_autores, guardar_autor, editar_autor, borrar_autor
from datetime import datetime

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
        self.id_autor = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.config(font=('Arial', 12, 'bold'))
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)

        self.label_nacionalidad = tk.Label(self, text="Nacionalidad: ")
        self.label_nacionalidad.config(font=('Arial', 12, 'bold'))
        self.label_nacionalidad.grid(row=2, column=0, padx=10, pady=10)

        self.label_fecha_nacimiento = tk.Label(self, text="Fecha de Nacimiento: ")
        self.label_fecha_nacimiento.config(font=('Arial', 12, 'bold'))
        self.label_fecha_nacimiento.grid(row=3, column=0, padx=10, pady=10)

    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable=self.apellido)
        self.entry_apellido.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.nacionalidad = tk.StringVar()
        self.entry_nacionalidad = tk.Entry(self, textvariable=self.nacionalidad)
        self.entry_nacionalidad.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_nacionalidad.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        self.fecha_nacimiento = tk.StringVar()
        self.entry_fecha_nacimiento = tk.Entry(self, textvariable=self.fecha_nacimiento)
        self.entry_fecha_nacimiento.config(width=50, state='disabled', font=('Arial', 12))
        self.entry_fecha_nacimiento.grid(row=3, column=1, padx=10, pady=10, columnspan=2)


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
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_nacionalidad.config(state='normal')
        self.entry_fecha_nacimiento.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_nacionalidad.config(state='disabled')
        self.entry_fecha_nacimiento.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.nombre.set('')
        self.apellido.set('')
        self.nacionalidad.set('')
        self.fecha_nacimiento.set('')
        self.id_autor = None
        self.btn_alta.config(state='normal')


    def guardar_campos(self):
        # Obtener los valores de los campos del formulario
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        nacionalidad = self.nacionalidad.get()
        fecha_nacimiento = self.fecha_nacimiento.get()

        # Crear un objeto Autor con los datos recolectados
        autor = Autor(
            nombre=nombre,
            apellido=apellido,
            nacionalidad=nacionalidad,
            fecha_nacimiento=fecha_nacimiento
        )

        # Guardar o editar el autor según corresponda
        if self.id_autor is None:
            guardar_autor(autor)
        else:
            editar_autor(autor, int(self.id_autor))

        # Actualizar la tabla y bloquear los campos después de guardar
        self.mostrar_tabla()
        self.bloquear_campos()


    def mostrar_tabla(self):
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Apellido', 'Nacionalidad', 'Fecha de Nacimiento'))
        self.tabla.grid(row=6, column=0, columnspan=5, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=5, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Apellido')
        self.tabla.heading('#3', text='Nacionalidad')
        self.tabla.heading('#4', text='Fecha de Nacimiento')

        self.actualizar_tabla()

        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_registro)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=7, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(self, text='Borrar', command=self.eliminar_registro)
        self.btn_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_delete.grid(row=7, column=1, padx=10, pady=10)


    def actualizar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())  # Limpiar tabla antes de cargar datos
        self.lista_autores = listar_autores()

        for autor in self.lista_autores:
            self.tabla.insert('', 'end', text=autor[0], values=(autor[1], autor[2], autor[3], autor[4]))


    def editar_registro(self):
        try:
            seleccion = self.tabla.selection()
            if seleccion:
                self.id_autor = self.tabla.item(seleccion)['text']
                self.nombre.set(self.tabla.item(seleccion)['values'][0])
                self.apellido.set(self.tabla.item(seleccion)['values'][1])
                self.nacionalidad.set(self.tabla.item(seleccion)['values'][2])
                self.fecha_nacimiento.set(self.tabla.item(seleccion)['values'][3])
                self.habilitar_campos()
        except Exception as e:
            print(f"Error al editar registro: {e}")

    def eliminar_registro(self):
        try:
            self.id_autor = self.tabla.item(self.tabla.selection())['text']
            borrar_autor(int(self.id_autor))
            self.mostrar_tabla()
            self.id_autor = None
        except Exception as e:
            print(f"Error al eliminar registro: {e}")

def regresar_principal(root):
    root.destroy()
    import principal
    principal.main() 
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Gestión de Autores')
    barrita_menu(root)
    app = Frame(root=root)
    app.mainloop()
