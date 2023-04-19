# 3. Crear un clase que represente los elementos de la lista, con la clase crear objetos que rellenen una lista de productos.
def principal():
    class Producto:
        def __init__(self, nombre, precio, stock):
            self.nombre = nombre
            self.precio = precio
            self.stock = stock
    
        def __str__(self):
            return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"
    
    productosLista = [
        {"nombre": "Leche", "precio": 2.50, "stock": 10},
        {"nombre": "Huevos", "precio": 1.50, "stock": 20},
        {"nombre": "Pan", "precio": 1.00, "stock": 15}
    ]

    listaProductos = []
    for producto in productosLista:
        p = Producto(producto['nombre'], producto['precio'], producto['stock'])
        listaProductos.append(p)

    for producto in listaProductos:
        print(producto)

if __name__=="__main__":
    principal()