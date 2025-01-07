import math


print('*** Constantes en Python ***')

PI = 3.14159
print('El valor de PI es:', PI)

NOMBRE_BASE_DATOS = 'clientes_db'
print('Nombre de la base de datos:', NOMBRE_BASE_DATOS)

# Esto NO se debe hacer, no se debe modificar el valor una constante
NOMBRE_BASE_DATOS = "listado_cliente_db"
print("No cambiar el valor de una constante:", NOMBRE_BASE_DATOS)

# User uan constante del lenguaje Python, aunque en este caso no esta en mayusculas
print("Valor de math.pi", math.pi)