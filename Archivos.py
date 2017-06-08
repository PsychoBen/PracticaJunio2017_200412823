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

import Matriz
import NodoOperacion
import ColaDeOperaciones

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

    def leerArchivoEntradaCompleto(self, pathArchivo):
        archivoEntrada = open(pathArchivo)
        contenido = ""
        contenido = archivoEntrada.read()
        archivoEntrada.close()
        return contenido

    def obtenerTamanioMatriz(self, contenido):
        filcol = ""
        separadorMatriz = contenido.split("</matriz>")
        matriz = ""
        matriz = separadorMatriz[0]
        separadorMatriz = matriz.split("<matriz>")
        matriz = separadorMatriz[1]
        fila = ""
        columnas = ""
        separadorMatriz = matriz.split("</x>")
        fila = separadorMatriz[0]
        columnas = separadorMatriz[1]
        separadorMatriz = fila.split()
        fila = separadorMatriz[1]
        separadorMatriz = columnas.split()
        columnas = separadorMatriz[1]
        filcol = fila + "," + columnas
        return filcol

    def obtenerOperacionesDesdeArchivo(self, contenido):
        listaOpera = ""
        separadorOperacion = contenido.split("</matriz>")
        operacio = ""
        operacio = separadorOperacion[1]
        separadorOperacion = operacio.split("</operaciones>")
        operacio = separadorOperacion[0]
        separadorOperacion = operacio.split("<operaciones>")
        operacio = separadorOperacion[1]
        operacio = operacio.replace("<operacion>", "")
        operacio = operacio.replace("</operacion>", ",")
        listaOpera = operacio
        return listaOpera







