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
##    filaColumna = ""
##    operaciones = ""
##
##    miArchivo = Archivos.Archivos()
##    contenidoArchivo = miArchivo.leerArchivoEntradaCompleto("archivoPruebas.xml")
##    filaColumna = miArchivo.obtenerTamanioMatriz(contenidoArchivo)
##    dimensionesMatriz = filaColumna.split(",")
##    filas = int(dimensionesMatriz[0])
##    columnas = int(dimensionesMatriz[1])
##    miMatriz.crearMatriz(filas, columnas)
##    miMatriz.ingresarValorMatriz(0,0,999)
##    miMatriz.ingresarValorMatriz(1,1,859)
##    miMatriz.mostrarMatrizTranspuesta()
##    miMatriz.mostrarMatrizOriginal()
##    operaciones= miArchivo.obtenerOperacionesDesdeArchivo(contenidoArchivo)
##    print operaciones


##menu funciona desde aqui

    miListaUsuarios = ListaDobleCircularUsuario.ListaDobleCircularUsuario()
    miListaUsuarios.insertarUsuarioFinal("papa", "a1")
    miListaUsuarios.insertarUsuarioFinal("pepe", "a2")
    miListaUsuarios.insertarUsuarioFinal("pepito", "pepito666")
    miListaUsuarios.insertarUsuarioFinal("pipi", "a4")
    miListaUsuarios.insertarUsuarioFinal("popo", "a5")
    miListaUsuarios.insertarUsuarioFinal("pupu", "a6")

    sessionIniciada = False
    opcionPrincipal = 0
    menu = Menus.Menus()
    while(opcionPrincipal!=3):
        opcionPrincipal = menu.menu_principal()

        if opcionPrincipal == 1:
            print("Creando Usuario")
            nombre = raw_input("Ingrese Nombre")
            password = raw_input("Ingrese Password")
            miListaUsuarios.insertarUsuarioFinal(nombre,password)

        elif opcionPrincipal ==2:  ##Ingresa al sistema
            nick = raw_input("Ingrese Usuario")
            clave = raw_input("Ingrese Password")
            if (miListaUsuarios.ingresarSistema(nick, clave)):
                sessionIniciada = True
                opcionUsuario = 0
                usuarioActual = miListaUsuarios.buscarUsuario(nick)  ##obtengo el usuario logueado actual

                while (opcionUsuario!=6):
                    opcionUsuario = menu.menu_usuario()

                    if opcionUsuario == 1:
                        print "leere archivo"

                    elif opcionUsuario == 2:
                        print "resolver operaciones"
                        opcionRevolverOperaciones = 0
                        while (opcionRevolverOperaciones!=2):
                            opcionRevolverOperaciones = menu.menu_operacion()
                            if opcionRevolverOperaciones == 1:
                                print "resolviendo siguiente operacion"
                        print "***************************"
                        print "Regresando a menu usuario"
                        print "***************************"

                    elif opcionUsuario == 3:
                        print "operar matriz"
                        opcionEnMatriz = 0
                        while (opcionEnMatriz !=5):
                            opcionEnMatriz = menu.menu_matriz()
                            if opcionEnMatriz == 1:
                                print "ingresando dato en matriz"
                            elif opcionEnMatriz == 2:
                                print "Operar transpuesta"
                            elif opcionEnMatriz == 3:
                                print "Mostrar matriz original"
                            elif opcionEnMatriz == 4:
                                print "Mostrar Matriz transpuesta"
                        print "***************************"
                        print "Regresando a menu usuario"
                        print "***************************"

                    elif opcionUsuario == 4:
                        print "*****************************"
                        print " Mostrar Lista de Usuarios   "
                        print "*****************************"
                        cadenaAdelante = miListaUsuarios.mostrarListadoNicksAdelante()
                        cadenaAtras = miListaUsuarios.mostrarListadoNicksAtras()
                        print cadenaAdelante
                        print cadenaAtras
                        print "************************************************"

                    elif opcionUsuario == 5:
                        print "*****************************"
                        print " Mostrar Cola de Operaciones "
                        print "*****************************"
                        miListaUsuarios.colaOperacionesUser.mostrarColaDeOperaciones()
                        print "********************************************************"

                sessionIniciada == False
                print "*******************************"
                print "       Sesion Finalizada       "
                print "*******************************"

            else:
                print "Verifique los datos no se puede Ingresar al Sistema"
                print "******************************************************"
                opcionPrincipal = 0

    print "Hasta Pronto!!!"

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
