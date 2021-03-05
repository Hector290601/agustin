#!/env/bin/python 3
#-*- coding: utf-8 -*-

"""
    Iteración:
    C:
    for
    while
    do while
    Python:
    for
    while
"""

numero = 0
numero = int(input("Dame un número: "))

##########for
"""
    for objetoIterable:
        cuerpo
    C:
    for(int i = 0; i < numero; i++){
    }
    objetos iterables:
    rangos:
        range(inicio (opcional), fin (obligatorio), paso(opcional))
        range regresa una lista de números desde el número inicio (por defecto es 0) hasta el número final -1 con aumentos de paso
        range(0, 10, 1) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        range(5) = [0, 1, 2, 3, 4]
        range(0, 50, 10) = [0, 10, 20, 30, 40]
    listas
"""
print("Con for:")
for i in range(1, 11, 1):
    print(numero * i)

##########while
"""
    while condicion:
        cuerpo
"""
print("Con while:")
i = 1
while i <= 10:
    print(numero * i)
    i += 1 ##suma en una sóla línea i++ i = i + 1




































