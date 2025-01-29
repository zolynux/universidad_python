print("*** Calculadora con Funciones ***")


def mostrar_menu():
    print(
        """Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir"""
    )
    return int(input("Escoge una opción: "))


def pedir_valores():
    operacion1 = float(input("Dame el valor 1: "))
    operacion2 = float(input("Dame el valor 2: "))
    return operacion1, operacion2


# Método de ejecutar la operación
def ejecutar_operacion(option, salir):
    # Solicitar los valores de los operaciones
    if 1 <= option <= 4:
        operacion1, operacion2 = pedir_valores()
    resultado = 0
    match option:
        case 1:
            resultado = operacion1 + operacion2
            print(f"El resultado de la suma es: {resultado}")
        case 2:
            resultado = operacion1 - operacion2
            print(f"El resultado de la resta es: {resultado}")
        case 3:
            resultado = operacion1 * operacion2
            print(f"El resultado de la multiplicación es: {resultado}")
        case 4:
            resultado = operacion1 / operacion2
            print(f"El resultado de la división es: {resultado}")
        case 5:
            print("Saliendo del programa de calculadora, ¡Hasta pronto!")
            salir = True
        case _:
            print("Opción Inválida.\nDebes escoger correctamente la opción.")
    return salir


# Programa principal
if __name__ == "__main__":
    salir = False
    while not salir:
        option = mostrar_menu()
        salir = ejecutar_operacion(option, salir)
