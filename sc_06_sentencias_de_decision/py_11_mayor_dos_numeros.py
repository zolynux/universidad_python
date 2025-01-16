print("*** El mayor  de dos números ***")

numero1 = int(input("Ingresa un primer número entero: "))
numero2 = int(input("Ingresa un segundo número entero: "))

numero_mayor = (
    "El primer numero es mayor." if numero1 > numero2 else "El segundo numero es mayor."
)

print(
    f"El primer es: {numero1}\nEl segundo es: {numero2}\n Resultado: *** {numero_mayor} ***"
)
