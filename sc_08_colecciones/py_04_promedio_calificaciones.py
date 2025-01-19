print("*** Promedio de Calificaciones ***")

total_calificaciones = int(input("Proporciona el no. de calificaciones a evaluar: "))
calificaciones = []
promedio = 0

# Iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion = int(input(f"Calificación[{indice + 1}] = "))
    calificaciones.append(calificacion)

# Imprimimos las calificaciones proporcionadas
print(
    f"""
Las calificaciones proporcionadas son: {calificaciones}
"""
)

# Calculamos el promedio de las calificaciones
# sum(iterable)
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / total_calificaciones

print(f"Promedio de las calificaciones: {promedio:.2f}")
