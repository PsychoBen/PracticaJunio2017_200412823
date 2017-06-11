#-------------------------------------------------------------------------------
# Name:        Clase Cola de Operaciones
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     06/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoOperacion
import subprocess
import os.path
import errno
import os

class ColaDeOperaciones:

    def __init__(self):
        self.primeroCola = None
        self.ultimoCola = None
        self.tamanioCola = 0
        self.Path="C:/Proyecto/EDDVacasJunio/"

    ## inserta al final de la cola
    def insertaElementoColaOperaciones(self, operacion):
        nuevaOperacion = NodoOperacion.NodoOperacion(operacion)
        if self.primeroCola == None:
            self.primeroCola = nuevaOperacion
            self.ultimoCola = nuevaOperacion
            self.tamanioCola = self.tamanioCola + 1
        else:
            self.ultimoCola.siguienteOperacion = nuevaOperacion
##            nuevaOperacion.anteriorOperacion = self.ultimoCola
            self.ultimoCola = nuevaOperacion
            self.tamanioCola = self.tamanioCola + 1

    ##elimina al inicio de la cola
    def eliminarElementoColaOperaciones(self):
        cadenaOperacion = ""
        if self.estaVaciaColaOperaciones() == False:
            cadenaOperacion = self.primeroCola.operacion
            self.primeroCola = self.primeroCola.siguienteOperacion
##            self.primeroCola.anteriorOperacion = None
            self.tamanioCola = self.tamanioCola - 1
        else:
            print "cola de operaciones vacia"
        return cadenaOperacion

    def obtenerElementoEliminarElementoColaOperaciones(self):
        noditoCola = None
        if self.estaVaciaColaOperaciones() == False:
            cadenaOperacion = self.primeroCola.operacion
            noditoCola = self.primeroCola
            self.primeroCola = self.primeroCola.siguienteOperacion
##            self.primeroCola.anteriorOperacion = None
            self.tamanioCola = self.tamanioCola - 1

        else:
            print "cola de operaciones vacia"
        return noditoCola

    def estaVaciaColaOperaciones(self):
        if self.primeroCola == None:
            return True
        else:
            return False

    def getTamanioColaOperaciones(self):
        return self.tamanioCola

    def mostrarColaDeOperaciones(self):
        if self.estaVaciaColaOperaciones()==True:
            print "La cola de operaciones esta vacia"
        else:
            aux = self.primeroCola
            cadena = ""
            while aux !=None:
                if aux == self.primeroCola:
                    cadena = " \" " + str(aux.operacion) +" \" "
                else:
                    if str(aux.operacion)=="":
                        cadena = cadena
                    else:
                        cadena = cadena + " -> " + " \" " + str(aux.operacion) +" \" "
                aux = aux.siguienteOperacion
            print cadena

    def mostrarColaDeOperacionesOtra(self):
        contador = 0
        if self.estaVaciaColaOperaciones()==True:
            print "La cola de operaciones esta vacia"
        else:
            aux = self.primeroCola
            while aux !=None:
                cadena = "Operacion indice " + str(contador) + ": " + str(aux.operacion)
                print cadena
                contador = contador + 1
                aux = aux.siguienteOperacion

    def crearCarpeta(self):
        try: os.makedirs(self.Path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def crearArchivoDotCompleto(self, padre):
        if(self.estaVaciaColaOperaciones==True):
            print "No crear"
        else:
            self.crearCarpeta()
            fileNameArchivo = self.Path + "colaOperacionesUsuarioCompleto.dot"
            archivoColaOperaciones = open(fileNameArchivo, 'w')
            cluster = "Cola_"+ padre
            archivoColaOperaciones.write(("subgraph ColaOperacionesUsuario { rankdir=LR \n node[shape=rectangle color=blue fillcolor = red style=\"rounded,filled\"];\n"))
            archivoListadoDobleCircular.write("graph [label=\"Cola operaciones\", labelloc=t, fontsize=10]; \n")
            self.generarListadoCompleto(archivoColaOperaciones)
            archivoColaOperaciones.write('}')
            archivoColaOperaciones.write(padre + " -> " + cluster)
##            archivoColaOperaciones.close()

    def verImagenCompleto(self):
        miComandooo = 'cd C:\Program Files (x86)\Graphviz2.38\bin'
        miComandooo = 'dot -Tgif '+ self.Path+'colaOperacionesUsuarioCompleto.dot -o '+self.Path+'colaOperacionesUsuarioCompleto.jpg'
        os.system(miComandooo)
        os.popen(self.Path+'colaOperacionesUsuarioCompleto.jpg')

    def generarListado(self, archivo):
        cadena =""
        if self.estaVaciaColaOperaciones () == True:
            print "Cola Vacia"
        else:
            aux = self.primeroCola
            while aux != self.ultimoCola:
                if aux == self.primeroCola:
                    cadena = " \"" + aux.operacion +" \""
                else:
                    cadena = cadena + " -> " + " \""+ aux.operacion +" \""
                aux = aux.siguienteOperacion
        cadena = cadena + " -> " + " \"" + self.ultimoCola.operacion +" \""
        archivo.write(cadena)

    def generarListadoPruebas(self, archivo):
        cadena =""
        if self.estaVaciaColaOperaciones () == True:
            print "Cola Vacia"
        else:
            aux = self.primeroCola
            contador = 0
            texto = ""
            while aux != self.ultimoCola:
                texto = str(contador) + "[label= " + " \"" + aux.operacion +" \"" +"]\n"
                archivo.write(texto)
                if aux == self.primeroCola:
                    cadena =  str(contador) +" "
                else:
                    cadena = cadena + " -> " + str(contador) +" "
                contador = contador + 1
                aux = aux.siguienteOperacion
        cadena = cadena + " -> " + str(contador + 1) + "\n "
        archivo.write(cadena)
        texto = str(contador + 1) + "[label= " + " \"" + self.ultimoCola.operacion +" \"" +"]\n"
        archivo.write(texto)

    def generarListadoCompleto(self, archivo):
        cadena =""
        if self.estaVaciaColaOperaciones () == True:
            print "Cola Vacia"
        else:
            aux = self.primeroCola
            while aux != self.ultimoCola:
                if aux == self.primeroCola:
                    cadena = " \"" + aux.operacion +" \""
                else:
                    cadena = cadena + " -> " + " \""+ aux.operacion +" \""
                aux = aux.siguienteOperacion
        cadena = cadena + " -> " + " \"" + self.ultimoCola.operacion +" \""
        archivo.write(cadena)

    def crearArchivoDot(self , padre):
        if(self.estaVaciaColaOperaciones==True):
            print "No crear"
        else:
            self.crearCarpeta()
            fileNameArchivo = self.Path + "colaOperacionesUsuario.dot"
            archivoColaOperaciones = open(fileNameArchivo, 'w')
            archivoColaOperaciones.write(("digraph ColaOperacionesUsuario { rankdir=LR \n node[shape=rectangle color=blue fillcolor = cadetblue3 style=\"rounded,filled\"];\n"))
##            self.generarListado(archivoColaOperaciones)
            self.generarListadoPruebas(archivoColaOperaciones)
            archivoColaOperaciones.write("\n label=\"Cola operaciones del usuario: "+ padre + " \"  \n")
            archivoColaOperaciones.write('}')
            archivoColaOperaciones.close()

    def verImagenCola(self):
        miComandooo = 'cd C:\Program Files (x86)\Graphviz2.38\bin'
        miComandooo = 'dot -Tgif '+ self.Path+'colaOperacionesUsuario.dot -o '+self.Path+'colaOperacionesUsuario.jpg'
        os.system(miComandooo)
        os.popen(self.Path+'colaOperacionesUsuario.jpg')






