print("*** Suma con Argumentos Variables ***")


# Función sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total


# Llamamos a la función sumar
resultado = sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Resultado de la suma:", resultado)
