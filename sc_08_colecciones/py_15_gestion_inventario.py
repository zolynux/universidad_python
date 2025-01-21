print("*** Sistema de Inventario ***")

inventario = []

while True:
    print(
        f"""{'-'* 10}Inventario de menú:{'-'* 10}
1. Mostrar el Inventario
2. Ingresar los productos
3. Buscar ID
4. Salir"""
    )
    try:
        opcion: int = int(input("Ingresa un número de menú (opción): "))
        match opcion:
            case 1:
                if not inventario:
                    print(
                        "\nInventario no tiene los productos.\nPor favor ingresar los productos en la opción de 2...\n"
                    )
                else:
                    # Mostrar el inventario detalle
                    print(f"\n{'='*10} Inventario detallado {'='*10}")
                    for producto in inventario:
                        print(f"ID: {producto.get('id')}")
                        print(f"Nombre: {producto.get('nombre')}")
                        print(f"Precio: ${producto.get('precio'):.2f}")
                        print(f"Cantidad: {producto.get('cantidad')}")
                        print("-" * 20)
                    print("=" * 42)
                print()
            case 2:
                # Definimos a los productos agregan a pedir al usuario
                numero_productos = int(
                    input("Cuanto producto deseas agregar al inventario?: ")
                )

                # Iteramos a las variables de productos para diccionario
                for indice in range(numero_productos):
                    print(f"Proporciona los valores del producto {indice + 1} ")
                    nombre = input("Nombre: ")
                    precio = float(input("Precio: "))
                    cantidad = int(input("Cantidad: "))
                    # Creamos el diccionario con el detalle del producto
                    producto = {
                        "id": indice,
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad,
                    }
                    # Agregamos el nuevo producto al inventario
                    inventario.append(producto)
                # Mostrar el inventario inicial
                print(f"\nInventario inicial: {inventario}\n")
            case 3:
                if not inventario:
                    print(
                        "\nInventario no tiene los productos.\nPor favor ingresar los productos en la opción de 2...\n"
                    )
                else:
                    # Buscar un producto por ID
                    id_buscar = int(input("\nIngresa el ID del producto a buscar: "))
                    producto_encontrado = None
                    for producto in inventario:
                        if producto.get("id") == id_buscar:
                            producto_encontrado = producto
                            break
                    if producto_encontrado is not None:
                        print("Información de producto encontrado")
                        print(f"ID: {producto_encontrado.get('id')}")
                        print(f"Nombre: {producto_encontrado.get('nombre')}")
                        print(f"Precio: ${producto_encontrado.get('precio'):.2f}")
                        print(f"Cantidad: {producto_encontrado.get('cantidad')}")
                    else:
                        print(f"Producto con ID {id_buscar} No encontrado")
                    print()
            case 4:
                print("Salido de sistema de Inventario")
                break
            case _:
                print("\nOpción inválida. Por favor Ingresa una opción correcta.\n")
    except ValueError:
        print("Error: entrada no válida. Debes ingresar un número entero.")
