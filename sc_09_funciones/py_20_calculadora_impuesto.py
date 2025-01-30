# Ejercicio: Calculadora de impuesto

print("*** Calculadora de Impuestos")


# Función que calcula el total de un pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total: float = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total


# Programa Principal
if __name__ == "__main__":
    pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
    impuesto = float(input("Proporcione el monto del impuesto: "))
    pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
    print(f"Pago con impuesto: {pago_con_impuesto}")
