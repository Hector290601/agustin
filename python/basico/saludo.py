#!/env/bin/python 3
#-*- coding: utf-8 -*-

"""
    crear funciones:
        def nombre(parametros):
            cuerpo
            return opcional
    Entradas del teclado (std en C)
    dondeGuardar = input("Mensaje")
    C:
        int int1 = 0;
        printf("Ingrese un número; \n");
        scanf("%d", &int1);
    python:
        numero = input("Ingresa un número: ")
    Python no necesita forzosamente que se declaren las variables antes de usarlas
    +: cadena -> concatena; numero -> lo opera
    *: cadena -> lo multiplica; numero -> lo opera
    hola * 5 = hola hola hola hola hola
    if en python:
    if parametros:
        cuerpo
    elif parametros:         #no existe el else if          elif replaza a else if
    else:
        cuerpo
    Castear:        #esto es cambiar el tipo de dato
        C:
            int = (int) char;
        Python:
            int = int(char)
"""

nombre = input("¿Cómo te llamas?: ")
print("Hola " + nombre + " contenando")
print("Hola %s con format"%nombre)

edad = int(input("¿Qué edad tienes?: "))     #input regresa una cadena, no un entero ni flotante, ni nada más, siempre una cadena
print(edad)

if edad > 18:
    print("Puedes tomar")
elif edad == 18:
    print("No tomes mucho")
else:
    print("Vete a tu casa, escuincle")

