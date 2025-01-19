print("*** PlayList de canciones ***")

# creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input("¿Cuentas  canciones deseas agregar?: "))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f"Proporciona la cancion {indice + 1}: ")
    lista_reproduccion.append(cancion)

# Empezamos a agregar canciones
"""
lista_reproduccion.append("Hotel California - Eaglles")
lista_reproduccion.append("Staying Alive - Bee Gees")
lista_reproduccion.append("Dream on - Aerosmith")
"""
# Ordenar la lista en orden alfabético (sort)
# lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort()

# Mostrar la lista de canciones
print(f"\nLista de Reproducción en orden alfabético:\n{lista_reproduccion}")

# Mostrar la lista iteramos sus elementos
print(f"\nIteramos el Playlist")
for cancion in lista_reproduccion:
    print(f"- {cancion}")
