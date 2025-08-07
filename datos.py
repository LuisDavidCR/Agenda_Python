import csv

lista = ['David', 'M', '666491285', 'davidluis2436@gmail.com']

# Función para agregar datos


def agregar_datos(x):
    with open('datos.csv', 'a+', newline='') as file:
        write = csv.writer(file)
        write.writerow(x)

# Función para ver datos


def ver_datos():
    datos = []
    with open('datos.csv') as file:
        leer_csv = csv.reader(file)
        for linea in leer_csv:
            datos.append(linea)
    return datos


# función para borrar datos


def borrar_datos(i):


    def agregar_nueva_lista(j):
        with open('datos.csv', 'w', newline='') as file:
            write = csv.writer(file)
            write.writerows(j)

    nueva_lista = []
    telefono = i
    with open('datos.csv', 'r') as file:
        leer_csv = csv.reader(file)
        for linea in leer_csv:
            nueva_lista.append(linea)
            for campo in linea:
                if campo == telefono:
                    nueva_lista.remove(linea)
    agregar_nueva_lista(nueva_lista)


def actualizar_datos(i):


    def agregar_nueva_lista(j):
        with open('datos.csv', 'w', newline='') as file:
            write = csv.writer(file)
            write.writerows(j)

    nueva_lista = []
    telefono = i[0]
    with open('datos.csv', 'r') as file:
        leer_csv = csv.reader(file)
        for linea in leer_csv:
            nueva_lista.append(linea)
            for campo in linea:
                if campo == telefono:
                    nombre = i[1]
                    sexo = i[2]
                    phone = i[3]
                    correo = i[4]

                    datos = [nombre, sexo, phone, correo]

                    index = nueva_lista.index(linea)
                    nueva_lista[index] = datos
    agregar_nueva_lista(nueva_lista)



def buscar_datos(i):
    datos = []
    phone = i

    with open('datos.csv') as file:
        leer_csv = csv.reader(file)
        for linea in leer_csv:
            for campo in linea:
                if campo == phone:
                    datos.append(linea)
    return datos


