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
mi_list = [elemeno1, elemento2, elemento3, ...]
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
