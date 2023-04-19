# 1.
import json
def principal():
    '''
    {"nombre": "Juan", "edad": 30, "email": "juan@acme.com", "trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}
    '''

    nombre = input("Ingrese el nombre del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    email = input("Ingrese el correo electrónico del usuario: ")
    empresa = input("Ingrese el nombre de la empresa en la que trabaja el usuario: ")
    puesto = input("Ingrese el puesto del usuario en la empresa: ")

    usuario = {
        "nombre": nombre,
        "edad": edad,
        "email": email,
        "trabajo": {
            "empresa": empresa,
            "puesto": puesto
        }
    }

    usuarioJson = json.dumps(usuario)

    print(usuarioJson)

if __name__=="__main__":
    principal()