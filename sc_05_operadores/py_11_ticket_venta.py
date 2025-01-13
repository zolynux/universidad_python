print("*** Generación Ticket de Venta ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio plátanos: "))

# Cálculo del subtotal (sin impuesto)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Cálculo con impousto (16%)
impuesto = subtotal * 0.16

# Calculo total de la compra (con impuesto)
costo_total_compra = subtotal + impuesto
print(
    f"""
subtotal: ${subtotal:.2f}
impuesto: ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}
      """
)
