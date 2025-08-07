from verificación import *
import os


class Agenda:
    def __init__(self):
        self.fichero = 'agenda.txt'

    def obtener_telefono(self):
        try:
            f = open(self.fichero, 'r')
        except FileNotFoundError:
            print('¡El fichero ' + self.fichero + ' no existe!\n')
        else:
            directorio = f.readlines()
            f.close()
            directorio = dict([tuple(line.split(',')) for line in directorio])
            persona = introducir_nombre()
            if persona in directorio:
                return print(directorio[persona])
            else:
                print('La persona ' + persona + ' no existe\n')

    def insertar_telefono(self):
        try:
            f = open(self.fichero, 'r')
            f.close()
        except FileNotFoundError:
            return print('¡El fichero ' + self.fichero + ' no existe!\n')
        else:
            f = open(self.fichero, 'a')
            persona = introducir_nombre()
            telefono = introducir_telefono()
            f.write(persona + ',' + telefono + '\n')
            f.close()
            print('El telefono se ha agregado.\n')

    def eliminar_telefono(self):
        try:
            f = open(self.fichero, 'r')
        except FileNotFoundError:
            print('¡El fichero ' + self.fichero + ' no existe!\n')
        else:
            directorio = f.readlines()
            f.close()
            directorio = dict([tuple(line.split(',')) for line in directorio])
            persona = introducir_nombre()
            if persona in directorio:
                del directorio[persona]
                f = open(self.fichero, 'w')
                for nombre, telefono in directorio.items():
                    f.write(nombre + ',' + telefono)
                f.close()
                print('La persona ' + persona + ' ha sido eliminada\n')
            else:
                print('la persona ' + persona + ' no existe\n')

    def crear_directorio(self):
        if os.path.isfile(self.fichero):
            pregunta = input('El fichero ' + self.fichero + ' ya existe.¿Desea reescribirlo? (S/N)?')
            if pregunta == 'N':
                return 'No se ha añadido el fichero porque ya existe.\n'
            else:
                f = open(self.fichero, 'w')
                f.close()
                print('Se ha añadido el fichero agenda.txt\n')
        else:
            f = open(self.fichero, 'w')
            f.close()
            print('Se ha añadido el fichero agenda.txt\n')

    def mostrar_todos(self):
        try:
            f = open(self.fichero, 'r')
        except FileNotFoundError:
            print('¡El fichero ' + self.fichero + ' no existe!\n')
        else:
            directorio = f.readlines()
            f.close()
            directorio = dict([tuple(line.split(',')) for line in directorio])
            print('________AGENDA TELEFONICA________\n')
            for nombre, telefono in directorio.items():
                print(nombre + ' : ' + telefono)


class menu(Agenda):

    def __init__(self):
        super().__init__()

    def menu(self):
        salir = False
        while not salir:
            print('______ MENU AGENDA ______')
            print()
            print("(1) Obtener un Teléfono. \n"
                  "(2) Insertar un Teléfono. \n"
                  "(3) Eliminar un Teléfono. \n"
                  "(4) Crear Agenda. \n"
                  "(5) Mostrar todos. \n"
                  "(6) Salir. \n     ")

            op = str(input('Seleccione una opción: '))

            if op == '1':
                super().obtener_telefono()
            elif op == '2':
                super().insertar_telefono()
            elif op == '3':
                super().eliminar_telefono()
            elif op == '4':
                super().crear_directorio()
            elif op == '5':
                super().mostrar_todos()
            elif op == '6':
                print('Saliendo del menú')
                salir = True
            else:
                print()
                print('Debe seleccionar una opción de 1 a 5')
                print()


obj = menu()

obj.menu()

