

def nombre_correcto(nombre):
    nombre_c = nombre.translate(str.maketrans('', '', ' '))
    if len(nombre_c) < 2:
        return 1
    for i in range(len(nombre_c)):
        if not ('A' <= nombre_c[i] <= 'z'):
            return 2
    else:
        return nombre


def telefono_correcto(telefono):
    if len(telefono) != 9:
        return 1
    if not telefono.isdigit():
        return 2
    else:
        return telefono

def verificar(datos):
    if datos[0] == 1:
        messagebox.showwarning('Error', "El nombre debe tener almenos dos caracteres alfabeticos")
    elif datos[0] == 2:
        messagebox.showwarning('Error', "El nombre solo debe tener caracteres alfabeticos")
    elif datos[2] == 1:
        messagebox.showwarning('Error', "El telefono debe contener 9 caracteres")
    elif datos[2] == 2:
        messagebox.showwarning('Error', "El telefono solo debe tener caracteres alfabeticos")


