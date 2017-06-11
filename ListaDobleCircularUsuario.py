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

    def ingresarSistema(self, nickname, clave):
        loguear = False
        auxx = self.primero
        nickname = nickname.upper()
        if nickname == auxx.nombreUsuario.upper() and clave==auxx.passUsuario:
            loguear = True
        else:
            auxx = self.primero
            auxx = auxx.siguiente
            while (auxx != None and auxx != self.primero):
                nomm1 = auxx.nombreUsuario
                nomm1 = nomm1.upper()
                clav1 = auxx.passUsuario
                if nomm1 == nickname and clav1 == clave:
                    loguear = True
                    break
                elif auxx == self.primero:
                    loguear = True
                    break
                else :
                    auxx = auxx.siguiente
        if loguear == False:
            print "******************************"
            print "    Datos no son correctos   "
        return loguear


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
##        if encontrado == False:
##            print "No se encontro el Usuario"
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
            print ("********************************")
            print ("    Usuario creado con Exito    ")
            print ("********************************")
        else:
            booleano = self.verificarUsuarioExiste(nombreUser)
            if  booleano == True:
                print ("********************************")
                print("   ERROR!!! Usuario ya existe    ")
                print ("********************************")
            else:
                self.ultimo.siguiente = nuevoUsuario
                nuevoUsuario.anterior = self.ultimo
                nuevoUsuario.siguiente = self.primero
                self.ultimo = nuevoUsuario
                self.longitud = self.longitud + 1
                print ("********************************")
                print ("    Usuario creado con Exito    ")
                print ("********************************")


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
        aux = self.primero
        while (aux != None):
            print(aux.verNodoUsuario())
            aux = aux.siguiente
            if aux == self.ultimo:
                print(aux.verNodoUsuario())
                break

    def mostrarListadoNicks(self):
        aux = self.primero
        while (aux != None):
            print(aux.verNickName())
            aux = aux.siguiente
            if aux == self.ultimo:
                print(aux.verNickName())
                break

    def mostrarListadoNicksAdelante(self):
        cadena =""
##        aux = self.primero
        if self.estaVacia () == True:
            print "Lista Vacia"
        else:
            aux = self.primero

            while aux != self.ultimo:
                if aux == self.primero:
                    cadena = aux.nombreUsuario
                else:
                    cadena = cadena + " -> " + aux.nombreUsuario
                aux = aux.siguiente
        cadena = cadena + " -> " + self.ultimo.nombreUsuario
        cadena = cadena + " -> " + self.primero.nombreUsuario
        return cadena

    def mostrarListadoNicksAtras(self):
        cadena =""
##        aux = self.primero
        if self.estaVacia () == True:
            print "Lista Vacia"
        else:
            aux = self.ultimo

            while aux != self.primero:
                if aux == self.ultimo:
                    cadena = aux.nombreUsuario
                else:
                    cadena = cadena + " -> " + aux.nombreUsuario
                aux = aux.anterior
        cadena = cadena + " -> " + self.primero.nombreUsuario
        cadena = cadena + " -> " + self.ultimo.nombreUsuario
        return cadena

    def crearArchivoDot(self):
        if(self.estaVacia==True):
            print "No crear"
        else:
            self.crearCarpeta()
            fileNameArchivo = self.Path + "listadoDobleCircularUsuarios.dot"
            archivoListadoDobleCircular = open(fileNameArchivo, 'w')
            archivoListadoDobleCircular.write(("digraph ListaDobleCircular { rankdir=LR \n node[shape=rectangle color=blue fillcolor = red style=\"rounded,filled\"];\n"))
            self.generarListado(archivoListadoDobleCircular)
            archivoListadoDobleCircular.write(" \n label=\"Listado Doble Circular Usuarios\" \n")
            archivoListadoDobleCircular.write('}')
            archivoListadoDobleCircular.close()

    def generarListado(self, archivo):
        cadena =""
        if self.estaVacia () == True:
            print "Lista Vacia"
        else:
            aux = self.primero

            while aux != self.ultimo:
                if aux == self.primero:
                    cadena = aux.nombreUsuario
                else:
                    cadena = cadena + " -> " + aux.nombreUsuario
                aux = aux.siguiente
        cadena = cadena + " -> " + self.ultimo.nombreUsuario
        cadena = cadena + " -> " + self.primero.nombreUsuario + " \n"
        archivo.write(cadena)
        cadena =""
        if self.estaVacia () == True:
            print "Lista Vacia"
        else:
            aux = self.ultimo
            while aux != self.primero:
                if aux == self.ultimo:
                    cadena = aux.nombreUsuario
                else:
                    cadena = cadena + " -> " + aux.nombreUsuario
                aux = aux.anterior
        cadena = cadena + " -> " + self.primero.nombreUsuario
        cadena = cadena + " -> " + self.ultimo.nombreUsuario + " \n"
        archivo.write(cadena)

    def verImagen(self):
        miComandooo = 'cd C:\Program Files (x86)\Graphviz2.38\bin'
        miComandooo = 'dot -Tgif '+ self.Path+'listadoDobleCircularUsuarios.dot -o '+self.Path+'listadoDobleCircularUsuarios.jpg'
        os.system(miComandooo)
        os.popen(self.Path+'listadoDobleCircularUsuarios.jpg')

    def verImagenCompleta(self):
        miComandooo = 'cd C:\Program Files (x86)\Graphviz2.38\bin'
        miComandooo = 'dot -Tgif '+ self.Path+'listadoDobleCircularUsuariosCompleta.dot -o '+self.Path+'listadoDobleCircularUsuariosCompleta.jpg'
        os.system(miComandooo)
        os.popen(self.Path+'listadoDobleCircularUsuariosCompleta.jpg')

    def verImagen2(self):
        outfd = open(self.Path+ 'archivo_out_vuelo', 'w+')
        errfd = open(self.Path+'archivo_err_vuelo', 'w+')
        miComando= ['dot','-Tgif',self.Path+'listadoDobleCircularUsuarios.dot','-o',self.Path+'listadoDobleCircularUsuarios.jpg']
        subprocess.call(miComando, stdout=outfd, stderr=errfd)
        outfd.close()
        errfd.close()
        fd = open(self.Path+ 'archivo_out_vuelo', 'r')
        output = fd.read()
        fd.close()
        fd = open(self.Path+'archivo_err_vuelo', 'r')
        err = fd.read()
        fd.close()
        print 'stdout: %s\n' % output
        print 'stderr: %s' % err
        os.popen(self.Path+'listadoDobleCircularUsuarios.jpg')


