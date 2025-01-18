print("*** Aplicación de Cajero Automático ***")

salir = False
saldo = 1000.00

while not salir:
    print(
        """Operaciones que puedes realizar:
          1. Consultar Saldo
          2. Retirar
          3. Depositar
          4. Salir."""
    )
    opcion = int(input("Escoge un número de opción: "))

    match opcion:
        case 1:
            print(f"\nTu saldo actual es: {saldo:.2f}\n")
        case 2:
            monto_retirar = float(input("Ingresa el monto a retirar: "))
            if monto_retirar <= saldo:
                saldo -= monto_retirar
                print(f"\nTu nuevo saldo es: ${saldo:.2f}\n")
            else:
                print(
                    f"\nNo cuentas con el saldo suficiente. Tu saldo actual: ${saldo:.2f}\n"
                )
        case 3:
            monto_depositar = float(input("Ingresa el monto a depositar: "))
            saldo += monto_depositar
            print(f"\nTu nuevo saldo es: ${saldo:.2f}\n")
        case 4:
            salir = True
        case _:
            print(
                "\nLa opción es inválida. Ingresa de nuevo debe ser un número entero de opción...\n"
            )
else:
    print("\nSaliendo del cajero automático. ¡Hasta Pronto!")
