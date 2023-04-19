## 3. Crear un diccionario que contenga los nombres y edades de varias personas
def principal():
    listNames = {}
    while True:
        name = str(input("Input the name:"))
        if name == "Done":
            break
        age = int(input("Input the age:"))
        listNames[name] = age

    for name, age in listNames.items():
        print(f"{name} is {age}")

    print(listNames)

if __name__=="__main__":
    principal()