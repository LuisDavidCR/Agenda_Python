
def nombre_correcto(nombre):
    nombre_c = nombre.translate(str.maketrans('', '', ' '))
    if len(nombre_c) < 2:
        print("El nombre debe tener almenos dos caracteres alfabeticos")
        return False
    for i in range(len(nombre_c)):
        if not ('A' <= nombre_c[i] <= 'z'):
            print("El nombre solo debe tener caracteres alfabeticos")
            return False
    else:
        return True


def introducir_nombre():
    salir = False
    while not salir:
        NOMBRE = str(input("Introduzca el nombre de la persona: "))
        name = NOMBRE.strip()
        salir = nombre_correcto(name)
    return name


def telefono_correcto(telefono):
    if len(telefono) != 9:
        print("El telefono debe contener 9 caracteres")
        return False
    if not telefono.isdigit():
        print("El telefono debe contener solo digitos")
        return False
    else:
        return True


def introducir_telefono():
    salir = False
    while not salir:
        TELEFONO = str(input("Introduzca número de Telefono: "))
        phone = TELEFONO.strip()
        salir = telefono_correcto(phone)
    return phone

