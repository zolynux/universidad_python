print("*** Sistema de Inventarios (con funciones) ***")

# Inventario del almacén
inventario = []
titulo = ["Menú", "Mostar", "Agregar", "Buscar", "Salir", "¡Error!"]
id_add = 0


def barrar_titulo(numero: int):
    return "-" * 20 + titulo[numero] + "-" * 20


def mostrar_inventario():
    print(barrar_titulo(1))
    if not inventario:
        print(barrar_titulo(5))
        print(
            "El inventario ha sido vacío."
            "\nDebes ingresar agregado un nuevo producto en 2 punto de opción..."
        )
        return
    for producto in inventario:
        print(
            f"ID: {producto.get('id')}, Nombre: {producto.get('nombre')}, "
            f"Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}"
        )


def agregar_producto():
    print(barrar_titulo(2))
    global id_add
    print("Proporciona nuevo producto:")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    nuevo_producto = {
        "id": id_add,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    inventario.append(nuevo_producto)
    id_add += 1
    print("Producto agregado al inventario")


def buscar_producto_por_id():
    print(barrar_titulo(3))
    if not inventario:
        print(barrar_titulo(5))
        print(
            "El inventario ha sido vacío."
            "\nDebes ingresar agregado un nuevo producto en 2 punto de opción..."
        )
        return
    print("Buscar Producto por ID")
    id_buscar = int(input("Ingresa el ID a buscar: "))
    for producto in inventario:
        if producto.get("id") == id_buscar:
            print("-" * 5, "Información del Producto encontrado:", "" * 5)
            print(
                f"ID: {producto.get('id')}, "
                f"Nombre: {producto.get('nombre')}, "
                f"Precio: ${producto.get('precio')}, "
                f"Cantidad: {producto.get('cantidad')}"
            )
            return
    print("Producto NO encontrado.")


def salir():
    print(barrar_titulo(4))
    print("Has salido el sistema de inventario")


# Programa Principal
if __name__ == "__main__":
    while True:
        print(barrar_titulo(1))
        print("\t1. Mostrar inventario")
        print("\t2. Agregar nuevo producto")
        print("\t3. Buscar producto por ID ")
        print("\t4. Salir")
        try:
            option: int = int(input("Proporciona una opción (1-4): "))
            match option:
                case 1:  # Mostrar un inventario
                    mostrar_inventario()
                case 2:  # Agregar nuevo producto
                    agregar_producto()
                case 3:  # Buscar producto por ID
                    buscar_producto_por_id()
                case 4:  # Salir
                    salir()
                    break

        except ValueError:
            print(barrar_titulo(5))
            print("Entrada no válida. Debes ingresar un número entero.")
