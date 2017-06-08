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
        self.matriz = None

    def crearMatriz(self, filas, columnas):
        self.matriz = []
        for x in range(filas):
            self.matriz.append([0] * columnas)
        for fil in range(filas):
            for col in range(columnas):
                self.matriz[fil][col] = -666
        self.matriz[1][1] = 777
        for fiila in self.matriz:
            print fiila



