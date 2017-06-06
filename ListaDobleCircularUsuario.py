#-------------------------------------------------------------------------------
# Name:        Clase Lista Doble Circular de Usuarios
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     05/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import NodoUsuario
import subprocess
import os.path
import errno
import os

class ListaDobleCircularUsuario:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.longitud = 0
        self.Path="C:/Proyecto/EDDVacasJunio/"

    def verificarUsuarioExiste(self, nombre):
        encontrado = False
        auxx = self.primero
        nombre = nombre.upper()
        if nombre == auxx.nombreUsuario.upper():
            encontrado = True
        else:
            auxx = self.primero
            auxx = auxx.siguiente
            while (auxx != None and auxx != self.primero):
                nomm1 = auxx.nombreUsuario
                nomm1 = nomm1.upper()
                if nomm1 == nombre:
                    encontrado = True
                    break
                elif auxx == self.primero:
                    encontrado = True
                    break
                else :
                    auxx = auxx.siguiente
        if encontrado == False:
            print "No se encontro el Usuario"
        return encontrado

    def estaVacia(self):
        if (self.primero == None):
            return True
        else:
            return False

    def insertarUsuarioFinal(self, nombreUser, passUser):
        nuevoUsuario = NodoUsuario.NodoUsuario(nombreUser, passUser)
        if self.estaVacia()==True:
            self.primero = nuevoUsuario
            self.ultimo = nuevoUsuario
            self.longitud = self.longitud + 1
        else:
            booleano = self.verificarUsuarioExiste(nombreUser)
            if  booleano == True:
                print("Usuario ya existe")
            else:

                self.ultimo.siguiente = nuevoUsuario
                nuevoUsuario.anterior = self.ultimo
                nuevoUsuario.siguiente = self.primero
                self.ultimo = nuevoUsuario

##                aux_ult = self.ultimo
##                aux_pri = self.primero

                self.longitud = self.longitud + 1

    def buscarUsuario(self, nombre):
        encontrado = None
        auxx = self.primero
        nombre = nombre.upper()
        while (auxx !=None):
            nomm1 = auxx.nombreUsuario
            nomm1=nomm1.upper()
            if nomm1==nombre:
                encontrado=auxx
                break
            else :
                auxx=auxx.siguiente
        if encontrado==None:
            print "No se encontro el Usuario"
        return encontrado



    def obtenerLongitud(self):
        return self.longitud

    def crearCarpeta(self):
        try: os.makedirs(self.Path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def mostrarListadoUsuario(self):

        print("***************")
        aux = self.primero
        while (aux != None and aux != self.primero):
            print(aux.verNodoUsuario()+" ->")
            aux = aux.siguiente


