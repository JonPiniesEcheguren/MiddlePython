## 2. Crear un diccionario que contenga el cuadrado de cada número del 1 al 5
def principal():
    numSquare = {}
    for num in range(1, 6):
        numSquare[num] = num**2

    print(numSquare)

if __name__=="__main__":
    principal()