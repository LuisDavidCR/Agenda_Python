from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datos import *
from verificacion2 import *


co0 = '#FFC832'     # Amarillo
co1 = '#f0f3f5'     # gris
co2 = '#feffff'     # Blanco
co3 = '#38576b'     # azul Oscuro
co4 = '#403d3d'     # Negro
co5 = '#6f9fbd'     # azul
co6 = '#ef5350'     # rojo
co7 = '#93cd95'     # verde


ventana = Tk()
ventana.title('Agenda')
ventana.geometry('500x450')
ventana.configure(background=co1)
ventana.resizable(width=FALSE, height=FALSE)

estilo = Style(ventana)
estilo.theme_use('clam')


marco_sup = Frame(ventana, width=500, height=50, bg=co7, relief='flat')
marco_sup.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

marco_cen = Frame(ventana, width=500, height=150, bg=co1, relief='flat')
marco_cen.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

marco_inf = Frame(ventana, width=500, height=248, bg=co2, relief='flat')
marco_inf.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

# configurando marco superior

l_nombre = Label(marco_sup, text='Agenda Telefónica', anchor=NE, font='normal 25 bold', bg=co7, fg=co4)
l_nombre.place(x=90, y=3)

l_linea = Label(marco_sup, text='', width=500, anchor=NE, font='normal 1', bg=co2, fg=co4)
l_linea.place(x=0, y=46)

global tree


# configurando marco inferior


def mostrar():
    # creando vista de árbol con barras de desplazamiento
    global tree
    list_header = [0, 1, 2]

    df_list = ver_datos()

    tree = ttk.Treeview(marco_inf, selectmode='extended', columns=list_header, show='headings')

    # vertical scrollbar

    vsb = ttk.Scrollbar(marco_inf, orient='vertical', command=tree.yview())

    # horizontal scrollbar

    hsb = ttk.Scrollbar(marco_inf, orient='horizontal', command=tree.xview())

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')


    # encabezado de arbol

    tree.heading(0, text='Nombre', anchor=NW)
    tree.heading(1, text='Teléfono', anchor=NW)
    tree.heading(2, text='Correo', anchor=NW)

    # cuerpo de arbol

    tree.column(0, width=0, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(0, width=170, anchor='nw')

    for item in df_list:
        tree.insert('', 'end', values=item)


mostrar()


def insertar():
    nombre = nombre_correcto(e_nombre.get())
    telefono = telefono_correcto(e_tel.get())
    email = e_email.get()

    datos = [nombre, telefono, email]
    if nombre == '' or telefono == '' or email == '':
        messagebox.showwarning('Datos', 'Por favor completar todos los campos.')
    elif nombre == 1:
        messagebox.showwarning('Error', "El nombre debe tener almenos dos caracteres alfabeticos")
    elif nombre == 2:
        messagebox.showwarning('Error', "El nombre solo debe tener caracteres alfabeticos")
    elif telefono == 1:
        messagebox.showwarning('Error', "El telefono debe contener 9 caracteres")
    elif telefono == 2:
        messagebox.showwarning('Error', "El telefono solo debe tener caracteres alfabeticos")
    else:
        agregar_datos(datos)
        messagebox.showwarning('Datos', 'Los datos han sido agregados.')
        e_nombre.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')

        mostrar()


def actualizar():
    try:
        tree_datos = tree.focus()
        tree_diccionario = tree.item(tree_datos)
        tree_lista = tree_diccionario['values']

        nombre = tree_lista[0]
        telefono = str(tree_lista[1])
        email = tree_lista[2]

        e_nombre.insert(0, nombre)
        e_tel.insert(0, telefono)
        e_email.insert(0, email)

        def confirmar():
            nombre = nombre_correcto(e_nombre.get())
            telefono_nuevo = telefono_correcto(e_tel.get())
            email = e_email.get()

            datos = [telefono, nombre, telefono_nuevo, email]
            if nombre == 1:
                messagebox.showwarning('Error', "El nombre debe tener almenos dos caracteres alfabeticos")
            elif nombre == 2:
                messagebox.showwarning('Error', "El nombre solo debe tener caracteres alfabeticos")
            elif telefono_nuevo == 1:
                messagebox.showwarning('Error', "El telefono debe contener 9 caracteres")
            elif telefono_nuevo == 2:
                messagebox.showwarning('Error', "El telefono solo debe tener caracteres alfabeticos")


            elif nombre == '' or telefono == '' or email == '':
                messagebox.showwarning('Datos', 'Por favor completar todos los campos.')
            else:

                messagebox.showwarning('Datos', 'Los datos han sido actualizados.')
                e_nombre.delete(0, 'end')
                e_tel.delete(0, 'end')
                e_email.delete(0, 'end')
                b_confirmar.destroy()
                actualizar_datos(datos)


            mostrar()

        b_confirmar = Button(marco_cen, command=confirmar, text='Confirmar', width=10, font='Ivy 8 bold', bg=co2, fg=co4,
                           relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=110)

    except IndexError:
    
        messagebox.showwarning('Datos', 'Por favor seleccione una persona de la lista.')


def borrar():
    try:
        tree_datos = tree.focus()
        tree_diccionario = tree.item(tree_datos)
        tree_lista = tree_diccionario['values']

        telefono = str(tree_lista[1])
        borrar_datos(telefono)
        messagebox.showwarning('Datos', 'los datos seleccionados han sido eliminados.')

        for widget in marco_inf.winfo_children():
            widget.destroy()


        mostrar()
    except IndexError:

        messagebox.showwarning('Datos', 'Por favor seleccione una persona de la lista.')


def buscar():
    telefono = e_obtener_telefono.get()

    datos = buscar_datos(telefono)

    tree.delete(*tree.get_children())

    for item in datos:
        tree.insert('', 'end', values=item)

    e_obtener_telefono.delete(0,'end')

# Configurando marco central


l_nombre = Label(marco_cen, text='Nombre ', anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_nombre.place(x=10, y=20)
e_nombre = Entry(marco_cen, width=25, justify='left', font=('', 10), highlightthickness=1)
e_nombre.place(x=80, y=20)

l_tel = Label(marco_cen, text='Teléfono ', anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_tel.place(x=10, y=50)
e_tel = Entry(marco_cen, width=25, justify='left', font=('', 10), highlightthickness=1)
e_tel.place(x=80, y=50)

l_email = Label(marco_cen, text='Correo ', anchor=NW, font='Ivy 10', bg=co1, fg=co4)
l_email.place(x=10, y=80)
e_email = Entry(marco_cen, width=25, justify='left', font=('', 10), highlightthickness=1)
e_email.place(x=80, y=80)

b_obtener_telefono = Button(marco_cen, command=buscar, text='Obtener Telefono', font='Ivy 8 bold', bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_obtener_telefono.place(x=10, y=110)
e_obtener_telefono = Entry(marco_cen, width=16, justify='left', font=('', 11), highlightthickness=1)
e_obtener_telefono.place(x=127, y=110)

b_ver = Button(marco_cen, command=mostrar, text='Ver Datos', width=10, font='Ivy 8 bold', bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_ver.place(x=400, y=20)

b_agregar = Button(marco_cen, command=insertar, text='Agregar', width=10, font='Ivy 8 bold', bg=co5, fg=co4, relief=RAISED, overrelief=RIDGE)
b_agregar.place(x=400, y=50)


b_actualizar = Button(marco_cen, command=actualizar, text='Actualizar', width=10, font='Ivy 8 bold', bg=co0, fg=co4, relief=RAISED, overrelief=RIDGE)
b_actualizar.place(x=400, y=80)

b_borrar = Button(marco_cen, command=borrar, text='Borrar', width=10, font='Ivy 8 bold', bg=co6, fg=co2, relief=RAISED, overrelief=RIDGE)
b_borrar.place(x=400, y=110)




ventana.mainloop()
