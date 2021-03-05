#!/env/bin/python 3
#-*- coding: utf-8 -*-

def saludar():
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

def main():
    saludar()
    return 0

if __name__ == "__main__":
    main()
