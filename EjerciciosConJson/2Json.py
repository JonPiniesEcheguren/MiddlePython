# 2.
import json
def principal():
    '''
    {"id": 123456789, "fechayhora": "2023-04-18T12:30:00Z", "monto": 500.25, "tipo": "compra", "producto": {"nombre": "Smartphone", "precio": 450.00, "descripcion": "Un teléfono inteligente de última generación"}}
    '''

    id = int(input("Ingrese el ID: "))
    fechayhora = input("Ingrese la fecha y hora (en formato ISO): ")
    monto = float(input("Ingrese el monto: "))
    tipo = input("Ingrese el tipo de transacción: ")
    nombreProducto = input("Ingrese el nombre del producto: ")
    precioProducto = float(input("Ingrese el precio del producto: "))
    descripcionProducto = input("Ingrese una descripción del producto: ")

    producto = {
        "nombre": nombreProducto,
        "precio": precioProducto,
        "descripcion": descripcionProducto
    }
    transaccion = {
        "id": id,
        "fechayhora": fechayhora,
        "monto": monto,
        "tipo": tipo,
        "producto": producto
    }

    transaccionJson = json.dumps(transaccion)

    print(transaccionJson)

if __name__=="__main__":
    principal()