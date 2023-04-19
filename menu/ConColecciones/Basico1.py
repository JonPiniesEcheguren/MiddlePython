## 1. Crear una lista que contenga las letras de una palabra, cada una en mayúscula
def principal():
    word = str(input("Word:"))
    wordUp = word.upper()
    wordList = list(wordUp)

    print(wordList)

if __name__=="__main__":
    principal()