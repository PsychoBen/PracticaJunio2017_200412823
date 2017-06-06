#-------------------------------------------------------------------------------
# Name:        Modulo principal
# Purpose:
#
# Author:      Ben Cotto
#
# Created:     05/06/2017
# Copyright:   (c) Ben Cotto
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cmd
import copy
import NodoUsuario
import ListaDobleCircularUsuario


def main():
    miListaUsuarios = ListaDobleCircularUsuario.ListaDobleCircularUsuario()
    miListaUsuarios.crearCarpeta()
    miListaUsuarios.insertarUsuarioFinal("a1","pass1")
    miListaUsuarios.insertarUsuarioFinal("a1","pass1")
    miListaUsuarios.insertarUsuarioFinal("a1","pass1")
    miListaUsuarios.insertarUsuarioFinal("a2","pass1")
    miListaUsuarios.insertarUsuarioFinal("a3","pass1")
    miListaUsuarios.insertarUsuarioFinal("a3","pass1")
    miListaUsuarios.insertarUsuarioFinal("a4","pass1")
    longi = miListaUsuarios.obtenerLongitud()
    print longi
    miListaUsuarios.mostrarListadoUsuario()


if __name__ == '__main__':
    main()

