import itertools
import os
import platform

if platform.system() == "Windows":
    os.system("cls")
    print("Estás en Windows")
elif platform.system() == "Darwin":
    os.system("clear")
    print("Estás en MacOS")
elif platform.system() == "Linux":
    os.system("clear")
    print("Estás en Linux")

# * Ejercicios básicos:

# ? Hacer los siguientes ejercicios básicos con compresión de colecciones y mostrar su equivalente con el bucle

 #! 1. Crear una lista que contenga las letras de una palabra, cada una en mayúscula:
# ¿: Op 1:


def Palabra():
    palabra = input("Intoduce una palabra1: ").upper()
    lista1 = []
    for letra in palabra:
        lista1.append(letra)
    print(f"Versión bucle: {lista1}")


if __name__ == "__main__":
    Palabra()

# #¿: Op 2:


def Palabra2():
    palabra2 = input("Intoduce una palabra2: ")
    lista2 = [letra for letra in palabra2.upper()]
    print(f"Versión compresión: {lista2}")
    print("_____________________________________________________________________")


if __name__ == "__main__":
    Palabra2()

# #! 2. Crear un diccionario que contenga el cuadrado de cada número del 1 al 5:
# #¿: Op 1:


def Cuadrado1():
    numCuad1 = {}
    for i in range(1, 6):
        numCuad1[i] = i**2
    print(f"Versión bucle: {numCuad1}")


if __name__ == "__main__":
    Cuadrado1()

# #¿: Op 2:


def Cuadrado2():
    numCuad2 = {}
    numCuad2 = {i: i**2 for i in range(1, 6)}
    print(f"Versión compresión: {numCuad2}")
    print("_____________________________________________________________________")


if __name__ == "__main__":
    Cuadrado2()

# #! 3. Crear un diccionario que contenga los nombres y edades de varias personas:
# #¿: Op 1:


def Edad(lista1, lista2):
    nomEdad = {}
    count = 0
    for nom in lista1:
        count += 1
        for edad in itertools.islice(lista2, count):
            nomEdad[nom] = edad
    print(f"Versión bucle: {nomEdad}")


def llamaEdad():
    lista1 = ["Eli", "David", "Carla", "Vicent"]
    lista2 = [25, 45, 35, 50, 23]
    Edad(lista1, lista2)


if __name__ == "__main__":
    llamaEdad()


# #¿: Op 2:
def Edad2(lista3, lista4):
    nomEdad = {nom: lista4[count] for count, nom in enumerate(lista3, start=0)}

    print(f"Versión compresión: {nomEdad}")
    print("_____________________________________________________________________")


def llamaEdad2():
    lista3 = ["Eli", "David", "Carla", "Vicent"]
    lista4 = [25, 45, 35, 50]
    Edad2(lista3, lista4)


if __name__ == "__main__":
    llamaEdad2()

# #* Ejercicios avanzados:

# #? Hacer los siguientes ejercicios básicos con compresión de colecciones y mostrar su equivalente con el bucle .

# #! 1. Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por `"EOI"`, los múltiplos de 5 por `"Cloud"` y los múltiplos de ambos por `"EOICloud"`.
# ¿: Op 1:


def listaNum():
    lista = []
    count = 0
    for i in range(1, 21):
        lista.append(i)

        if i % 3 == 0 and i % 5 == 0:
            lista[count] = "EOICloud"
        elif i % 3 == 0:
            lista[count] = "EOI"
        elif i % 5 == 0:
            lista[count] = "Cloud"
        count += 1
    print(f"Versión bucle: {lista}")


if __name__ == "__main__":
    listaNum()

# #¿: Op 2:


def listaNum2():
    lista2 = ["EOICloud" if i % 3 == 0 and i % 5 == 0 else "EOI" if i %
              3 == 0 else "Cloud" if i % 5 == 0 else i for i in range(1, 21)]
    print(f"Versión compresión: {lista2}")
    print("_____________________________________________________________________")


if __name__ == "__main__":
    listaNum2()


#! 2. Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella.
# ¿: Op 1:
def ContarPal():
    palabras = input("Introduce las palabras: ").split()
    contarPal = {}
    for palabra in palabras:
        contarPal[palabra] = palabras.count(palabra)
    print(f"Versión bucle: {contarPal}")


if __name__ == "__main__":
    ContarPal()

# ¿: Op 2:


def ContarPal2():
    palabras2 = input("Introduce las palabras: ").split()
    contarPal = {palabra: palabras2.count(palabra) for palabra in palabras2}
    print(f"Versión compresión: {contarPal}")


if __name__ == "__main__":
    ContarPal2()

#! 3. Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema. **Nota** el diccionario deberá ordenarse por su clave.
#!     - `Nueva York` - La Estatua de la Libertad
#!     - `Tokio` - La flor del cerezo
#!     - `París` - La Torre Eiffel
#!     - `Londres` - El Big Ben
#!     - `Sídney` - La Opera de Sídney
#!     - `Buenos Aires` - El Obelisco
#!     - `Johannesburgo` - El león
#!     - `Moscú` - El Kremlin
#!     - `Ámsterdam` - Los molinos de viento
#!     - `Dubai` - El Burj Khalifa


def Ciudad():

    ciudadEmbl = {
        "Nueva York": "La Estatua de la Libertad",
        "Tokio": "La flor del cerezo",
        "París": "La Torre Eiffel",
        "Londres": "El Big Ben",
        "Sídney": "La Opera de Sídney",
        "Buenos Aires": "El Obelisco",
        "Johannesburgo": "El león",
        "Moscú": "El Kremlin",
        "Ámsterdam": "Los molinos de viento",
        "Dubai": "El Burj Khalifa"
    }
    ciudadEmblrdenado = dict(sorted(ciudadEmbl.items()))
    ciudadEmb = input(
        "Introduce las ciudades separadas con comas: ").lower().split(", ")
    print(ciudadEmb)
    for key, value in ciudadEmblrdenado.items():
        if key.lower() in ciudadEmb:

            print(f"{key}: {value}")


if __name__ == "__main__":
    Ciudad()
