#-------------------------------------------------------------------------------
# Name:        Clase Nodo Operacion
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     06/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import PilaDeOperaciones
import NodoPilaOperaciones


class NodoOperacion:

    def __init__(self, operacion):
        self.operacion = operacion
        self.pilaOperacion = PilaDeOperaciones.PilaDeOperaciones()
        self.siguienteOperacion = None
        self.anteriorOperacion = None

    def verNodoOperacion(self):
        operaccion = self.operacion
        return operaccion


