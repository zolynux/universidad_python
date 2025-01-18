# Ciclos

## Ciclos en Python

### Ciclo while

Los ciclos en Python son estructuras de control que repitan una serie de instrucciones hasta que se cumple una condición específica.

En Python tenemos dos tipos de estructuras para ejecutar ciclos: Ciclo `while` y ciclo `for`. Comencemos con el ciclo `while`.

El ciclo `while` repite una serie de instrucciones mientras la condición a evaluar sea verdadera.

```python
# Sintaxis ciclo while:
while condicion:
  # Bloque de código a ejecutar
```

```python
# Ejemplo ciclo while:
# Imprimir de 1 a 3
contador = 1
while contador <= 3:
  print(contador)
  contador += 1
```

#### Diagrama de Flujo Ciclo `while`

Dado el siguiente código, veamos el diagrama de flujo asociado:

![alt text](image.png)

Valor contador = ~~1~~ 2

Resultado Condición:

`1 <= 3 -> True`

Salida a Consola

```console
1
2
3
```

**📄 Código :**

```python
print("*** Ciclo while ***")

# Imprimir los valores del 1 al 5
contador = 1
while contador <= 5:
    print(contador, end=" ")
    contador += 1  # contador = contador + 1
```

**🟢 Ejecutar:**

```console
*** Ciclo while ***
1 2 3 4 5
```

### Ciclo for

El ciclo `for` itera o recorre una secuencia de valores, por ejemplo los caracteres de una cadena, una lista, etc. y ejecuta bloque de código por cada elemento de la secuencia.

```python
# Sintaxis ciclo for
for variable in secuencia:
  # Bloque de código a ejecutar
```

```python
# Ejemplo ciclo for
cadena = 'Hola Mundo'
for letra in cadena:
  print(letra, end=' ')
```

Salida a consola:

```console
H o l a  M u n d o
```

**📄 Código :**

```python
print("*** Ciclo for ***")

print("Recorremos los caracteres de una cadena")
cadena = "Hola Mundo"
# Iteramos los caracteres
for letra in cadena:
    print(letra, end=" ")

print("\n\nRecorremos la lista de frutas:")
frutas = ["Plátano", "Fresa", "Mango", "Uva", "Manzana", "Pera", "Naranja"]
for fruta in frutas:
    print(fruta, end=" ")
```

**🟢 Ejecutar:**

```console
*** Ciclo for ***
Recorremos los caracteres de una cadena
H o l a   M u n d o

Recorremos la lista de frutas:
Plátano Fresa Mango Uva Manzana Pera Naranja
```
