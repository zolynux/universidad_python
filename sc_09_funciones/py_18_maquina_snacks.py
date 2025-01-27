print("*** Máquina de Snacks ***")

# Definimos la lista de snacks inicial
snacks = [
    {"id": 1, "nombre": "Papas", "precio": 30},
    {"id": 2, "nombre": "Refresco", "precio": 50},
    {"id": 3, "nombre": "Sandwich", "precio": 120},
]

# Lista de productos (vacíos). Son los snacks ya comprados
productos = []


def mostrar_snacks():
    print("-" * 15, "Snacks Disponibles", "-" * 15)
    for snack in snacks:
        print(
            f"\tID: {snack.get('id')} -> {snack.get('nombre')} - ${snack.get('precio')}"
        )


def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get("id") == id_buscar:
            return snack
    # Si llegamos al final y no se encontró el snack regresa None
    return None


def comprar_snacks():
    print(f"{'-'*15} Comprar Snacks {'-'*15}")
    id_snack = int(input("¿Qué snack quieres comprar (id): "))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f"Snack agregado: {snack_encontrado}")
    else:
        print(f"Snack NO encontrado con el ID: {id_snack}")


def mostrar_ticket():
    ticket = f"\t{10*'-'} Ticket de Venta {10*'-'}"
    total = 0
    for producto in productos:
        ticket += f"\n\t- {producto.get('nombre')} - ${producto.get('precio')}"
        total += producto.get("precio")
    ticket += f"\n\tTotal: ${total}"
    print(ticket)


# Programa Principal
if __name__ == "__main__":
    # Creamos el menú
    while True:
        print("-" * 15, "Menú", "-" * 15)
        print("\t1. Mostrar Snacks")
        print("\t2. Comprar Snack")
        print("\t3. Mostrar Ticket")
        print("\t4. Salir")

        option = int(input("Escoge una opción: "))
        if option == 1:
            mostrar_snacks()
        elif option == 2:
            comprar_snacks()
        elif option == 3:
            mostrar_ticket()
        elif option == 4:
            print("-" * 15, "Salir", "-" * 15)
            print("¡Regresa Pronto!")
            break
        else:
            print("-" * 15, "Opción inválida", "-" * 15)
            print("Proporciona otra opción.")
