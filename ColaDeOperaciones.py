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

class ColaDeOperaciones:

    def __init__(self):
        self.primeroCola = None
        self.ultimoCola = None
        self.tamanioCola = 0

    ## inserta al final de la cola
    def insertaElementoColaOperaciones(self, operacion):
        nuevaOperacion = NodoOperacion.NodoOperacion(operacion)
        if self.primeroCola == None:
            self.primeroCola = nuevaOperacion
            self.ultimoCola = nuevaOperacion
            self.tamanioCola = self.tamanioCola + 1
        else:
            self.ultimoCola.siguienteOperacion = nuevaOperacion
            nuevaOperacion.anteriorOperacion = self.ultimoCola
            self.ultimoCola = nuevaOperacion
            self.tamanioCola = self.tamanioCola + 1

    ##elimina al inicio de la cola
    def eliminarElementoColaOperaciones(self):
        cadenaOperacion = ""
        if self.estaVaciaColaOperaciones() == False:
            cadenaOperacion = self.primeroCola.operacion
            self.primeroCola = self.primeroCola.siguienteOperacion
            self.primeroCola.anteriorOperacion = None
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
            self.primeroCola.anteriorOperacion = None
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
                    cadena = str(aux.operacion)
                else:
                    cadena = cadena + " -> " + str(aux.operacion)
                aux = aux.siguienteOperacion
            print cadena




