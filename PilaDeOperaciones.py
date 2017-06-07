#-------------------------------------------------------------------------------
# Name:        Clase Pilas de operaciones
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     06/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoPilaOperaciones

class PilaDeOperaciones:

    def __init__(self):
        self.tamanioPila = 0
        self.primeroPila = None
        self.ultimoPila = None

    def estaVaciaPilaOperaciones(self):
        if self.primeroPila == None:
            return True
        else:
            return False

    ##inserta en el inicio o top de la pila
    def insertarNodoPilaOperaciones(self, valor, operador):
        nuevoNodoPila = NodoPilaOperaciones.NodoPilaOperaciones(valor, operador)
        if estaVaciaPilaOperaciones==True:
            self.primeroPila = nuevoNodoPila
            self.ultimoPila = nuevoNodoPila
            self.tamanioPila = self.tamanioPila + 1
        else:
            nuevoNodoPila.siguiente = self.primeroPila
            self.primeroPila.anterior = nuevoNodoPila
            self.primeroPila = nuevoNodoPila
            self.tamanioPila = self.tamanioPila + 1

    def eliminarNodoPilaOperaciones(self):
        if self.estaVaciaPilaOperaciones() == False:
            self.primeroPila = self.primeroPila.siguiente
            self.primeroPila.anterior = None
            self.tamanioPila = self.tamanioPila - 1
        else:
            print "cola de operaciones vacia"





