#!/env/bin/python 3
#-*- coding: utf-8 -*-

from saludoMejorado import *
#import saludoMejorado

"""
    "inyectar" código:
        C:
            #include <stdio.h>
            #include "nombre.h"
        python:
            import nombreLibreria
                                  as apodo
            from nombreLibreria import funcion
                                                as apodo
"""

def main():
    ######aquí escribe el cuerpo
    #saludoMejorado.saludar()
    saludar()
    return 0

if __name__ == "__main__":
    main()

