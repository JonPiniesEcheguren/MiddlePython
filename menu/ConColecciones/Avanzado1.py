## 1. Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por `"EOI"`, los múltiplos de 5 por `"Cloud"` y los múltiplos de ambos por `"EOICloud"`
def principal():
    listofNumb = []

    for i in range(1, 21):  
        if i % 3 == 0 and i % 5 == 0:
            listofNumb.append("EOICloud")
        elif i % 3 == 0:
            listofNumb.append("EOI")
        elif i % 5 == 0:
            listofNumb.append("Cloud")
        else:
            listofNumb.append(i)

    print(listofNumb)

if __name__=="__main__":
    principal()