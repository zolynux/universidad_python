print('*** Operador "not" ***')

condicion = False
print(f"Operador de variable es: {condicion}")
resultado = not condicion
print(f"Operador not store {condicion} = {resultado}")

# Revisar si una variable es cadena vacia
nombre = ""
es_cadena_vacia = not nombre
print(
    f"Varaible es cadena vacía '{nombre}'\nLa variable NO tiene ningún valor? {es_cadena_vacia}"
)

# Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(
    f"Varaible es sin valor asignado {variable} \n¿La variable NO tiene ningún valor asignado?: {es_variable_sin_valor}"
)
