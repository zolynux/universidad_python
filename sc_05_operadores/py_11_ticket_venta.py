print("*** Generación Ticket de Venta ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio plátanos: "))
descuento_porcentaje = int(input("¿Aplicar algún descuento (%)?: "))

# Cálculo del subtotal (sin impuesto)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje / 100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Cálculo con impousto (16%)
impuesto = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuesto)
costo_total_compra = subtotal_con_descuento + impuesto
print(
    f"""
subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje})
Subtotal: con descuento: ${subtotal_con_descuento}
impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}
      """
)
