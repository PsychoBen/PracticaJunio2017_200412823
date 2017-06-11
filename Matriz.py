#-------------------------------------------------------------------------------
# Name:        Clase Matriz
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     07/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Matriz:

    def __init__(self):
        self.filas = 0
        self.columnas = 0
        self.transpuesta = None
        self.matriz = None

    def crearMatriz(self, filas, columnas):
        self.matriz = []
        self.transpuesta = []
        self.filas = filas
        self.columnas = columnas
        for x in range(filas):
            self.matriz.append([0] * columnas)
        for fil in range(filas):
            for col in range(columnas):
                self.matriz[fil][col] = -666

        for j in range(columnas):
            self.transpuesta.append([0] * filas)
        for col in range(columnas):
            for fil in range(filas):
                self.transpuesta[col][fil] = -555

    def mostrarMatrizOriginal(self):
        print "************  Matriz Original   **************"
        for fiila in self.matriz:
            print fiila

    def mostrarMatrizTranspuesta(self):
        print "************  transpuesta   **************"
        for col in range(self.columnas):
            for fil in range(self.filas):
                self.transpuesta[col][fil] = self.matriz[fil][col]
        for fiilla in self.transpuesta:
            print fiilla

    def operarMatrizTranspuesta(self):
        print "************  transpuesta   **************"
        for col in range(self.columnas):
            for fil in range(self.filas):
                self.transpuesta[col][fil] = self.matriz[fil][col]
##        for fiilla in self.transpuesta:
##            print fiilla

    def ingresarValorMatriz(self, fil, col, valor):
        sePudo = False
        if fil >= 0 and fil < self.filas and col >= 0 and col < self.columnas:
            self.matriz[fil][col] = valor
            sePudo = True
        else:
            print "**********************************************"
            print "         No se puede ingresar el valor        "
            print "   Las coordenadas estan fuera de la matriz   "
            print "**********************************************"
        return sePudo



