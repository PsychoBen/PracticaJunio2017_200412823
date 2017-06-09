#-------------------------------------------------------------------------------
# Name:        Clase de menus
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     07/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Menus:
    def __init__(self):
        print ""

    def menu_principal(self):
        print "Bienvenido al Sistema Practica 1"
        print "**********************************"
        print "        Menu Principal            "
        print "**********************************"
        print "1.  Crear Usuario "
        print "2.  Ingresar al Sistema"
        print "3.  Salir del Programa"
        mensaje = "Menu principal:   "
        opcion = self.validarEntradaNumero(mensaje)
##        opcion = input("Menu principal:   ")
        return opcion

    def menu_usuario(self):
        print "**********************************"
        print "           Menu Usuario           "
        print "**********************************"
        print "1. Leer Archivo"
        print "2. Resolver Operaciones"
        print "3. Operar la Matriz"
        print "4. Mostrar Usuarios"
        print "5. Mostrar Cola"
        print "6. Cerrar Session"
        mensaje = "Operaciones de Usuario:   "
        opcion = self.validarEntradaNumero(mensaje)
##        opcion = input("Operaciones de Usuario:   ")
        return opcion

    def menu_operacion(self):
        print "**********************************"
        print "     Menu Resolver Operaciones    "
        print "**********************************"
        print "1. Operar Siguiente"
        print "2. Regresar"
        mensaje = "Resolver Operaciones:   "
        opcion = self.validarEntradaNumero(mensaje)
##        opcion = input("Resolver Operaciones:   ")
        return opcion

    def menu_matriz(self):
        print "**********************************"
        print "        Menu Operar Matriz        "
        print "**********************************"
        print "1. Ingresar Dato"
        print "2. Operar Transpuesta"
        print "3. Mostrar Matriz Original"
        print "4. Mostrar Martiz Transpuesta"
        print "5. Regresar"
        mensaje = "Operar la Matriz:   "
        opcion = self.validarEntradaNumero(mensaje)
##        opcion = input("Operar la Matriz:   ")
        return opcion

    def validarEntradaNumero(self, mensaje):
        valor1 = 999
        try:
            valor1=int(raw_input(mensaje))
        except ValueError:
            print "**********************************"
            print "    Ingrese un Numero entero      "
            print "**********************************"
        return valor1

