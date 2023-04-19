# 3.
def principal():
    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

    cSesiones3 = 0
    cList3 = []
    for x in asistencias["Ana"]:
        if x not in asistencias["Luis"]:
            cSesiones3 += 1
            cList3.append(x)
    for x in asistencias["Luis"]:
        if x not in asistencias["Ana"]:
            cSesiones3 += 1
            cList3.append(x)

    print("3.", cList3)

if __name__=="__main__":
    principal()