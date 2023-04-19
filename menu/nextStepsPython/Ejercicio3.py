#3. Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. 

#El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.
def principal():
    op = "s"
    while op == "s":
        cadena=input("Introduce la cadena de texto :")

        cadena_dividida= cadena.split()

        i=0

        while i<len(cadena_dividida) :
            i+=1
        if(i==0):
            print("La cadena esta vacia")
        elif (i==1):
            print("Hay una palabra en la cadena")
        else:
            print("Hay {numero} palabras en la cadena".format(numero=i))
        choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
        op = choose.lower()