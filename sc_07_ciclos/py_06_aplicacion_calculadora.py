print("*** Calculadora en Python ***")

salir = False
operadores = ["Suma", "Resta", "Multiplicación", "División"]
num1 = num2 = resultado = 0

while not salir:
    print(
        f"""Operaciones que puedes realizar:
        1. {operadores[0]}
        2. {operadores[1]}
        3. {operadores[2]}
        4. {operadores[3]}
        5. Salir"""
    )
    opcion = int(input("Escoge una opción con número: "))

    match opcion:
        case 1:
            print("-" * 5, f"{operadores[0]}", "-" * 5)
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = num1 + num2
            print(f"\nEl resultado de la {operadores[0]} es: {resultado}\n")
        case 2:
            print("-" * 5, f"{operadores[1]}", "-" * 5)
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = num1 - num2
            print(f"\nEl resultado de la {operadores[1]} es: {resultado}\n")
        case 3:
            print("-" * 5, f"{operadores[2]}", "-" * 5)
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = num1 * num2
            print(f"\nEl resultado de la {operadores[2]} es: {resultado}\n")
        case 4:
            print("-" * 5, f"{operadores[3]}", "-" * 5)
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if num1 == 0 or num2 == 0:
                print("Error. Debes ingresar números sin cero.\n")
            else:
                resultado = num1 / num2
                print(f"\nEl resultado de la {operadores[3]} es: {resultado}\n")
        case 5:
            print("Saliendo del aplicación calculadora. ¡Hasta pronto!")
            salir = True
        case _:
            print("Opción inválida. Debe ingresar correctamente a la opción...")
