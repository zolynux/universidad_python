estrella = "*" * 3
print(estrella, "Sistema de Empleado", estrella)

nombre_empleado = input("Nombre del empleado: ")
edad_empleado = int(input("Edad del empleado: "))
salario_empleado = float(input("Salario de empleado: "))
es_jefe_departamento = str(input("¿Es jefe de departamento (Si/No)? "))


# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"

# Imprimir los valores del Empleado
print()
print(estrella, "Datos del Empleado", estrella)
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario: {salario_empleado:.2f}")
print(f"Jefe de departamento es: {es_jefe_departamento}")
