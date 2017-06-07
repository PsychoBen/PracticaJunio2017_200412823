#-------------------------------------------------------------------------------
# Name:        Clase Nodo Pila Operaciones
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     06/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class NodoPilaOperaciones:
    def __init__(self, valor, operador):
        self.valor = valor
        self.operador = operador
        self.esOperador = False
        self.siguiente = None
        self.anterior = None

    def mostrarNodoPilaOperacion(self):
        return self.valor
