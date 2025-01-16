print("*** La estación del Año ***")

numero_mes = int(input("Introduce el número de mes entre 1 y 12: "))
mensaje = ""

match numero_mes:
    case 1 | 2 | 12:
        mensaje = "Es Invierno"
    case 3 | 4 | 5:
        mensaje = "Es Primavera"
    case 6 | 7 | 8:
        mensaje = "Es Verano"
    case 9 | 10 | 11:
        mensaje = "Es Otoño"
    case _:
        mensaje = "Introdujiste es un inválido"

print(
    f"""{'-' * 10} Estación del Año {'-' * 10}
Esta la estación: {mensaje}
"""
)
