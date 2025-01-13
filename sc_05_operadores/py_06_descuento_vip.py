print("*** Sistema Descuentos VIP ***")

NO_PRODUCTOS_DESCUENTOS = 10
cantidad_productos = int(input("¿Cuántos productos compraste hoy?: "))
tiene_membresia = str(input("¿Tienes la membresía de la tienda (Si/No)?: "))

es_elegible_descuento = (
    cantidad_productos >= NO_PRODUCTOS_DESCUENTOS
    and tiene_membresia.strip().lower() == "si"
)

print(f"¿Tienes acceso al descuento VIP?: {es_elegible_descuento}")
