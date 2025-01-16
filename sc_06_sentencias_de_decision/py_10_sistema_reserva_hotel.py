print("*** Sistema Reserva Hotel ***")

# Variables del hotel
TARIFA_DIARIA_SIN_VISTA_MAR = 150.50
TARIFA_DIARIA_CON_VISTA_MAR = 190.50

# Pedimos la información al usuario
nombre_cliente = input("Ingresa el nombre de cliente: ")
dias_estadia = int(input("Ingresa el número de los días de estadía: "))
vista_al_mar_txt = input("Ingresa con vista al mar (Si/No): ")
vista_al_mar = vista_al_mar_txt.strip().lower == "si"

# Cálculo del costo total de la estancia
costo_total = (
    dias_estadia * TARIFA_DIARIA_CON_VISTA_MAR
    if vista_al_mar
    else dias_estadia * TARIFA_DIARIA_SIN_VISTA_MAR
)

# Mostramos los detalles de la reserva
print(
    f"""
{'-' * 10} Detalles de la Reservación {'-' * 10}
Cliente: {nombre_cliente}
Días de estandía: {dias_estadia}
Costo total: ${costo_total:.2f}
Habitación con vista al mar: {'Sí' if vista_al_mar else 'No'}
"""
)
