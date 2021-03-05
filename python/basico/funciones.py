#!/env/bin/python 3
#-*- coding: utf-8 -*-

"""
    Funciones:
        c:
            tipoDeRetorno nombreDeFuncion(parametros){
                cuerpo
                retorno opcional;
            }
        python:
            def nombre(parametros):
                cuerpo
                retorno opcional
"""

def suma(a, b):
    return a + b

a = b = c = 0
a = int(input("Ingrese un valor: "))
b = int(input("Ingrese otro valor: "))

c = suma(a, b)

print("La suma es: " + str(c))

def multiplicar(a = 1, b = 1):
    return a * b

a = int(input("Ingrese un valor: "))
b = int(input("Ingrese un valor: "))

c = multiplicar(a, b)

print("La multiplicación es: " + str(c))

c = multiplicar(a)

print("La multiplicación es: " + str(c))

c = multiplicar()

print("La multiplicación es: " + str(c))

"""
    sqrt(4) = 2 = 1 ^ (1/2)
    a^3 = a * a * a
    a^3 = a**100
    ** ~~ ^
"""

def potencias(a = 1, b = 1/2):
    return a ** b

a = int(input("Ingrese un valor: "))
b = int(input("Ingrese una potencia: "))


c = potencias(a, b)

print("La potencia es: " + str(c))

c = potencias(a)

print("La potencia es: " + str(c))




















