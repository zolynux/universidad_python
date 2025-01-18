print("*** Sistema de Administración de Cuenta ***")

salir = False
while not salir:
    print(
        f"""Menú:
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir"""
    )
    opcion = int(input("Escoge una opción: "))
    match opcion:
        case 1:
            print("Creando tu cuenta... \n")
        case 2:
            print("Eliminado tu cuenta... \n")
        case 3:
            print("Salimos del sistema. Hasta pronto!\n")
            salir = True
        case _:
            print("Opción inválida, proporciona otra opción...\n")
else:
    print("Terminando el sistema de Administración de Cuentas")
