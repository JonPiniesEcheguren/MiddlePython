## 2. Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella
def principal():
    list = ["apple", "banana", "cherry", "banana", "apple", "cherry"]
    wordCounts = {}

    for word in list:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

    print(wordCounts)

if __name__=="__main__":
    principal()