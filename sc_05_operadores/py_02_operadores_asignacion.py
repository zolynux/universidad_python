print("*** Operadores de Asignación ***")
numero = 5
print(f"Valor de la variable numero: {numero}")
numero = 10
print(f"Valor de la variable numero: {numero}")
cadena = "Hola, mundo"
print(f"Valor de la variable cadena: {cadena}")

# Asignación Múltiple
a, b, c = 10, "Saludo", 14.5
print(f"Valor de a = {a}, b = {b}, c = {c}")

# Asignación Encadenada
x = y = z = 10
print(f"Valor de x = {x}, y = {y}, z = {z}")

# Intercambio de valores de una variable, sin utilizar variables temporales.
x, y = 5, 10
print(f"Valor de iniciales x = {x}, y = {y}")
# Aplicando el concepto de asignación múltiple, intercambiamos los valores de las variables x y y.
x, y = y, x
print(f"Valor de intercambio x = {x}, y = {y}")

# Recibir múltiples valores de la entrada del usuario
nombre, apellido = input("Ingresa tu nombre y apellido separados por coma: ").split(",")
print(f"Nombre: {nombre.strip()}, Apellido: {apellido.strip()}")
