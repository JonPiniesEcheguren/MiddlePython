# MiddlePython

### Instrucciones de instalación:

- Clonar el repositorio:

  - `git clone https://github.com/JonPiniesEcheguren/MiddlePython.git` 

- Crear y activar el entorno virtual:

  - Versión Python 3.11.2

  - Windows

    - `python -m venv env` 
    - `env\scripts\activate.bat` (Windows command line)
    - `env\scripts\activate.ps1` (Windows PowerShell)

  - MacOs / Linux

    - `python3 -m venv env`

    - `source env\bin\activate`

- Instalar las librerias
  - `pip install -r requirements.txt`

- Instrucciones de ejecución
  - `py main.py`

### Colaboradores:

- Cristian Miron
- Jon Pinies Echeguren
- Mohamed Amri
- Víctor Manuel Pérez Rosa

Ejercicios de carácter puramente educativo.

## Los programas presentes en este repositorio fueron creados para resolver los siguientes problemas: 

1. Calcular la letra del DNI Español
2. Calcular el salario de un empleado
3. Determinar la ruta para llegar a una ciudad por avión. [Con base de datos]
4. Calcula el área y perímetro de un círculo dado su radio.
5. Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor. 
6. Crea un programa en Python que convierta grados Celsius a Fahrenheit.
7. Dado un número entero, crea un programa en Python que determine si es par o impar.
8. Crea un programa en Python que determine si un año es bisiesto o no.
9. Crea un programa en Python que determine si una cadena de texto es un palíndromo o no.
10. Dada una lista de nombres, crea un programa en Python que ordene la lista alfabéticamente.
11. Crea un programa en Python que calcule el factorial de un número entero.
12. Dado un número entero, crea un programa en Python que determine si es primo o no.
13. Crea un programa en Python que calcule el área y volumen de un cubo dado su lado.
14. Dada una lista de números enteros, crea un programa en Python que calcule la suma de todos los números pares de la lista.
15. Crea un programa en Python que determine si un número es positivo, negativo o cero.
16. Dada una lista de números enteros, crea un programa en Python que calcule la media de la lista.
17. Crea un programa en Python que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El programa en Python deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.
18. Crea un programa en Python que determine si una cadena de texto es un anagrama de otra cadena de texto.
19. Dada una lista de números enteros, crea un programa en Python que elimine los números duplicados de la lista.
20. Crea un programa en Python que determine si un número es capicúa o no.
1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero.  El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.
2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.
3. Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.

4. Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30").  La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.

5. Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh"). El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.

6. Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado. El programa debe utilizar un bucle `for` para sumar los números.

7. Crea un programa que le pida al usuario una cadena de caracteres y luego imprima cada carácter en una línea separada. El programa debe utilizar un bucle `for` para recorrer la cadena.

8. Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres. El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.

9. Crea un programa en Python donde la entrada sean una cadena de caracteres, una palabra y una palabra de reemplazo ,el resultado debe ser la cadena con todas las ocurrencias de la palabra reemplazadas por otra palabra. El programa debe utilizar un bucle `while` para buscar todas las ocurrencias de la palabra y reemplazarlas.

10. Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal.  La función debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.

11. Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3. El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar los números.


## Ejercicios sobre JSON

Dados los siguientes JSON, deberá crear un programa en python, que pida la información por teclado, conforme un objeto Python y al final convierta el objeto conformado al JSON correspondiente: 

### Programa 1: Información sobre un usuario: 

El JSON generado deberá ser.

```
{"nombre": "Juan", "edad": 30, "email": "juan@acme.com", "trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}
```

### Programa 2: Transacción financiera:

El JSON generado deberá ser.

```
{"id": 123456789, "fechayhora": "2023-04-18T12:30:00Z", "monto": 500.25, "tipo": "compra", "producto": {"nombre": "Smartphone", "precio": 450.00, "descripcion": "Un teléfono inteligente de última generación"}}
```

### Programa 3: Información medica de paciente:

El JSON generado deberá ser:

```
{"nombre": "Pedro", "apellido": "Pérez", "edad": 45, "peso": 80.5, "altura": 1.75, "historial_medico": {"alergias": ["penicilina", "mariscos"], "problemas_cardiacos": false, "medicamentos": [{"nombre": "Ibuprofeno", "dosis": "200mg"}, {"nombre": "Paracetamol", "dosis": "500mg"}]}, "ultima_revision": "2022-10-01", "proximo_turno": "2023-05-15"}
```

**NOTA: **Para comprobar los programas anteriores, cree un programa en python, que pida un JSON como texto y lo convierta en un objeto Python y lo muestre por pantalla.

## Ejercicios básicos de clases

### Programa 1: 
 Crear una clase `Lapiz` que tenga los atributos `color` (cadena de caracteres) y `grosor` (entero). El constructor debe inicializar ambos atributos con valores por defecto. Agregar un método `escribir` que imprima por pantalla la frase "Escribiendo con un lapiz de [color] y grosor [grosor]". Crear un objeto de la clase `Lapiz` e invocar el método `escribir`.

### Programa 2: 
 Crear una clase `Flor` que tenga los atributos `nombre` (cadena de caracteres) y `color` (cadena de caracteres). El constructor debe recibir ambos atributos como argumentos e inicializarlos. Agregar un método `mostrar_informacion` que imprima por pantalla el nombre y color de la flor. Crear dos objetos de la clase `Flor` e invocar el método `mostrar_informacion` para ambos.

### Programa 3: 
Dada la siguiente lista de productos. 

   ```
   productos_lista = [
       {"nombre": "Leche", "precio": 2.50, "stock": 10},
       {"nombre": "Huevos", "precio": 1.50, "stock": 20},
       {"nombre": "Pan", "precio": 1.00, "stock": 15}
   ]
   ```

   Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de productos.

### Programa 4: 
Dada la siguiente lista de alumnos. 

   ```
   alumnos_lista = [
       {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "notas": [7, 8, 9]},
       {"nombre": "María", "apellido": "González", "edad": 22, "notas": [6, 9, 10]},
       {"nombre": "Pedro", "apellido": "García", "edad": 21, "notas": [5, 7, 8]} ]
   ```
   Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de alumnos.
   La clase deberá tener un método que incorpore el promedio de las notas del alumno.

   

​	



​	

