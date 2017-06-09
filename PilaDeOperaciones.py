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


import Matriz
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
        if self.estaVaciaPilaOperaciones==True:
            self.primeroPila = nuevoNodoPila
            self.ultimoPila = nuevoNodoPila
            self.tamanioPila = self.tamanioPila + 1
        else:
            nuevoNodoPila.siguiente = self.primeroPila
##            self.primeroPila.anterior = nuevoNodoPila
            self.primeroPila = nuevoNodoPila
            self.tamanioPila = self.tamanioPila + 1

    def insertarNodoPilaOperacionesFinal(self, valor, operador):
        nuevoNodoPila = NodoPilaOperaciones.NodoPilaOperaciones(valor, operador)
        if operador == "*" or operador == "-" or operador =="+":
            oper1 = self.eliminarNodoPilaOperaciones()
            oper2 = self.eliminarNodoPilaOperaciones()
            print "Operando: "+ str(oper1) + str(operador) + str(oper2)
            self.hacerOperacionPila(oper1, oper2, operador)
        else:
            if self.estaVaciaPilaOperaciones==True:
                self.primeroPila = nuevoNodoPila
                self.ultimoPila = nuevoNodoPila
                self.tamanioPila = self.tamanioPila + 1
            else:
                nuevoNodoPila.siguiente = self.primeroPila
    ##            self.primeroPila.anterior = nuevoNodoPila
                self.primeroPila = nuevoNodoPila
                self.tamanioPila = self.tamanioPila + 1

    def eliminarNodoPilaOperaciones(self):
        operando = 0
        if self.estaVaciaPilaOperaciones() == False:
            self.primeroPila = self.primeroPila.siguiente
##            self.primeroPila.anterior = None
            operando = self.primeroPila.valor
            self.tamanioPila = self.tamanioPila - 1
        else:
            print "cola de operaciones vacia"
        return operando

    def mostrarPilaOperaciones(self):
        if self.estaVaciaPilaOperaciones()==True:
            print "La lista esta vacia"
        else:
            aux = self.primeroPila
            cadena = " "
            while aux != None:
                cadena = cadena + " -> " + str(aux.valor)
                aux = aux.siguiente
            print cadena

    def hacerOperacionPila(self, operando1, operando2, operador):
        resultado = 0
        if operador == "+":
            resultado = operando1 + operando2
        elif operador  == "-":
            resultado == operando1 - operando2
        elif operador == "*":
            resultado = operando1 * operando2







