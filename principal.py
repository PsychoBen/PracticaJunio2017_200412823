#-------------------------------------------------------------------------------
# Name:        Modulo principal
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     05/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import cmd
import copy
import Menus
import Matriz
import Archivos
import NodoUsuario
import NodoOperacion
import ColaDeOperaciones
import PilaDeOperaciones
import NodoPilaOperaciones
import ListaDobleCircularUsuario



def main():

##    miMatriz = Matriz.Matriz()
##    miMatriz.crearMatriz(4,5)
    miArchivo = Archivos.Archivos()
    miArchivo.leerArchivoEntrada("archivoPruebas.xml")


##menu funciona desde aqui

##    miListaUsuarios = ListaDobleCircularUsuario.ListaDobleCircularUsuario()
##
##    opcionPrincipal = 0
##    menu = Menus.Menus()
##    while(opcionPrincipal!=3):
##        opcionPrincipal = menu.menu_principal()
##        if opcionPrincipal == 1:
##            print("Creando Usuario")
##            nombre = raw_input("Ingrese Nombre")
##            password = raw_input("Ingrese Password")
##            miListaUsuarios.insertarUsuarioFinal(nombre,password)
##        elif opcionPrincipal ==2:
##            ## verificar si esxiste el usuario y luego si user y pass son reales
##
##
####            if (miListaUsuarios.verificarUsuarioExiste()==True)
##
##
##            opcionUsuario = 0
##            while (opcionUsuario!=6):
##                opcionUsuario = menu.menu_usuario()
##                if opcionUsuario == 1:
##                    print "leere archivo"
##                elif opcionUsuario == 2:
##                    print "resolver operaciones"
##                    opcionRevolverOperaciones = 0
##                    while (opcionRevolverOperaciones!=2):
##                        opcionRevolverOperaciones = menu.menu_operacion()
##                        if opcionRevolverOperaciones == 1:
##                            print "resolviendo siguiente operacion"
##                    print "Regresando a menu usuario"
##                elif opcionUsuario == 3:
##                    print "operar matriz"
##                    opcionEnMatriz = 0
##                    while (opcionEnMatriz !=5):
##                        opcionEnMatriz = menu.menu_matriz()
##                        if opcionEnMatriz == 1:
##                            print "ingresando dato en matriz"
##                        elif opcionEnMatriz == 2:
##                            print "Operar transpuesta"
##                        elif opcionEnMatriz == 3:
##                            print "Mostrar matriz original"
##                        elif opcionEnMatriz == 4:
##                            print "Mostrar Matriz transpuesta"
##                    print "Regresando a menu usuario"
##                elif opcionUsuario == 4:
##                    print "mostrar usuarios"
##                    miListaUsuarios.mostrarListadoNicks()
##                elif opcionUsuario == 5:
##                    print "mostrar cola"
##            print "sesion cerrada"
##
##
##    print "Hasta Pronto!!!"

## hasta aca



##    miListaUmenusuarios = ListaDobleCircularUsuario.ListaDobleCircularUsuario()
##    miListaUsuarios.crearCarpeta()
##    miListaUsuarios.insertarUsuarioFinal("a1","pass1")
##    miListaUsuarios.insertarUsuarioFinal("a1","pass1")
##    miListaUsuarios.insertarUsuarioFinal("a1","pass1")
##    miListaUsuarios.insertarUsuarioFinal("a2","pass1")
##    miListaUsuarios.insertarUsuarioFinal("a3","pass1")
##    miListaUsuarios.insertarUsuarioFinal("a3","pass1")
##    miListaUsuarios.insertarUsuarioFinal("a4","pass1")
##    longi = miListaUsuarios.obtenerLongitud()
##    print longi
##    miListaUsuarios.mostrarListadoUsuario()
##    miPilaOperaciones = PilaDeOperaciones.PilaDeOperaciones()
##    miPilaOperaciones.mostrarPilaOperaciones()
##    print "************************************"
##    miPilaOperaciones.insertarNodoPilaOperaciones(55, "+")
##    miPilaOperaciones.insertarNodoPilaOperaciones(60, "*")
##    miPilaOperaciones.insertarNodoPilaOperaciones(5, "*")
##    miPilaOperaciones.insertarNodoPilaOperaciones(51, "-")
##    miPilaOperaciones.mostrarPilaOperaciones()
##    print miPilaOperaciones.tamanioPila
##    miPilaOperaciones.eliminarNodoPilaOperaciones()
##    print "************************************"
##    miPilaOperaciones.mostrarPilaOperaciones()
##    print miPilaOperaciones.tamanioPila
##    miPilaOperaciones.agregarCosas()
##    miListaUsuarios.mostrarListadoNicks()




if __name__ == '__main__':
    main()
