import os
import sys
#from Varios import principal

from menu import Clases1
from menu import Clases2
from menu import Clases3
from menu import Clases4
from menu import Json1
from menu import Json2
from menu import Json3
from menu import Ejercicio1
from menu import Ejercicio2
from menu import Ejercicio3
from menu import Ejercicio4
from menu import Ejercicio5
from menu import ejercicio6
from menu import ejercicio7
from menu import ejercicio8
from menu import ejercicio9
from menu import ejercicio10
from menu import ejercicio11
from menu import ej1LetraDNI
from menu import ej2Salario
from menu import ej3RutaAvion
from menu import ej4AreaPerimetro
from menu import ej5MayorMenor
from menu import ej6CelAFah
from menu import ej7ParImpar
from menu import ej8BisiestoONo
from menu import ej9Palíndromo
from menu import ej10Ordenar
from menu import ej11Factorial
from menu import ej12Primo
from menu import ej13Cubo
from menu import ej14Suma
from menu import ej15DeterminaNum
from menu import ej16XBar
from menu import ej17Aleatorio
from menu import ej18Anagrama
from menu import ej19Duplicados
from menu import ej20Capicua



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

    #print("1-Ejercicios con colecciones")
    #print("2-Ejercicios con compresión de listas")
    print("3-Ejercicios con JSON")
    print("4-Ejercicios con clases")

    print("0-Salir")

    opcion = input("Seleccione una opción:")

    #if opcion == "1":

        #print("Menu Ejercicios con colecciones")

        #print("0-Salir")

    #elif opcion == "2":

        #print("Menu Ejercicios con compresión de listas")

        #print("0-Salir")

    if opcion == "3":

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