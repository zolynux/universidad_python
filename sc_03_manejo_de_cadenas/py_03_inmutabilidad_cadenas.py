# Inmutabilidad en cadenas
cadena1 = "Hola Mundo"
# cadena1 [0] = 'h' # no podemos modificar los carateres
cadena2 = cadena1
cadena1 = "Adios"
print(cadena1)
print(cadena2)
