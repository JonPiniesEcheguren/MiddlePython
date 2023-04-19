# 1.
def principal():
    asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}

    cSesiones1 = 0

    for nombre, sesiones in asistencias.items():
        print(nombre,len(sesiones))
        cSesiones1 += len(sesiones)

    print("1.", cSesiones1)

if __name__=="__main__":
    principal()