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

### Ejercicio Acumulador Suma en Ciclo

Realizar la suma de los primeros 5 números utilizando un ciclo while

![alt text](image-1.png)

**📄 Código :**

```python
print('*** Suma Acumulativa "while" ***')

# Sumar los primeros 5 números
MAXIMO = 5
numero = 1
acumulador_suma = 0

# Empezamos a iterar
while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f"(acumulador_suma + numer) -> {acumulador_suma} + {numero}")
    acumulador_suma += numero
    numero += 1

    # Imprimir el resultado de la suma parcial
    print(f"Suma parcial acumulada: {acumulador_suma}")

print(f"\nResultado suma acumulado: {acumulador_suma}")
```

**🟢 Ejecutar:**

```console
*** Suma Acumulativa "while" ***
(acumulador_suma + numer) -> 0 + 1
Suma parcial acumulada: 1
(acumulador_suma + numer) -> 1 + 2
Suma parcial acumulada: 3
(acumulador_suma + numer) -> 3 + 3
Suma parcial acumulada: 6
(acumulador_suma + numer) -> 6 + 4
Suma parcial acumulada: 10
(acumulador_suma + numer) -> 10 + 5
Suma parcial acumulada: 15

Resultado suma acumulado: 15
```

### Menú Iterativo

**📄 Código :**

```python
print("*** Sistema de Administración de Cuenta ***")

salir = False
while not salir:
    print(
        f"""Menú:
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir"""
    )
    opcion = int(input("Escoge una opción: "))
    match opcion:
        case 1:
            print("Creando tu cuenta... \n")
        case 2:
            print("Eliminado tu cuenta... \n")
        case 3:
            print("Salimos del sistema. Hasta pronto!\n")
            salir = True
        case _:
            print("Opción inválida, proporciona otra opción...\n")
else:
    print("Terminando el sistema de Administración de Cuentas")
```

**🟢 Ejecutar:**

```console
*** Sistema de Administración de Cuenta ***
Menú:
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir
Escoge una opción: 1
Creando tu cuenta... 

Menú:
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir
Escoge una opción: 5
Opción inválida, proporciona otra opción...

Menú:
          1. Crear cuenta
          2. Eliminar cuenta
          3. Salir
Escoge una opción: 3
Salimos del sistema. Hasta pronto!

Terminando el sistema de Administración de Cuentas
```
