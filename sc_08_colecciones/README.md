from sc_02_variables.py_04_tipos_de_datos import direccionfrom sc_02_variables.py_02_modificado import telefono

# Colecciones en Python

## Colecciones

Una colección es un conjunto de datos. En Python tenemos varios tipos que podemos utilizar con el objetivo de almacenar,
organizar y manipular múltiples conjuntos de datos, por ello también se les conoce como Estructures de Datos.

Los tipos que vamos a estudiar son:

- Listas
- Tuplas
- Set (conjunto)
- Diccionarios

Estos son los tipos más comunes y más utilizados. Comencemos con el tipo lista.

### Listas

Las listas son colecciones ordenadas y mutables de elementos que pueden ser de diferentes tipos. Las listas son
dinámicas, lo que significa que pueden cambiar de tamaño, podemos añadir, modificar o eliminar elementos.

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

Debes solicitar al usuario cuántas canciones desea agregar a la lista y posteriormente ir solicitando cada canción que
desea agregar a la lista.

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

### Promedio de calificaciones

Crea un programa para realizar el cálculo promedio de calificaciones.

El programa debe solicitar el número de calificaciones a utilizar para obtener el promedio.

Posteriormente, se debe solicitar cada calificación al usuario.

Posteriormente, realizar la suma de todas las calificaciones y finalmente mandar a imprimir el promedio.

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

Las tuplas son similares a las listas, ya que también son una colección de datos ordenados, pero las tuplas son
inmutables, lo que significa que una vez creada una tupla no es posible modificar su tamaño, ni podemos agregar más
elementos, ni modificarlos ni eliminarlos.

Las tuplas suelen utilizarse para crear colecciones de datos que no deben cambiar con el tiempo

```python
# Sintaxis de una tupla
mi_tupla = (elemento1, elemento2, elemento3)
mi_tupla_sin_parentesis = elemento1, elemento2, elemento3
```

```python
# Ejemplo de tuplas
tuplas_numeros = (1, 2, 3, 4, 5)
tupla_mixta = ("manzana", 10, 3.14, [1, 2, 3])
tupla_sin_parentesis = 'Juan', 'Karla'
tupla_un_elemento = 10,  # La coma no es opcional
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

### Desempaquetado de Tuplas (unpacking)

**📄 Código :**

```python
print("*** Desempaquetado de Tuplas ***")

producto = ("P001", "Camisa", 20.00)

# Desempaquetado
id, descripcion, precio = producto

# imprimir los valores
print(f"Tupla completa: {producto}")
# Valores independientes ya desempaquetados
print(f"Producto: id = {id}, descripción = {descripcion}, precio = {precio}")
```

**🟢 Ejecutar:**

```console
*** Desempaquetado de Tuplas ***
Tupla completa: ('P001', 'Camisa', 20.0)
Producto: id = P001, descripción = Camisa, precio = 20.0
```

### Combinación de Listas y Tuplas

**📄 Código :**

```python
print("*** Combinación de Listas y Tuplas ***")

# definir una lista que almacena tuplas de productos.
productos = [
    ("P001", "Camiseta", 20.00),
    ("P002", "Jeans", 30.00),
    ("P003", "Sudadera", 40.00),
]

# Imprimir la información de cada producto
#  y además calculamos el precio total
precio_total = 0

print("Información de los productos: ")
for producto in productos:
    id, descripcion, precio = producto  # unpacking
    print(f"Product: id = {id}, descripción = {descripcion}, precio = {precio}")
    precio_total += precio  # Productos[2]
print(f"Precio total de los productos: {precio_total}")
```

**🟢 Ejecutar:**

```console
*** Combinación de Listas y Tuplas ***
Información de los productos:
Product: id = P001, descripción = Camiseta, precio = 20.0
Product: id = P002, descripción = Jeans, precio = 30.0 
Product: id = P003, descripción = Sudadera, precio = 40.0
Precio total de los productos: 90.0
```

### Sets en Python

Los sets (conjuntos) son colecciones de datos no ordenados de elementos únicos. Son muy útiles cuando debemos
asegurarnos de que no haya elementos duplicados en nuestra colección.

```python
# Sintaxis de un set
mi_set = {elemento1, elemento2, elemento3}
```

```python
# Ejemplo de sets
set_a = {1, 2, 3, 4}
set_b = {3, 'Juan', True, 6.5}
numeros = {1, 2, 2, 3, 4}
print(numeros)  # Salida: {1, 2, 3, 4}
```

**📄 Código :**

```python
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
```

**🟢 Ejecutar:**

```console
*** Manejo de Sets ***
Mi set: {1, 2, 3, 4, 5}
Mi set modificado: {1, 2, 3, 4, 5, 6, 7}
1 2 3 5 6 7
Existe el valor de 4 en el set? False
Longitud del conjunto: 6
```

### Operaciones con Set

**📄 Código :**

```python
print("*** Operaciones con Set ***")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f"Unión a | b: {union}")

interseccion = a & b
print(f"Intersección a & b: {interseccion}")

diferencia = a - b
print(f"Diferencia a - b: {diferencia}")
```

**🟢 Ejecutar:**

```console
*** Operaciones con Set ***
Unión a | b: {1, 2, 3, 4, 5, 6}
Intersección a & b: {3, 4}
Diferencia a - b: {1, 2}
```

### Lista de suscriptores

Crea un programa para administrar una lista de suscriptores utilizando su email.

Supón que una persona se suscribe al boletín información utilizando su email.

A medida que la lista crece, hay que asegurarnos que no tengamos suscriptores duplicados.

También deberemos poder agregar y eliminar suscriptores.

**📄 Código :**

```python
print("*** Lista de Suscriptores ***")

suscriptores = {"luisa@mail.com", "marcos@mail", "elena@mail.com"}
print(f"Lista de suscriptores inicial: {suscriptores}")

# Verifica si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = "karla@mail.com"
if nuevo_suscriptor in suscriptores:
    print(f"El nuevo suscriptor ya está en lista {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}")

print(f"Lista de suscriptores: {suscriptores}")

# Eliminamos un suscriptor
suscriptor_eliminar = "elena@mail.com"
suscriptores.remove(suscriptor_eliminar)
print(f"El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista")
print(f"Lista de suscriptores: {suscriptores}")

# Verificamos la cantidad total de suscriptores
print(f"Cantidad total suscriptores: {len(suscriptores)}")

# Mostramos todos los suscriptores
print("-" * 5, "Lista de Suscriptores", "-" * 5)
for suscriptor in suscriptores:
    print(f"- {suscriptor}")
```

**🟢 Ejecutar:**

```console
*** Lista de Suscriptores ***
Lista de suscriptores inicial: {'luisa@mail.com', 'marcos@mail', 'elena@mail.com'}
El nuevo suscriptor se ha agregado a la lista karla@mail.com
Lista de suscriptores: {'luisa@mail.com', 'marcos@mail', 'elena@mail.com', 'karla@mail.com'}
El suscriptor elena@mail.com ha sido eliminado de la lista
Lista de suscriptores: {'luisa@mail.com', 'marcos@mail', 'karla@mail.com'}
Cantidad total suscriptores: 3
----- Lista de Suscriptores -----
- luisa@mail.com
- marcos@mail
- karla@mail.com
```

### Lista de Suscriptores dinámica con Sets

```python
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
```

### Diccionarios en Python

Los diccionarios son una colección de datos ordenada (3.7+). Y se almacenan en forma de llave:valor. Es una estructura
muy útil cuando necesitas asociar un conjunto de valores con un conjunto de claves o llaves que sirven como índices
únicos.

```python
# Sintaxis de un diccionario
mi_diccionario = {clave1: valor1, clave2: valor2}
```

```python
# Ejemplo de un diccionario
persona = {'nombre': 'Pedro', 'edad': 30, 'es_casado': True}
```

**📄 Código :**

```python
print("*** Diccionarios en Python ***")

# Creamos un dict de persona con clave y valor
persona = {"nombre": "Sergio", "edad": 30, "ciudad": "México"}

print(f"Diccionario de persona: {persona}")

# Acceder a los elementos del diccionario
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")
print(f"Ciudad: {persona.get('ciudad')}")

# Modificar un valor del diccionario
persona["edad"] = 35
print(f"Diccionario de persona: {persona}")

# Agregar un nuevo elemento
persona["profesion"] = "Ingeniero"
print(f"Diccionario de persona: {persona}")

# Eliminar un elemento
del persona["ciudad"]
print(f"Diccionario de persona: {persona}")

persona.pop("profesion")
print(f"Diccionario de persona: {persona}")

# Iterar los elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f"Llave: {llave}, Valor: {valor}")

# Obtener los valores
print(f"\nValores de diccionario:")
for valor in persona.values():
    print(f"- Valor: {valor}")

# Obtener las llaves
for llave in persona.keys():
    print(f"- {llave}")
```

**🟢 Ejecutar:**

```console
*** Diccionarios en Python ***
Diccionario de persona: {'nombre': 'Sergio', 'edad': 30, 'ciudad': 'México'}
Nombre: Sergio
Edad: 30
Ciudad: México
Diccionario de persona: {'nombre': 'Sergio', 'edad': 35, 'ciudad': 'México'}
Diccionario de persona: {'nombre': 'Sergio', 'edad': 35, 'ciudad': 'México', 'profesion': 'Ingeniero'}
Diccionario de persona: {'nombre': 'Sergio', 'edad': 35, 'profesion': 'Ingeniero'}
Diccionario de persona: {'nombre': 'Sergio', 'edad': 35}
Llave: nombre, Valor: Sergio
Llave: edad, Valor: 35

Valores de diccionario:
- Valor: Sergio
- Valor: 35
- nombre
- edad
```

### Agenda de Contactos

Crear una agenda de contactos utilizando un diccionario de Python con la siguiente estructura

````python
agenda
{
    nombre
{
    telefono
email
dirección
}
}
````

**📄 Código :**

```python
print("*** Agenda de contactos ***")

agenda = {
    "Carlos": {
        "telefono": "34235435",
        "email": "carlos@mail.com",
        "direccion": "Calle Principal 132",
    },
    "María": {
        "telefono": "4353344",
        "email": "maria@mail.com",
        "direccion": "Avenida Central 453",
    },
    "Pedro": {
        "telefono": "4334344",
        "email": "pedro@mail.com",
        "direccion": "Plaza Mayor 898",
    },
}

print(agenda)

# Acceder a la información de un contacto en especifico
print(
    f"""Información del contacto de María:
Teléfono: {agenda['María']['telefono']}
Email: {agenda.get('María').get('email')}
Dirección: {agenda.get('María').get('direccion')}
"""
)

# Agregar un nuevo contacto
agenda["Ana"] = {
    "telefono": "453563443",
    "email": "ana@mail.com",
    "direccion": "Calle Salvador Diaz 321",
}

print(agenda)

# Eliminar un contacto existente
agenda.pop("Pedro")
# del agenda["Pedro"]
print(agenda)

# Mostramos los contactos de la agenda
# Usar iterable
print()
print("Contactos en la agena".center(35, "="))
for nombre, detalles in agenda.items():
    print(
        f"""
{'=' * 50}
Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}"""
    )
```

**🟢 Ejecutar:**

```console
*** Agenda de contactos ***
{'Carlos': {'telefono': '34235435', 'email': 'carlos@mail.com', 'direccion': 'Calle Principal 132'}, 'María': {'telefono': '4353344', 'email': 'maria@mail.com', 'direccion': 'Avenida Central 453'}, 'Pedro': {'telefono': '4334344', 'email': 'pedro@mail.com', 'direccion': 'Plaza Mayor 898'}}
Información del contacto de María:
Teléfono: 4353344
Email: maria@mail.com
Dirección: Avenida Central 453

{'Carlos': {'telefono': '34235435', 'email': 'carlos@mail.com', 'direccion': 'Calle Principal 132'}, 'María': {'telefono': '4353344', 'email': 'maria@mail.com', 'direccion': 'Avenida Central 453'}, 'Pedro': {'telefono': '4334344', 'email': 'pedro@mail.com', 'direccion': 'Plaza Mayor 898'}, 'Ana': {'telefono': '453563443', 'email': 'ana@mail.com', 'direccion': 'Calle Salvador Diaz 321'}}
{'Carlos': {'telefono': '34235435', 'email': 'carlos@mail.com', 'direccion': 'Calle Principal 132'}, 'María': {'telefono': '4353344', 'email': 'maria@mail.com', 'direccion': 'Avenida Central 453'}, 'Ana': {'telefono': '453563443', 'email': 'ana@mail.com', 'direccion': 'Calle Salvador Diaz 321'}}

=======Contactos en la agena=======

==================================================
Nombre: Carlos
    Teléfono: 34235435
    Email: carlos@mail.com
    Dirección: Calle Principal 132

==================================================
Nombre: María
    Teléfono: 4353344
    Email: maria@mail.com
    Dirección: Avenida Central 453

==================================================
Nombre: Ana
    Teléfono: 453563443
    Email: ana@mail.com
    Dirección: Calle Salvador Diaz 321
```
