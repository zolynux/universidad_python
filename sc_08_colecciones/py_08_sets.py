print("*** Manejo de Sets ***")
# Crear un conjunto
mi_set = {1, 2, 3, 4, 5, 4}
print(f"Mi set: {mi_set}")

# Agregar elementos al set
mi_set.add(6)
mi_set.add(7)

# Intentamos agregar un elemento duplicado
mi_set.add(3)
print(f"Mi set modificado: {mi_set}")

# Eliminar un elemento del conjunto
mi_set.remove(4)

# Iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=" ")

# Comprobar si existe un elemento en el set
print(
    f"\nExiste el valor de 4 en el set? {4 in mi_set}"
)  # False, fue eliminado un elemento de 4 anterior en el código

# Obtener la longitud del set
print(f"Longitud del conjunto: {len(mi_set)}")
