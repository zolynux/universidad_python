print("*** Imprimir detalles de una persona usando kwargs ***")


# Función que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print("\nValores recibidos:")
    for llave, valor in kwargs.items():
        print(f"{llave}:{valor}")


imprimir_detalle_persona(nombre="Karla", edad=30, ciudad="México")
imprimir_detalle_persona(nombre="Carlos", edad=28, ciudad="Colombia", puesto="Gerente")
