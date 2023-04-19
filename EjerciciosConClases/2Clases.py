# 2. Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) y `color` (cadena de caracteres). 
# El constructor debe recibir ambos atributos como argumentos e inicializarlos. 
# Agregar un método `mostrar_informacion` que imprima por pantalla el nombre y color de la flor. 
# Crear dos objetos de la clase `Flor` e invocar el método `mostrar_informacion` para ambos.
def principal():
    class Flor:
        def __init__(self, nombre, color):
            self.nombre = nombre
            self.color = color
    
        def mostrarInformacion(self):
            print(f"La flor se llama {self.nombre} y su color es {self.color}")

    flor1 = Flor(color='Rojo', nombre='Rosa')
    # flor1 = Flor('Rosa', 'Rojo')
    flor1.mostrarInformacion()

    flor2 = Flor(nombre='Margarita', color='Blanco')
    flor2.mostrarInformacion()

if __name__=="__main__":
    principal()