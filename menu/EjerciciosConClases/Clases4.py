# 4. Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.
    # La clase deberá tener un método que incorpore el promedio de las notas del alumno.

def principal():
    class Alumno:
        def __init__(self, nombre, apellido, edad, notas):
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.notas = notas
            self.promedio = sum(self.notas) / len(self.notas)
    
        def __str__(self):
            return f"{self.nombre} {self.apellido} - Edad: {self.edad} - Promedio de notas: {self.promedio}"
    
    alumnosLista = [
        {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
        {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
        {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]}
    ]

    listaAlumnos = []
    for alumno in alumnosLista:
        a = Alumno(alumno['nombre'], alumno['apellido'], alumno['edad'], alumno['notas'])
        listaAlumnos.append(a)

    for alumno in listaAlumnos:
        print(alumno)

if __name__=="__main__":
    principal()