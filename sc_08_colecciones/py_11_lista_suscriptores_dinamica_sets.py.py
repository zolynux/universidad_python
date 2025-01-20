print("*** Lista de Suscriptores ***")

# Definimos el set inicial
# suscriptores = {} # Aquí se define un diccionario vacío
suscriptores = set()  # Definimos un set vacío

# Definimos el número entero con entrada de datos
numero_suscriptores = int(input("Proporciona el número de suscriptores iniciales: "))
# Iteramos el numero de suscriptores
for _ in range(numero_suscriptores):
    suscriptores.add(input("Nuevo Suscriptor (email): "))


suscriptores = {"luisa@mail.com", "marcos@mail", "elena@mail.com"}
print(f"Lista de suscriptores inicial: {suscriptores}")

# Verifica si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = input("Proporciona el  nuevo suscriptor: ")
if nuevo_suscriptor in suscriptores:
    print(f"El nuevo suscriptor ya está en lista {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}")

print(f"Lista de suscriptores: {suscriptores}")

# Eliminamos un suscriptor
suscriptor_eliminar = input("Proporciona el suscriptor a eliminar: ")
suscriptores.remove(suscriptor_eliminar)
print(f"El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista")
print(f"Lista de suscriptores: {suscriptores}")

# Verificamos la cantidad total de suscriptores
print(f"Cantidad total suscriptores: {len(suscriptores)}")

# Mostramos todos los suscriptores
print("-" * 5, "Lista de Suscriptores", "-" * 5)
for suscriptor in suscriptores:
    print(f"- {suscriptor}")
