print("*** Convertidor de Temperatura ***")


# Función que convierte de fehrenheit a celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Función que convierte de celsius a fehrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


if __name__ == "__main__":
    salir = False
    while not salir:
        print(
            """Menú
        1. Convertido en Fahrenheit a Celsius
        2. Convertido en Celsius a Fahrenheit
        3. Salir"""
        )
        option = int(input("Escoge una opción: "))
        match option:
            case 1:
                fahrenheit = float(
                    input("Proporcione un número de fahrenheit en grado: ")
                )
                print(
                    f"Resultado de que a celsius: {fahrenheit_a_celsius(fahrenheit):.2f}"
                )
            case 2:
                celsius = float(input("Proporcione un número de celsius en grado: "))
                print(
                    f"Resultado de que a fahrenheit: {celsius_a_fahrenheit(celsius):.2f}"
                )
            case 3:
                print("Salida de Convertidor de Temperatura.\n¡Hasta Pronto!")
            case _:
                print("Opción inválida. Escoge otra opción correcta.")
                salir = True
