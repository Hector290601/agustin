#!/env/bin/python 3
# -*- coding: utf-8 -*-
"""
    C:
        estructuras de selección:
            if
            if else
            if else if else
            int = (a>b)?: a:b;
            if (a > b){
                int = a;
            }else{
                int = b;
            }
    Python:
        estructuras de selección:
        if
        if else
        if elif else
        lambdaExpressions (expresiones lambda)
        lambda o1, o2 : expresion
        suma = lambda a, b : a+b
        suma = a+b
"""

a = 0
b = 0

"""
    equivale a:
        a = 0
        b = 0
"""

a = int(input("Ingresa el número a: "))
b = int(input("Ingresa el número b: "))

###########################################if
"""
    if condicion:
        cuerpo
"""
print("if")
if a > b:
    print(a)
if b > a:
    print(b)

########################################if else
"""
    if condicion:
        cuerpo
    else:
        cuerpo
"""
print("if else")
if a > b:
    print(a)
else:
    print(b)
######################################if elif else
"""
    if condicion:
        cuerpo
    elif condicion:
        cuerpo
    else:
        cuerpo
"""
print("if elif else")
if a>b:
    print(a)
elif a == b:
    print("Son iguales XDDDDDDDDDDDDD")
else:
    print(b)
######################################lambda
"""
    valor = lambda x y : x+y
"""
print("Lambda:")
uno = lambda a, b:a>b
print("a>b: " + str(uno(a, b)))
uno = lambda a, b:a<b
print("a<b: " + str(uno(a, b)))
uno = lambda a, b:a==b
print("a==b: " + str(uno(a, b)))
