# 5.
def principal():
    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

    cSesiones5 = 0
    cList5 = []
    for x in asistencias["Luis"]:
        if x not in asistencias["Ana"]:
            cSesiones5 = 0
            cList5.append(x)

    print("5.", cList5)


if __name__=="__main__":
    principal()