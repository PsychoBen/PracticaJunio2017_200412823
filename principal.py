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
import PilaDeOperaciones
import ColaDeOperaciones
import NodoPilaOperaciones
import ListaDobleCircularUsuario

def validarEntradaCorrectaNumero(mensaje):
    valor1 = -999
    try:
        valor1=int(raw_input(mensaje))
    except ValueError:
        print "**********************************"
        print "    Ingrese un Numero entero      "
        print "**********************************"
    return valor1

def main():

##menu funciona desde aqui

    miListaUsuarios = ListaDobleCircularUsuario.ListaDobleCircularUsuario()
    miListaUsuarios.insertarUsuarioFinal("Alejandra", "Alejandra")
    miListaUsuarios.insertarUsuarioFinal("Julissa", "Julissa")
    miListaUsuarios.insertarUsuarioFinal("Dayanna", "Dayanna")
    miListaUsuarios.insertarUsuarioFinal("Sindy", "Sindy")
    miListaUsuarios.insertarUsuarioFinal("Benjamin", "Benjamin")
    miListaUsuarios.insertarUsuarioFinal("Evelyn", "Evelyn")
    miListaUsuarios.insertarUsuarioFinal("Elizabeth", "Elizabeth")
    miListaUsuarios.insertarUsuarioFinal("Vanessa", "Vanessa")
    miListaUsuarios.insertarUsuarioFinal("Brenda", "Brenda")

    sessionIniciada = False
    opcionPrincipal = 0
    menu = Menus.Menus()
    while(opcionPrincipal!=3):
        opcionPrincipal = menu.menu_principal()

        if opcionPrincipal == 1:
            print("Creando Usuario")
            nombre = raw_input("Ingrese Nombre:   ")
            password = raw_input("Ingrese Password:   ")
            miListaUsuarios.insertarUsuarioFinal(nombre,password)

        elif opcionPrincipal ==2:  ##Ingresa al sistema
            nick = raw_input("Ingrese Usuario:   ")
            clave = raw_input("Ingrese Password:   ")
            if (miListaUsuarios.ingresarSistema(nick, clave)):
                sessionIniciada = True
                opcionUsuario = 0
                usuarioActual = miListaUsuarios.buscarUsuario(nick)  ##obtengo el usuario logueado actual

                while (opcionUsuario!=6):
                    opcionUsuario = menu.menu_usuario()

                    if opcionUsuario == 1:
                        pathArchivo = raw_input("Ingrese el nombre del archivo:   ")
                        ruta = os.path.dirname(os.path.abspath(__file__))
                        ruta = ruta +"\\" + pathArchivo
                        print ruta
                        if os.path.isfile(ruta):
                            miMatriz = Matriz.Matriz()
                            miArchivo = Archivos.Archivos()
                            contenidoArchivo = miArchivo.leerArchivoEntradaCompleto(pathArchivo)
                            filaColumna = miArchivo.obtenerTamanioMatriz(contenidoArchivo)
                            dimensionesMatriz = filaColumna.split(",")
                            filas = int(dimensionesMatriz[0])
                            columnas = int(dimensionesMatriz[1])
                            if usuarioActual.archivoCargado == False:
                                miMatriz.crearMatriz(filas, columnas)
                                usuarioActual.archivoCargado = True
                                usuarioActual.matrizUsuario = miMatriz
                                usuarioActual.matrizTranspuesta = miMatriz.operarMatrizTranspuesta()
                                print "***************************"
                                print "       Matriz Creada       "
                                print "***************************"
                            else:
                                print "*********************************************"
                                print "    Ignorando la Matriz del Nuevo Archivo    "
                                print "*********************************************"
                            operaciones= miArchivo.obtenerOperacionesDesdeArchivo(contenidoArchivo)
                            listadoOperaciones = operaciones.split(",")
                            cadActual = ""
                            for opera in listadoOperaciones:
                                operacionChain = ""
                                cadActual = opera
                                cadActual = cadActual.split()
                                for cd in cadActual:
                                    if operacionChain=="":
                                        operacionChain = cd
                                    else:
                                        operacionChain = operacionChain + " " +cd
                                if operacionChain != "":
                                    usuarioActual.colaOperacionesUser.insertaElementoColaOperaciones(operacionChain)
                            print "***************************"
                            print "   Operacion Ingresada     "
                            print "***************************"
                            print "***************************"
                            print "       Archivo Leido       "
                            print "***************************"
                        else:
                            print "***************************"
                            print "   El archivo no existe    "
                            print "***************************"


                    elif opcionUsuario == 2:
                        if usuarioActual.archivoCargado ==True:
                            print "***************************"
                            print "     Resolver Operacion    "
                            print "***************************"
                            opcionRevolverOperaciones = 0
                            while (opcionRevolverOperaciones!=2):
                                opcionRevolverOperaciones = menu.menu_operacion()
                                if opcionRevolverOperaciones == 1:
                                    if usuarioActual.colaOperacionesUser.tamanioCola > 0:
    ##                                    print "resolviendo siguiente Operacion"
                                        operacionActual = ""
                                        nodoOperacionActual = usuarioActual.colaOperacionesUser.obtenerElementoEliminarElementoColaOperaciones()
        ##                                operacionActual = usuarioActual.colaOperacionesUser.eliminarElementoColaOperaciones()
                                        operacionActual = nodoOperacionActual.operacion
                                        operacionActual = operacionActual.split()
                                        print nodoOperacionActual.operacion
                                        for elemento in operacionActual:
                                            if elemento !="+" and elemento !="-" and elemento !="*":
                                                datoo = int(elemento)
                                                nodoOperacionActual.pilaOperacion.insertarNodoPilaOperacionesFinal(datoo, elemento)
                                            else:
        ##                                        datoo = int(elemento)
                                                nodoOperacionActual.pilaOperacion.insertarNodoPilaOperacionesFinal(0, elemento)
                                        print "******************************************"
                                        resulFinal = 0
                                        print "Al realizar la operacion: " + nodoOperacionActual.operacion
                                        resulFinal = nodoOperacionActual.pilaOperacion.primeroPila.valor
                                        print "El resultado es: " + str(resulFinal)
                                        print "******************************************"
                                    else:
                                        print "***************************"
                                        print "     No hay Operaciones    "
                                        print "***************************"
                            print "***************************"
                            print "Regresando a menu Operacion"
                            print "***************************"
                        else:
                            print "*******************************"
                            print "   Cargue primero un archivo   "
                            print "*******************************"
                    elif opcionUsuario == 3:
                        if usuarioActual.archivoCargado ==True:
                            print "operar matriz"
                            opcionEnMatriz = 0
                            while (opcionEnMatriz !=5):
                                opcionEnMatriz = menu.menu_matriz()

                                if opcionEnMatriz == 1:
                                    print "***************************"
                                    print " Ingresando dato en matriz "
                                    print "***************************"
                                    mensaje = "Ingrese posicion X:   "
                                    posX = validarEntradaCorrectaNumero(mensaje)
                                    while posX == -999:
                                        mensaje = "Ingrese posicion X:   "
                                        posX = validarEntradaCorrectaNumero(mensaje)
    ##                                posX = int(raw_input("Ingrese posicion X:   "))
                                    mensaje = "Ingrese posicion Y:   "
                                    posY = validarEntradaCorrectaNumero(mensaje)
                                    while posY == -999:
                                        mensaje = "Ingrese posicion Y:   "
                                        posY = validarEntradaCorrectaNumero(mensaje)
    ##                                posY = int(raw_input("Ingrese posicion Y:   "))
                                    mensaje = "Ingrese el valor a ingresar X:   "
                                    valorIngresar = validarEntradaCorrectaNumero(mensaje)
                                    while posX == -999:
                                        mensaje = "Ingrese el valor a ingresar X:   "
                                        valorIngresar = validarEntradaCorrectaNumero(mensaje)
    ##                                valorIngresar = int(raw_input("Ingrese el valor a ingresar X:   "))
                                    seInserto = usuarioActual.matrizUsuario.ingresarValorMatriz(posX, posY, valorIngresar)
                                    if seInserto == True:
                                        print "***************************"
                                        print "      Dato Ingresado       "
                                        print "***************************"

                                elif opcionEnMatriz == 2:
                                    print "***************************"
                                    print "     Operar transpuesta    "
                                    print "***************************"
                                    usuarioActual.matrizUsuario.operarMatrizTranspuesta()
                                    print "********************************"

                                elif opcionEnMatriz == 3:
                                    print "*****************************"
                                    print "   Mostrar matriz original   "
                                    print "*****************************"
                                    usuarioActual.matrizUsuario.mostrarMatrizOriginal()
                                    print "********************************"

                                elif opcionEnMatriz == 4:
                                    print "********************************"
                                    print "   Mostrar Matriz transpuesta   "
                                    print "********************************"
                                    usuarioActual.matrizUsuario.mostrarMatrizTranspuesta()
                                    print "********************************"
                            print "***************************"
                            print "Regresando a menu usuario"
                            print "***************************"
                        else:
                            print "*******************************"
                            print "   Cargue primero un archivo   "
                            print "*******************************"

                    elif opcionUsuario == 4:
                        print "*****************************"
                        print " Mostrar Lista de Usuarios   "
                        print "*****************************"
                        cadenaAdelante = miListaUsuarios.mostrarListadoNicksAdelante()
                        cadenaAtras = miListaUsuarios.mostrarListadoNicksAtras()
                        miListaUsuarios.crearArchivoDot()
                        miListaUsuarios.verImagen()
##                        miListaUsuarios.verImagen2()
                        print cadenaAdelante
                        print cadenaAtras
                        print "************************************************"

                    elif opcionUsuario == 5:
                        print "*****************************"
                        print " Mostrar Cola de Operaciones "
                        print "*****************************"
                        usuarioActual.colaOperacionesUser.mostrarColaDeOperaciones()
                        usuarioActual.colaOperacionesUser.mostrarColaDeOperacionesOtra()
                        if usuarioActual.colaOperacionesUser.primeroCola != None:
                            usuarioActual.colaOperacionesUser.crearArchivoDot(usuarioActual.nombreUsuario)
                            usuarioActual.colaOperacionesUser.verImagenCola()
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


if __name__ == '__main__':
    main()
