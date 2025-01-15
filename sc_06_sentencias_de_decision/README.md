# Sentencias de decisión

Las sentencias de decisión nos permiten controlar el flujo de ejecución de un programa.

Las estructuras que podemos usar son: `if`, `else`, y `elif`

- La sentencia `if` permite ejecutar un bloque de código si la condición a evaluar es verdadera. Una condición es una expresión que evaluar a  `True` o `False`, Ej: `edad >= 18`
  
```python
# Sintaxis sentencias if
if condicion:
  # Bloque de código que se
  # Ejecuta si la condición es True
```

```python
# Ejemplo Sentencia fi
edad = 30
if edad >= 18:
  print("Eres mayor de edad.")
```

## Diagrama de Flujo

Un programa de flujo es una representación gráfica de los pasos a ejecutar para lograr un resultado específico.

Se utilizan símbolos estandarizados para representar distintos tipos de acciones:

- Un óvalo  representa el inicio o fin de un proceso:
![alt text](image.png)
- Un rectángulo muestra instrucciones o acciones a ejecutar
![alt text](image-1.png)
- Un rombo o diamante indica decisiones, con múltiples flujos dependiendo si la respuesta es verdadera o falsa
![alt text](image-2.png)
- Las fechas dirigen el flujo del proceso, mostrando la dirección en que se mueven la secuencia de acciones.
![alt text](image-3.png)

## Diagrama de Flujo Sentencia `if`

Dado el código siguiente, vamos a crear su diagram de flujo equivalente:

```python
# Ejemplo Sentencia if
edad = 30
if edad >= 18:
  print("Eres mayor de edad.")
```

![alt text](image-4.png)

**📄 Código :**

```python
print("*** Sentencia IF ***")

edad = 30
if edad >= 18:
    print(f"Eres mayor de edad. Tienes {edad} años")
#     print()
#     print()
# print()
# print()
```

**🟢 Ejecutar:**

```console
*** Sentencia IF ***
Eres mayor de edad. Tienes 30 años
```

## Sentencia if else

- La sentencia `else` se usa para ejecutar un bloque de código cuando la condición del `if` es falsa.

```python
# Sintaxis sentecia if else
if condicion:
  # Bloque de código que se ejecuta
  # si la condición es verdadera
else:
  # Bloque de código que se ejecuta
  # Si la condición es falsa
```

```python
# Ejemplo Sentencia if else
edad = 10
if edad >= 18:
  print("Eres mayor de edad.")
else:
  print("Eres menor de edad.")
```

### Diagrama de Flujo sentencia `if else`

Dado el siguiente código, vamos a crear el diagrama de flujo equivalente:

```python
# Ejemplo Sentencia if else
edad = 10
if edad >= 18:
  print("Eres mayor de edad.")
else:
  print("Eres menor de edad.")
```

![alt text](image-5.png)

**📄 Código :**

```python
print("*** Sentencia IF ***")

edad = 10
if edad >= 18:
    print(f"Eres mayor de edad. Tienes {edad} años")
else:
    print(f"Eres menor de edad. Tienes {edad} años")
```

**🟢 Ejecutar:**

```console
*** Sentencia IF ***
Eres menor de edad. Tienes 10 años
```

## Sentencia `if` `elif` `else`

La sentencia `elif` es una abreviatura de `else if`, y se utiliza cuando necesitamos verificar múltiples condiciones, una tras otra.

Se pueden agregar tantas nuevas condiciones de tipo `elif` como necesitemos, pero deben después de un `if` y antes de un `else`.

```python
# Sintaxis sentencia if else
if condicion1:
  # Bloque de código condicion1 True
elif condicion2:
  # Bloque de código condicion2 True
else:
  # Bloque de código condiciones False
```

```python
# Ejemplo sintaxis if elif else
edad = 16
if edad >= 18:
  print("Eres mayor de edad.")
elif 13 <= edad < 18:
  print("Eres un adolescente.")
else:
  print("Eres un niño.")
```

![alt text](image-6.png)

**📄 Código :**

```python
print("*** Sentencia IF ***")

edad = 9
if edad >= 18:
    print(f"Eres mayor de edad. Tienes {edad} años")
elif 13 <= edad < 18:
    print(f"Eres un adolescente. Tienes {edad} años")
else:
    print(f"Eres un niño. Tienes {edad} años")
```

**🟢 Ejecutar:**

```console
*** Sentencia IF ***
Eres un niño. Tienes 9 años
```

## Ejemplo Valor Positivo

![alt text](image-7.png)

**📄 Código :**

```python
print("*** Ejemplo Valor Positivo ***")

numero = int(input("Proporciona un número positivo: "))

if numero > 0:
    print(f"Número es positivo: {numero}")
elif numero < 0:
    print(f"Número es negativo: {numero}")
else:
    print(f"Número es cero: {numero}")
```

**🟢 Ejecutar:**

```console
*** Ejemplo Valor Positivo ***
Proporciona un número positivo: -3
Número es negativo: -3
```

## Tienda en línea

Crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o si es miembro de la tienda.

Se deben revisar las siguientes condiciones:

1. Si ha comprado más de $1,000 y es miembro -> descuento de 10%
2. Si sólo es miembro de la tienda -> Descuento del 5%
3. Si no es miembro mi compro más de $1,000 -> Descuento del 0%

**📄 Código :**

```python
print("*** Sistema Tienda en Línea con Descuentos ***")

# condiciones
MONTO_COMPRA_DESC = 1000

monto_compra = float(input("¿Cuál fue el monto de tu compra?: "))
es_miembro = input("¿Eres miembro de la tienda (Si/No)?: ")

descuento = 0
# verificar cada case, con los datos proporcionados
if monto_compra >= MONTO_COMPRA_DESC and es_miembro.strip().lower() == "si":
    descuento = 0.1  # Descuento del 10%
elif es_miembro.strip().lower() == "si":
    descuento = 0.05  # Descuento del 5%
elif monto_compra >= MONTO_COMPRA_DESC:
    descuento = 0.03  # Descuento del 3%
else:
    descuento = 0

# Hacemos los cálculos respectivos para obtener el monto final
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(
        f"""
Felicidades, has obtenido un descuento del {descuento * 100:.0f}%
Monto de la compra: ${monto_compra:.2f}
Monto del descuento: ${monto_descuento:.2f}
Monto final de la compra con descuento: ${monto_final:.2f}
          """
    )
else:
    print(
        f"""
No obtuviste ningún tipo de descuento
Te invitamos a hacerte miembro de la tienda
Monto final de la compra: ${monto_compra:.2f}
          """
    )

```

**🟢 Ejecutar:**

```console
*** Sistema Tienda en Línea con Descuentos ***
¿Cuál fue el monto de tu compra?: 1500 
¿Eres miembro de la tienda (Si/No)?: si

Felicidades, has obtenido un descuento del 10%
Monto de la compra: $1500.00
Monto del descuento: $150.00
Monto final de la compra con descuento: $1350.00
```
