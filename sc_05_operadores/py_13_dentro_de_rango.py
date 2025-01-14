print("*** Valor Dentro de Rango ***")

VALOR_MINIMO, VALOR_MAXIMO = 0, 5

numero = int(input("Proporciona un número dentro de rango entre 0 y 5: "))

# rango = numero >= VALOR_MINIMO and numero <= VALOR_MAXIMO
rango = VALOR_MINIMO <= numero <= VALOR_MAXIMO  # exactamente la misma de linea anterior

print(f"Valor dentro de rango: {rango}")
