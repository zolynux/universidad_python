
# Operadores

Los operadores son símbolos especiales que están disñados para realizar operaciones específicas. Tenemos varios tipos, como son:

- **Operadores Aritméticos:** Permiten realizar cálculos matemáticos básicos, como suma, resta, multiplicación o división.
- **Operadres de asisgnació:** Se utilizan para asignar valores a variables.
- **Operadores de Comparación:** Se utiliza para comparar un valor con otro.
- **Operadores Lógicos:** Se utilizan para combinar expreseiones condicionales o lógicas
- **Operadores de Identidad:** Se utlizan para comparar si dos variables son el mismo objeto.
- **Operadores de membresía:** Se utilizan para poder probar si una secuencia (Ej. una subcadena) se presenta en un objeto.

## Operadores Aritméticos

Los operadores aritméticos nos permiten realizar cálculos matemáticos básicos entre números. Por ejemplo:

- **Suma (`+`):** Suma dos operandos
- **Resta (`-`):** Resta dos operandos
- **Multiplicación (`*`):** Multiplica dos operandos
- **División (`/`):** Divide el primer operando enter el segundo. Resulta un valor flotante.
- **División Entera (`//`):** Divide el primer operando entre el segundo. Resulta un tipo entero.
- **Módulo (`%`):** Regresa el residuo de la división.
- **Exponente (`**`):** Eleva el primer operando a la potencia del segunda.

**📄 Código :**

```python
# Operadores Aritméticos

a = 10
b = 3

# Suma +
suma = a + b
print(f"Suma: {suma}")

# Resta -
resta = a - b
print(f"Resta: {resta}")

# Multiplicación *
multiplicacion = a * b
print(f"Multiplicación: {multiplicacion}")

# División / (retorna un tipo flotante)
division = a / b
print(f"División: {division:.2f}")

# División Entera //
division_entera = a // b
print(f"División Entera: {division_entera}")

# Módulo %
modulo = a % b
print(f"Módulo: {modulo}")

# Exponente **
exponente = a**b
print(f"Exponente: {exponente}")
```

**🟢 Ejecutar:**

```console
Suma: 13
Resta: 7
Multiplicación: 30
División: 3.33
División Entera: 3
Módulo: 1
Exponente: 1000
```

## Operadores de Asignación

El operador de asignación se utiliza para asignar un valor a una variable, y se utiliza el carácter (`=`)

```python
# Sintaxis Operador asignación
variable = valor
```

```python
# Ejemplo Operador Asignación
numero = 10
texto = "Hola, mundo"
```

En Python también tenemos la asignación múltiple, lo que nos permite asignar valores a varias variables en una sola línea de código.. El código es más compacto y fácil de leer

```python
# Sintaxis de Asignación Múltiple
variable1, variable2 = valor1, valor2
```

```python
# Ejemplo de Asignación Múltiple
a, b, c = 10, 'Saludo', 14.5
```

### Asignación Encadenada

En Python también contamos con la asignación encadenada. Esto permite asignar el mismo valor a múltiples variables.

```python
# Sintaixs de Asignación Encadenada
variable1 = variable2 = ... = valor
```

```python
# Ejemplo. Inicializar contadores
contador1 = contador2 = 0
```

**📄 Código :**

```python
print("*** Operadores de Asignación ***")
numero = 5
print(f"Valor de la variable numero: {numero}")
numero = 10
print(f"Valor de la variable numero: {numero}")
cadena = "Hola, mundo"
print(f"Valor de la variable cadena: {cadena}")

# Asignación Múltiple
a, b, c = 10, "Saludo", 14.5
print(f"Valor de a = {a}, b = {b}, c = {c}")

# Asignación Encadenada
x = y = z = 10
print(f"Valor de x = {x}, y = {y}, z = {z}")
```

**🟢 Ejecutar:**

```console
*** Operadores de Asignación ***
Valor de la variable numero: 5
Valor de la variable numero: 10
Valor de la variable cadena: Hola, mundo
Valor de a = 10, b = Saludo, c = 14.5
Valor de x = 10, y = 10, z = 10
```

## Asingación Multiple

**📄 Código :**

```python
print("*** Operadores de Asignación ***")
numero = 5
print(f"Valor de la variable numero: {numero}")
numero = 10
print(f"Valor de la variable numero: {numero}")
cadena = "Hola, mundo"
print(f"Valor de la variable cadena: {cadena}")

# Asignación Múltiple
a, b, c = 10, "Saludo", 14.5
print(f"Valor de a = {a}, b = {b}, c = {c}")

# Asignación Encadenada
x = y = z = 10
print(f"Valor de x = {x}, y = {y}, z = {z}")

# Intercambio de valores de una variable, sin utilizar variables temporales.
x, y = 5, 10
print(f"Valor de iniciales x = {x}, y = {y}")
# Aplicando el concepto de asignación múltiple, intercambiamos los valores de las variables x y y.
x, y = y, x
print(f"Valor de intercambio x = {x}, y = {y}")

# Recibir múltiples valores de la entrada del usuario
nombre, apellido = input("Ingresa tu nombre y apellido separados por coma: ").split(",")
print(f"Nombre: {nombre.strip()}, Apellido: {apellido.strip()}")
```

**🟢 Ejecutar:**

```console
*** Operadores de Asignación ***
Valor de la variable numero: 5
Valor de la variable numero: 10
Valor de la variable cadena: Hola, mundo
Valor de a = 10, b = Saludo, c = 14.5
Valor de x = 10, y = 10, z = 10
Valor de iniciales x = 5, y = 10
Valor de intercambio x = 10, y = 5
Ingresa tu nombre y apellido separados por coma: Juan, Perez
Nombre: Juan, Apellido: Perez
```

## Operadores de Arignación Compuestos

Los operadores de asignación compuesto combinan una operación aritmética con una asignación, haciendo las operaciones más conscisas

Los operadores pueden ser +=, -=, *=, /=, etc.
Operador `=`

```python
# Sintaxis operador Asignación compuesto
variable OPERADOR= valor
```

```python
# Ejemplo Operador Asginación Compuesto
contador = 0
contador += 1 # contador = contador + 1
```

**📄 Código :**

```python
print("*** Operadores de Asignación Compuestos ***")
a, b = 10, 15
print(f"Valor de a = {a}, b = {b}")

# Operador de Asignación Compuesto suma +=
a += b  # a = a + b
print(f"Valor de suma a = {a}, b = {b}")

# Operador de Asignación Compuesto resta -=
a = 10
a -= b  # a = a - b
print(f"Valor de resta a = {a}, b = {b}")

# Operador de Asignación Compuesto multiplicación *=
a = 10  # reiniciamos el valor de a
a *= b  # a = a * b
print(f"Valor de multiplicación a = {a}, b = {b}")

# Operador de Asignación Compuesto división /=
a = 10  # reiniciamos el valor de a
a /= b  # a = a / b
print(f"Valor de división a = {a}, b = {b}")

# Operador de Asignación Compuesto división entera //=
a = 10  # reiniciamos el valor de a
a //= b  # a = a // b
print(f"Valor de división entera a = {a}, b = {b}")

# Operador de Asignación Compuesto módulo %=
a = 10  # reiniciamos el valor de a
a %= b  # a = a % b
print(f"Valor de módulo a = {a}, b = {b}")

# Operador de Asignación Compuesto exponenciación **=
a, b = 10, 2  # reiniciamos el valor de a
a **= b  # a = a ** b
print(f"Valor de exponenciación a = {a}, b = {b}")
```

**🟢 Ejecutar:**

```console
Valor de a = 10, b = 15
Valor de suma a = 25, b = 15
Valor de resta a = -5, b = 15
Valor de multiplicación a = 150, b = 15
Valor de división a = 0.6666666666666666, b = 15
Valor de división entera a = 0, b = 15
Valor de módulo a = 10, b = 15
```

## Operadores de Comparación

Los operadores de comparación en Python se utilizan para comparar dos valores. El resultado de una comparación es un valor booleano: `True` o `False`. Aquí tienes una lista de los operadores de comparación más comunes:

1. **Igual a (`==`)**: Comprueba si dos valores son iguales.
   ```python
   a == b
   ```

2. **Distinto de (`!=`)**: Comprueba si dos valores son diferentes.
   ```python
   a != b
   ```

3. **Mayor que (`>`)**: Comprueba si el valor de la izquierda es mayor que el de la derecha.
   ```python
   a > b
   ```

4. **Menor que (`<`)**: Comprueba si el valor de la izquierda es menor que el de la derecha.
   ```python
   a < b
   ```

5. **Mayor o igual que (`>=`)**: Comprueba si el valor de la izquierda es mayor o igual al de la derecha.
   ```python
   a >= b
   ```

6. **Menor o igual que (`<=`)**: Comprueba si el valor de la izquierda es menor o igual al de la derecha.
   ```python
   a <= b
   ```

Aquí tienes un ejemplo de cómo se pueden usar estos operadores en un programa:

```python
# Ejemplo de operadores de comparación
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
```

Estos operadores son fundamentales para controlar el flujo de un programa, especialmente en estructuras de control como condicionales (`if`, `else`) y bucles (`while`, `for`).

**📄 Código :**

```python
print("*** Operadores de Comparación ***")
a, b = 7, 5
print(f"Valor inicial: a = {a}, b = {b}")

# Operador de Igualdad
resultado = a == b
print(f"Resultado de a == b es: {resultado}")

# Operador de Desigualdad
resultado = a != b
print(f"Resultado a != b es: {resultado}")

# Operador mayor que
resultado = a > b
print(f"Resultado a > b es: {resultado}")

# Operador mayor o igual que
resultado = a >= b
print(f"Resultado a >= b es: {resultado}")

# Operador menor que
resultado = a < b
print(f"Resultado a < b es: {resultado}")

# Operador menor o igual que
resultado = a <= b
print(f"Resultado a <= b es: {resultado}")

```

**🟢 Ejecutar:**

```console
*** Operadores de Comparación ***
Valor inicial: a = 7, b = 5
Resultado de a == b es: False
Resultado a != b es: True
Resultado a > b es: True
Resultado a >= b es: True
Resultado a < b es: False
Resultado a <= b es: False
```

## Operadores Lógicos

Los operadores lógicos nos permiten combinar múltiples condiciones o valores booleanos y obtener un resultado verdadero o falso. Los principales operadores lógicos en Python son:

- `and`: Devuelve True si ambas condiciones son verdaderas
- `or`: Devuelve True si al menos una condición es verdadera  
- `not`: Invierte el valor booleano (True a False o False a True)

| a     | b     | a and b | a or b | not a |
| ----- | ----- | ------- | ------ | ----- |
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

**📄 Código :**

```python
print("*** Operador 'and' ***")
# Regresa Verdadero si ambos valores a evaluar son verdaderos
condicion1 = True
condicion2 = False
resultado = condicion1 and condicion2
print(f"Resultado {condicion1} and {condicion2} = {resultado}")
```

**🟢 Ejecutar:**

```console
*** Operador 'and' ***
Resultado True and False = False
```

### Ejemplo Descuento VIP

**📄 Código :**

```python
print("*** Sistema Descuentos VIP ***")

NO_PRODUCTOS_DESCUENTOS = 10
cantidad_productos = int(input("¿Cuántos productos compraste hoy?: "))
tiene_membresia = str(input("¿Tienes la membresía de la tienda (Si/No)?: "))

es_elegible_descuento = (
    cantidad_productos >= NO_PRODUCTOS_DESCUENTOS
    and tiene_membresia.strip().lower() == "si"
)

print(f"¿Tienes acceso al descuento VIP?: {es_elegible_descuento}")

```

**🟢 Ejecutar:**

```console
*** Sistema Descuentos VIP ***
¿Cuántos productos compraste hoy?: 12
¿Tienes la membresía de la tienda (Si/No)?: Si
¿Tienes acceso al descuento VIP?: True
```

### Operador 'or'

**📄 Código :**

```python
print("*** Operador 'or' ***")
# Regresa or regresa True si cualquiera de los operandos es True
condicion1 = True
condicion2 = False
resultado = condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2} = {resultado}")
```

**🟢 Ejecutar:**

```console
*** Operador 'or' ***
Resultado True or False = True
```

### Sistema Préstamo de Libros

Se pide crear un sistema para una biblioteca, la cual desea prestar libros si cumples con cualquiera de las siguientes condicionales.

1. El usuario tiene credencial de estudiante
2. El usuario vive a no más de 3 km a la redonda

Si cumple con cualquiera de estas condiciones se le puede prestar el libro

**📄 Código :**

```python
print("*** Sistema Préstamo de Libros ***")

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input("¿Cuentas con credencial de estudiante (Si/No)?: ")
distancia_biblioteca_km = int(input("¿A cuántos km vives de la biblioteca?: "))

es_elegible_prestamo = (
    tiene_credencial.strip().lower() == "si"
    or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM
)

print(f"¿Eres elegible para préstamo de libros?: {es_elegible_prestamo}")
```

**🟢 Ejecutar:**

```console
*** Sistema Préstamo de Libros ***
¿Cuentas con credencial de estudiante (Si/No)?: si
¿A cuántos km vives de la biblioteca?: 5
¿Eres elegible para préstamo de libros?: True
```

### Operador 'not'

**📄 Código :**

```python
print('*** Operador "not" ***')

condicion = False
print(f"Operador de variable es: {condicion}")
resultado = not condicion
print(f"Operador not store {condicion} = {resultado}")

# Revisar si una variable es cadena vacia
nombre = ""
es_cadena_vacia = not nombre
print(
    f"Varaible es cadena vacía '{nombre}'\nLa variable NO tiene ningún valor? {es_cadena_vacia}"
)

# Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(
    f"Varaible es sin valor asignado {variable} \n¿La variable NO tiene ningún valor asignado?: {es_variable_sin_valor}"
)
```

**🟢 Ejecutar:**

```console
*** Operador "not" ***
Operador de variable es: False
Operador not store False = True
Varaible es cadena vacía ''
La variable NO tiene ningún valor? True
Varaible es sin valor asignado None
¿La variable NO tiene ningún valor asignado?: True
```

### Fuera de rango - Operador not

**📄 Código :**

```python
# Revisar si una variable se encuentra dentro de rango entre 1 Y 10
dato = int(input("Proporciona un dato entero: "))

# Revisamos si está dentro de rango
# esta_dentro_rango  = 1 <= dato <= 10
# print(f'Variable está dentro de rango (entre 1 y 10): {esta_dentro_rango}')

# revisamos la lógica inversa, si el dato está fuera de rango
esta_fuera_rango = not (1 <= dato <= 10)
print(f"Variable está fuera de rango (entre 1 y 10): {esta_fuera_rango}")
```

**🟢 Ejecutar:**

```console
Proporciona un dato entero: 2
Variable está fuera de rango (entre 1 y 10): False
```

## Generación Ticket Venta

Supongamos que compramos varios artículos en el supermercado y queremos obtener el ticket de venta total incluyendo impuestos.

El sistema solicitará el precio de cada producto a comprar y el usuario deberá indicar su precio (valor de tipo de punto decimal)

El sistema debe realizar la suma de cada producto, calcular el impuesto y finalmente imprimir el total de la compra.

**📄 Código :**

```python
print("*** Generación Ticket de Venta ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio plátanos: "))

# Cálculo del subtotal (sin impuesto)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Cálculo con impousto (16%)
impuesto = subtotal * 0.16

# Calculo total de la compra (con impuesto)
costo_total_compra = subtotal + impuesto
print(
    f"""
subtotal: ${subtotal:.2f}
impuesto: ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}
      """
)
```

**🟢 Ejecutar:**

```console
*** Generación Ticket de Venta ***
Precio leche: 10
Precio pan: 5
Precio lechuga: 6
Precio plátanos: 9

subtotal: $30.00
impuesto: $4.80
Costo total de la compra: $34.80
```

### Generación Ticket de Venta con Descuento

**📄 Código :**

```python
print("*** Generación Ticket de Venta ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio plátanos: "))
descuento_porcentaje = int(input("¿Aplicar algún descuento (%)?: "))

# Cálculo del subtotal (sin impuesto)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje / 100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Cálculo con impousto (16%)
impuesto = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuesto)
costo_total_compra = subtotal_con_descuento + impuesto
print(
    f"""
subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje})
Subtotal: con descuento: ${subtotal_con_descuento}
impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}
      """
)
```

**🟢 Ejecutar:**

```console
*** Generación Ticket de Venta ***
Precio leche: 10
Precio pan: 5
Precio lechuga: 6
Precio plátanos: 9
¿Aplicar algún descuento (%)?: 10

subtotal: $30.00
Descuento: $3.0 (10)
Subtotal: con descuento: $27.0
impuesto (16%): $4.32
Costo total de la compra: $31.32
```

## Sistema de Autenticación

Crea un programa para validar el usuairo y password proporcionados por el usuario

crea 2 constantes con los valores correctos y posteriormente compara que el usuario y password proporcionados por el usuario sean válidos.

Debe solicitar el usuario y el password al usuario y si son iguales que los valorss correctos almacenados en las contantes debe imprimir True, de lo contrario debe imprimir False.

**📄 Código :**

```python
print("*** Sistema Autenticación ***")

USUARIO_VALIDO = "admin"
PASSWORD_VALIDO = "123"
usuario = input("¿Cuál es tu usuario?: ")
password = input("¿Cuál es tu contraseña?: ")

valido = usuario.strip() == USUARIO_VALIDO and password.strip() == PASSWORD_VALIDO

print(f"¿Datos correctos?: {valido}")
```

**🟢 Ejecutar:**

```console
*** Sistema Autenticación ***
¿Cuál es tu usuario?: admin
¿Cuál es tu contraseña?: 123 
¿Datos correctos?: True
```

## Valor Dentro de Rango

Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado está dentro de rango.

Se deben definir 2 constante, `VALOR_MINIMO = 0` y `VALOR_MAXIMO = 5`

Y debemos comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5

Finalmente se debe imprimir: `valor dentro de rango: {True/False}`

**📄 Código :**

```python
print("*** Valor Dentro de Rango ***")

VALOR_MINIMO, VALOR_MAXIMO = 0, 5

numero = int(input("Proporciona un número dentro de rango entre 0 y 5: "))

# rango = numero >= VALOR_MINIMO and numero <= VALOR_MAXIMO
rango = VALOR_MINIMO <= numero <= VALOR_MAXIMO  # exactamente la misma de linea anterior

print(f"Valor dentro de rango: {rango}")
```

**🟢 Ejecutar:**

```console
*** Valor Dentro de Rango ***
Proporciona un número dentro de rango entre 0 y 5: 4
Valor dentro de rango: True
```

## Cálculo Área y Perímetro de un rectángulo

Se solicita calcular el área y perímetro de un rectángulo aplicando las siguientes fórmulas:

![alt text](image.png)

```python
area = base * altura
perimetro = 2 * (base + altura)
```

**📄 Código :**

```python
print("*** Cálculo Área y Perímetro de un Rectángulo ***")

base = float(input("Ingresa la base (cm) del rectángulo: "))
altura = float(input("Ingresa la altura (cm) del rectángulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")
```

**🟢 Ejecutar:**

```console
*** Cálculo Área y Perímetro de un Rectángulo ***
Ingresa la base (cm) del rectángulo: 5
Ingresa la altura (cm) del rectángulo: 2
El área del rectángulo es: 10.0
El perímetro del rectángulo es: 14.0
```

## Precedencia de Operadores

La precedencia de operadores determina el orden en que se evalúan los operaciones en una expresión.

Python aplica la siguiente tabla para asegurar que algunos operadores tengan mayor prioridad que otros durante la evaluación de expresiones.

1. Operador de paréntesis `()`
2. Exponente `**`
3. Unarios `+x`, `-x`
4. Multiplicación, División y Módulo `*`, `/`, `//`, `%`
5. Suma y resta `+`, `-`
6. Comparación `==`, `!=`, `>`, `>=`, `<`, `<=`
7. Operadores Lógicos `not`, `and` y `or`
8. Operadores Asignación `=`, `+=`, `-=`, `/=`, `%=`, `//==`, `**=`

```python
resultado = 5 + 3 * 2 ** 2 # 17
resultado = (5 + 3) * 2 ** 2 # 32
```

**📄 Código :**

```python
print("*** Precedencia de Operadores ***")
# Ejemplo de precedencia de operadores
# 1. División 12 / 3 = 4
# 2. Multiplicación 2 * 3 = 6
# 3. Suma 4 + 6 = 10
# 4. Resta 10 - 1 = 9
resultado = 12 // 3 + 2 * 3 - 1
print(f"Resultado: {resultado}")

```

**🟢 Ejecutar:**

```console
*** Precedencia de Operadores ***
Resultado: 9
```
