# 1. Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) y `grosor` (entero). El constructor debe inicializar ambos atributos con valores por defecto. Agregar un método `escribir` que imprima por pantalla la frase "Escribiendo con un lapiz de [color] y grosor [grosor]". Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.
def principal():
    class Lapiz:
        def __init__(self, color='negro', grosor=1):
            self.color = color
            self.grosor = grosor
    
        def __escribir(self):
            print(f"Un lapiz de {self.color} y grosor {self.grosor}")

        def escribirColor(self):
            self.__escribir()

    miLapiz = Lapiz(color='azul', grosor=2)
    miLapiz.escribirColor()

if __name__=="__main__":
    principal()