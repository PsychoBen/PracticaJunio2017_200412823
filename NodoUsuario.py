<<<<<<< HEAD
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

class NodoUsuario:

    def __init__(self, nombreUsuario, passUsuario):
        self.nombreUsuario = nombreUsuario
        self.passUsuario = passUsuario
        self.siguiente = None
        self.anterior = None

    def verNodoUsuario(self):
=======
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

class NodoUsuario:

    def __init__(self, nombreUsuario, passUsuario):
        self.nombreUsuario = nombreUsuario
        self.passUsuario = passUsuario
        self.siguiente = None
        self.anterior = None

    def verNodoUsuario(self):
>>>>>>> origin/master
        return {"NameUsuario": self.nombreUsuario, "Contrasenia": str(self.Contrasenia)}