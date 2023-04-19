# 4.
def principal():
    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

    cSesiones4 = 0
    cList4 = []
    for x in asistencias["Ana"]:
        if x not in asistencias["Luis"]:
            cSesiones4 = 0
            cList4.append(x)

    print("4.", cList4)

if __name__=="__main__":
    principal()