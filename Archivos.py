#-------------------------------------------------------------------------------
# Name:        Clase Archivo
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     07/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Archivos:
    def __init__(self):
        pass

    def leerArchivoEntrada(self, pathArchivo):
        archivoEntrada = open(pathArchivo)
        linea = archivoEntrada.readline()
        while linea!= '':
            palabras = linea.split()
            for pal in palabras:
                self.analisarPalabraPruebas(pal)
            linea = archivoEntrada.readline()
        archivoEntrada.close()

    def analisarPalabraPruebas(self, palabra):
        if(palabra=="<archivo>"):
            print "inicio archivo"
        elif(palabra=="</archivo>"):
            print "fin archivo"
        elif(palabra=="<matriz>"):
            print "inicio matriz"
        elif(palabra=="</matriz>"):
            print "fin matriz"
        elif(palabra=="<operaciones>"):
            print "inicio operaciones"
        elif(palabra=="</operaciones>"):
            print "fin operaciones"
        elif(palabra=="<operacion>"):
            print "inicio operacion"
        elif(palabra=="</operacion>"):
            print "fin operacion"
        else:
            print "puta"




