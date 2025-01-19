# Colecciones en Python

## Colecciones

Una colección es un conjunto de datos. En Python tenemos varios tipos que podemos utilizar con el objetivo de almacenar, organizar y manipular múltiples conjuntos de datos, por ello también se les conoce como Estructures de Datos.

Los tipos que vamos a estudiar son:

- Listas
- Tuplas
- Set (conjunto)
- Diccionarios

Estos son los tipos más comunes y más utilizados. Comencemos con el tipo lista.

### Listas

Las listas son colecciones ordenadas y mutables de elementos que pueden ser de diferentes tipos. Las listas son dinámicas, lo que significa que pueden cambiar de tamaño, podemos añadir, modificar o eliminar elementos.

```python
# Sintaxis Listas
mi_list = [elemento1, elemento2, elemento3, ...]
```

```python
# Ejemplos de listas
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza"]
mixta = [1, "dos", 3.0, [4, 5]]
```

**📄 Código :**

```python
print("*** Manejo de Listas ***")

mi_lista = [1, 2, 3, 4, 5]
print(f"{mi_lista} -> Lista original")

# Largo de una lista
print(f"Largo de la lista: {len(mi_lista)}")

# Acceder a los elementos de la lista por indice
print(f"Accedemos al valor del indice 4: {mi_lista[4]}")
print(f"Accedemos al último índice de la lista: {mi_lista[-1]}")

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f"Modificamos el valor del indice 1: {mi_lista[1]}")

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f"{mi_lista} -> Se agregó el elemento 6")

# Añadir un nuevo elemento en un indice específico
mi_lista.insert(2, 15)
print(f"{mi_lista} -> Se añadió el valor de 15 en el índice 2")

# Eliminar elementos de una lista
# Usando el método remove
mi_lista.remove(5)
print(f"{mi_lista} -> Se removió el valor 5")
# Removemos por índice con el método pop
mi_lista.pop(1)  # Remueve el elemento del índice 1
print(f"{mi_lista} -> Se eliminó el índice 1 ")
# Eliminar usando la palabra del
del mi_lista[2]
print(f"{mi_lista} -> Se eliminó el índice 2")

# Obtener sublistas
sublista = mi_lista[1:3]  # Genera una sublista del índice 1 al 2 (3 no se incluye)
print(f"sublista [1:3]: {sublista}")
```

**🟢 Ejecutar:**

```console
*** Manejo de Listas ***
[1, 2, 3, 4, 5] -> Lista original
Largo de la lista: 5
Accedemos al valor del indice 4: 5
Accedemos al último índice de la lista: 5
Modificamos el valor del indice 1: 10
[1, 10, 3, 4, 5, 6] -> Se agregó el elemento 6
[1, 10, 15, 3, 4, 5, 6] -> Se añadió el valor de 15 en el índice 2
[1, 10, 15, 3, 4, 6] -> Se removió el valor 5
[1, 15, 3, 4, 6] -> Se eliminó el índice 1
[1, 15, 4, 6] -> Se eliminó el índice 2
sublista [1:3]: [15, 4]
```

### Iterar elementos de una lista

**📄 Código :**

```python
print("*** Iterar Listas ***")

nombres = ["Karla", "Juan", "Laura"]

for nombre in nombres:
    print(nombre)

lista_heterogenea = [100, True, "Ivonne"]
print()
for elemento in lista_heterogenea:
    print(elemento)
```

**🟢 Ejecutar:**

```console
*** Iterar Listas ***
Karla
Juan
Laura

100
True
Ivonne
```

### Lista de Reproducción

Crea un programa para administrar una lista de canciones.

Debes solicitar al usuario cuántas canciones desea agregar a la lista y posteriormente ir solicitando cada canción que desea agregar a la lista.

Finalmente, debe desplegar la lista de canciones en orden alfabético.

**📄 Código :**

```python
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
```

**🟢 Ejecutar:**

```console
*** PlayList de canciones ***
¿Cuentas  canciones deseas agregar?: 3
Proporciona la cancion 1: Hotel California - Eaglles
Proporciona la cancion 2: Staying Alive - Bee Gees
Proporciona la cancion 3: Dream on - Aerosmith

Lista de Reproducción en orden alfabético:
['Dream on - Aerosmith', 'Hotel California - Eaglles', 'Staying Alive - Bee Gees']

Iteramos el Playlist
- Dream on - Aerosmith
- Hotel California - Eaglles
- Staying Alive - Bee Gees
```

### Promedio de calificaiones

Crea un programa para realizar el cálculo promedio de calificaciones.

El programa debe solicitar el número de calificaciones a utilizar para obtener el promedio.

Posteriormente, se debe solicitar cada calificación al usuario.

Posteriormente realizar la suma de todas las calificaciones y finalmente mandar a imprimir el promedio.

**📄 Código :**

```python
print("*** Promedio de Calificaciones ***")

total_calificaciones = int(input("Proporciona el no. de calificaciones a evaluar: "))
calificaciones = []
promedio = 0

# Iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion = int(input(f"Calificación[{indice + 1}] = "))
    calificaciones.append(calificacion)

# Imprimimos las calificaciones proporcionadas
print(
    f"""
Las calificaciones proporcionadas son: {calificaciones}
"""
)

# Calculamos el promedio de las calificaciones
# sum(iterable)
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / total_calificaciones

print(f"Promedio de las calificaciones: {promedio:.2f}")
```

**🟢 Ejecutar:**

```console
*** Promedio de Calificaciones ***
Proporciona el no. de calificaciones a evaluar: 4      
Calificación[1] = 3
Calificación[2] = 6
Calificación[3] = 8 
Calificación[4] = 9

Las calificaciones proporcionadas son: [3, 6, 8, 9]    

Promedio de las calificaciones: 6.50
```

### Tuplas

Las tuplas son similares a las listas, ya que también son una colección de datos ordenados, pero las tuplas son inmutables, lo que significa que una vez creada una tupla no es posible modificar su tamaño, ni podemos agregar más elementos, ni modificarlos ni eliminarlos.

Las tuplas suelen utilizarse para crear colecciones de datos que no deben cambiar con el tiempo

```python
# Sintaxis de una tupla
mi_tupla = (elemento1, elemento2, elemento3)
mi_tupla_sin_parentesis = elemento1, elemento2, elemento3
```

```python
# Ejemplo de tuplas
tuplas_numeros = (1,2,3,4,5)
tupla_mixta = ("manzana", 10, 3.14, [1, 2, 3])
tupla_sin_parentesis = 'Juan', 'Karla'
tupla_un_elemento = 10, # La coma no es opcional
```

**📄 Código :**

```python
print("*** Manejo de Tuplas ***")

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# No podemos modificar una tupla
# mi_tupla[0] = 10
# No podemos agregar un elemento de la tupla
# mi_tupla.append(6)

# Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento, end=" ")

# Crear una tupla para una coordenada x, y
coordenadas = (3, 5)
# Accedemos a cada elemento de la tupla
print(f"\nCoordenada en el eje x:{coordenadas[0]}")
print(f"Coordenada en el eje y:{coordenadas[1]}")

# Crear una tupla unitaria
tupla_un_elemento = (10,)
print(f"Tupla de un elemento {tupla_un_elemento}")

# Tupla anidada
tuplas_anidada = (1, (2, 3), (4, 5))
print(f"Segundo elemento tupla anidada: {tuplas_anidada[1]}")
```

**🟢 Ejecutar:**

```console
*** Manejo de Tuplas ***
(1, 2, 3, 4, 5)
1 2 3 4 5 
Coordenada en el eje x:3
Coordenada en el eje y:5
Tupla de un elemento (10,)
Segundo elemento tupla anidada: (2, 3)
```
