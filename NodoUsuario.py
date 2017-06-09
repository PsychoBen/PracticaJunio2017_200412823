#-------------------------------------------------------------------------------
# Name:        Clase Nodo Usuario
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     05/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoOperacion
import ColaDeOperaciones


class NodoUsuario:

    def __init__(self, nombreUsuario, passUsuario):
        self.nombreUsuario = nombreUsuario
        self.passUsuario = passUsuario
        self.siguiente = None
        self.anterior = None
        self.archivoCargado = False
        self.colaOperacionesUser = ColaDeOperaciones.ColaDeOperaciones()
        self.matrizUsuario = None
        self.matrizTranspuesta = None


    def verNodoUsuario(self):
        return {"Nickname": self.nombreUsuario,"password ": str(self.passUsuario)}

    def verNickName(self):
        nick = self.nombreUsuario
        return nick

    def obtenerColaUsuario(self):
        return self.colaOperacionesUser

    def obtenerMatrizUsuario(self):
        return self.matrizUsuario

    def obtenerMatrizTranpuesta(self):
        return self.matrizTranspuesta
