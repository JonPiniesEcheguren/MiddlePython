import os
import sys
#from Varios import principal

from menu import ej33ListasCompehension as ej33 
from menu import Clases1 as cl1 
from menu import Clases2 as cl2 
from menu import Clases3 as cl3 
from menu import Clases4 as cl4
from menu import Json1 as j1
from menu import Json2 as j2
from menu import Json3 as j3
from menu import ej32 as ej32



while True:
    if sys.platform.startswith("linux"):
        # linux
        os.system('clear') 
    elif sys.platform == "darwin":
        # MAX OS X
        os.system('clear') 
    elif os.name == "nt":
        #Windows, Cigwyin, etc. (32/64-bit)
        os.system('cls') 
    # os.system("cls") #Limpia la pantalla en la consola
    # os.system("clear") #Limpia pantalla consola MAC y Linux
    
    print("Bienvenidos")
    print("Menu principal")

    print("1-Ejercicios con colecciones")
    print("2-Ejercicios con compresión de listas")
    print("3-Ejercicios con JSON")
    print("4-Ejercicios con clases")

    print("0-Salir")

    opcion = input("Seleccione una opción:")

    if opcion == "1":

        print("Menu Ejercicios con colecciones")
        print("1-Primer ejercicio con colecciones")
        print("2-Segundo ejercicio con colecciones")
        print("3-Tercer ejercicio con colecciones")
        print("4-Cuarto ejercicio con colecciones")
        print("5-Quinto ejercicio con colecciones")
        print("6-Sexto ejercicio con colecciones")

        print("0-Salir")

        opcion = input("Seleccione una opción:")

        if opcion == "1":
            ej32.cantSesiones()
        elif opcion == "2":
            ej32.MostSEsiones()
        elif opcion == "3":
            ej32.mostrarSesionesNoAmbos() 
        elif opcion == "4":
            ej32.mostrarSesionesAna()
        elif opcion == "5":
            ej32.mostrarSesionesLuis()
        
    elif opcion == "2":

        print("Menu Ejercicios con compresión de listas")
        print("1-Primer ejercicio básico con compresion de listas")
        print("2-Segundo ejercicio básico con compresion de listas")
        print("3-Tercer ejercicio básico con compresion de listas")
        print("4-Primer ejercicio  avanzado con compresion de listas")
        print("5-Segundo ejercicio avanzado con compresion de listas")
        print("6-Tercer ejercicio avanzado con compresion de listas")

        print("0-Salir")

        opcion = input("Seleccione una opción:")

        if opcion == "1":
            ej33.Palabra2()
        elif opcion == "2":
            ej33.Cuadrado2()
        elif opcion == "3":
            ej33.llamaEdad2() 
        elif opcion == "4":
            ej33.listaNum2() 
        elif opcion == "5":
            ej33.ContarPal2() 
        elif opcion == "6":
            ej33.Ciudad() 

        elif opcion == "0":
            print("Un placer atenderle. Chao!")
            break
            
        continuar=input("Presione enter para continuar...")

    elif opcion == "3":

        print("Menu Ejercicios con JSON")

        print("1-Primer ejercicio JSON")
        print("2-Segundo ejercicio JSON")
        print("3-Tercer ejercicio JSON")
    
        print("0-Salir")
    
        opcion = input("Seleccione una opción:")

        if opcion == "1":
            Json1.principal()
        elif opcion == "2":
            Json2.principal()
        elif opcion == "3":
            Json3.principal() 
        
        elif opcion == "0":
            print("Un placer atenderle. Chao!")
            break
            
        continuar=input("Presione enter para continuar...")

    elif opcion == "4":

        print("Menu Ejercicios con clases")

        print("1-Primer ejercicio clases")
        print("2-Segundo ejercicio clases")
        print("3-Tercer ejercicio clases")
        print("4-Cuarto ejercicio clases")
    
        print("0-Salir")
    
        opcion = input("Seleccione una opción:")
    
        if opcion == "1":
            Clases1.principal()
        elif opcion == "2":
            Clases2.principal()
        elif opcion == "3":
            Clases3.principal()
        elif opcion == "4":
            Clases4.principal() 
        
        elif opcion == "0":
            print("Un placer atenderle. Chao!")
            break

        continuar=input("Presione enter para continuar...")

    elif opcion == "0":
        print("Un placer atenderle. Chao!")
        break

    continuar=input("Presione enter para continuar...")