# 2.
def principal():
    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}
    
    cSesiones2 = 0
    cList2 = []
    for x in asistencias["Ana"]:
        if x in asistencias["Luis"]:
            cSesiones2 += 1
            cList2.append(x)

    print("2.", cList2)

if __name__=="__main__":
    principal()