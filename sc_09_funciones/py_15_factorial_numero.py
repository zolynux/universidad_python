print("*** Factorial de un Número con Recursividad ***")


# Definimos la función factorial recursiva
def factorial_recursiva(numero):
    # Caso Base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f"Resultado factorial parcial {numero} es: 1")
        return 1
    else:  # Caso Recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f"Resultado factorial parcial {numero} es: {factorial_parcial}")
        return factorial_parcial


numero = 5
resultado = factorial_recursiva(numero)
print(f"El factorial de {numero} es: {resultado}")
