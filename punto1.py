class Producto:
    def __init__(self, nombre, precio, cantidad_stock):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad_stock}"

class Almacen:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        # Verificar si el producto ya existe
        for p in self.productos:
            if p.nombre == producto.nombre:
                print(f"{producto.nombre} ya existe en el almacén.")
                return
        # Agregar el producto al almacén
        self.productos.append(producto)
        print(f"{producto.nombre} ha sido agregado al almacén.")

    def actualizar_stock(self, nombre_producto, nueva_cantidad):
        # Buscar el producto por nombre
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.cantidad_stock = nueva_cantidad
                print(f"Stock de {producto.nombre} actualizado a {nueva_cantidad}.")
                return

        # Si el producto no se encuentra, mostrar un mensaje de error
        print(f"{nombre_producto} no se encontró en el almacén. No se puede actualizar el stock.")

    def mostrar_almacen(self):
        print("Productos en el almacén:")
        for producto in self.productos:
            print(producto)

# Ejemplo de uso
if __name__ == "__main__":
    almacen = Almacen()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Mostrar almacén")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad_stock = int(input("Cantidad del producto en stock: "))
            nuevo_producto = Producto(nombre, precio, cantidad_stock)
            almacen.agregar(nuevo_producto)

        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            nueva_cantidad = int(input("Nueva cantidad en stock: "))
            almacen.actualizar_stock(nombre, nueva_cantidad)

        elif opcion == "3":
            almacen.mostrar_almacen()

        elif opcion == "4":
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
 
   
    