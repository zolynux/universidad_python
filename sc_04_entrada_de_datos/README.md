# Entrada de Datos

**Conversión de tippos de datos:**

La conversiós de tipos de datos, también conocida como casting, es una técnica para manipular datos que no están en el tipo requerido.

Podemos hacer conversiones desde y hacia distintos tipos de datos

- **Convertir a entero** -> Función `int()`
- **Convertir a flotante** -> Función `float()`
- **Convertir a cadena** -> Función `str()`
- **Convertir a booleano** -> Función `bool()`

**📄 Código :**

```python
# Conversión de Tipos de datos

# Convertir de cadena a numero
numero_cadena = "10"
numero_entero = int(numero_cadena)
print(f"Valor numérico en cadena: {numero_cadena}")
print(f"Cadena a entero: {numero_cadena}")

# Convertir de cadena a flotante
numero_cadena = "3.14"
numero_flotante = float(numero_cadena)
print(f"Cadena a flotante: {numero_flotante}")

# Convertir de Numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f"Valor numero a cadena: {numero_cadena}")

# Convertir a booleano
# tipo bool es False en los siguientes casos
# Si el valor es 0, cadena vacío, o None, entonce regresa False
# Regresa True, si el valor es distinto de 0, si es distinto de cadena vacia
# y también si es distinto de None
numero_entero = 0
booleano = bool(numero_entero)
print(f"Valor booleano de 0: {booleano}")  # False, incluye 0, 0.0

numero_entero = 5
booleano = bool(numero_entero)
print(f"Valor booleano de 1: {booleano}")  # True

cadena = ""  # El largo de la cadena es 0
booleano = bool(cadena)
print(f"Valor booleano de cadena vacía: {booleano}")  # False

cadena = "Cadena con valor"
booleano = bool(cadena)
print(f"Valor booleano de cadena NO vacía: {booleano}")  # True

ninguno = None
booleano = bool(ninguno)
print(f"Valor booleano de None: {booleano}")  # False
```

**🟢 Ejecutar:**

```console
Valor numérico en cadena: 10
Cadena a entero: 10
Cadena a flotante: 3.14
Valor numero a cadena: 25
Valor booleano de 0: False
Valor booleano de 1: True
Valor booleano de cadena vacía: False
Valor booleano de cadena NO vacía: True
Valor booleano de None: False
```

## Ejemplo de Conversión de Tipos de Datos

**📄 Código :**

```python
# Ejemplo tipos de datos

# Ejemplo de concatenación o suma de valores
numero1_cadena = "10"
print(f"Número 1 en cadena: {numero1_cadena}")
numero2_cadena = "20"
print(f"Número 2 en cadena: {numero1_cadena}")
resultado = numero1_cadena + numero2_cadena
print(f"concatenación: {resultado}")

# Convertimos a tipos enteros
numero1_cadena = int(numero1_cadena)
numero2_cadena = int(numero2_cadena)
resultado = numero1_cadena + numero2_cadena
print(f"Suma: {resultado}")
```

**🟢 Ejecutar:**

```console
Número 1 en cadena: 10
Número 2 en cadena: 10
concatenación: 1020
Suma: 30
```

## Entrada de Datos por Conosla

En Python, la entrada de datos se realiza usando la función `input()`

Esta función puasa la ejecución del programa y espera a que el usuario introduzca algún texto desde el teclado.

Una vez que el usuario presiona Enter, el texto introducido se devuelve como una cadena (str)

### Características de la función `input`

- **Interactividad:** Permite a los usuarios de nuestros programas proporcionar valores dinámicos, en lugar de utilizar valores en código duro o estáticos.
- **Sencillez:** La función `input` es muy fácil de usar y solo necesita, opcionalmente, indicar la cadena o mensaje a mostrar al usuario, para que éste sepa lo que se le está solicitando.
- **Tipo de Datos:** Siempre devuelve una cadena, si riquiere otro tipo hay que Convertirlo

**📄 Código :**

```python
# Entrada de datos por consola

nombre = input("Introduce tu nombre: ")
print(f"Recibiendo el valor de nombre: {nombre}")

# Pedir la edad al usuario (entra como cadena, y lo convertirmos a numero)
edad = int(input("Introduce tu edad: "))
print(f"Tu edad es: {edad}, y en un año tendras {edad + 1}")
```

**🟢 Ejecutar:**

```console
Introduce tu nombre: Juan
Recibiendo el valor de nombre: Juan
Introduce tu edad: 32
Tu edad es: 32, y en un año tendras 33
```

## Sistema de Empleados

Crea un programa para solicitar la información de un empleado, introduciendo los datos por consola.

- Nombre Empleado
- Edad del Empleado (convertir a entero)
- Salario del Empleado (convertir a flotante)
- Es jefe de departamento (Si/No)

**📄 Código :**

```python
estrella = "*" * 3
print(estrella, "Sistema de Empleado", estrella)

nombre_empleado = input("Nombre del empleado: ")
edad_empleado = int(input("Edad del empleado: "))
salario_empleado = float(input("Salario de empleado: "))
es_jefe_departamento = str(input("¿Es jefe de departamento (Si/No)? "))


# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"

# Imprimir los valores del Empleado
print()
print(estrella, "Datos del Empleado", estrella)
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario: {salario_empleado:.2f}")
print(f"Jefe de departamento es: {es_jefe_departamento}")
```

**🟢 Ejecutar:**

```console
*** Sistema de Empleado ***
Nombre del empleado: Juan Gomez
Edad del empleado: 32
Salario de empleado: 34223.253
¿Es jefe de departamento (Si/No)?No

*** Datos del Empleado ***
Nombre: Juan Gomez
Edad: 32
Salario: 34223.25
Jefe de departamento es: False
```

## Receta de Cocina

Crear un programa para solicitar algunos valores importante para una receta de cocina.

Los valores que debe introducir el usuario son:

- Nombre de la receta
- Ingredientes
- Tiempo de preparación (en minutos)
- Dificultad (Facil, Media, Alta)

Mandar a imprimir la receta

**📄 Código :**

```python
estrella = "*" * 3
print(f"{estrella} Receta de Cocina {estrella}")
nombre_receta = str(input("Ingresa el nombre de la receta: "))
ingredientes = str(input("Ingresa los ingredientes: "))
tiempo_preparacion = int(input("Ingresa el tiempo de preparación (min): "))
dificultad = str(input("Ingresa la dificultad: "))

print("-" * 20)
print(f"Nombre receta: {nombre_receta}")
print(f"Ingredientes: {ingredientes}")
print(f"Tiempo de preparación: {tiempo_preparacion}")
print(f"Dificultad: {nombre_receta}")
```

**🟢 Ejecutar:**

```console
*** Receta de Cocina ***
Ingresa el nombre de la receta: Pasta con brocolis
Ingresa los ingredientes: Pasta fusili, brocoli, nueces de brasil espinaca y aceite de oli
va
Ingresa el tiempo de preparación (min): 10
Ingresa la dificultad: Fácil
--------------------
Nombre receta: Pasta con brocolis
Ingredientes: Pasta fusili, brocoli, nueces de brasil espinaca y aceite de oliva
Tiempo de preparación: 10
Dificultad: Pasta con brocolis
```

## Generar valores aleatorios

La función `randint()`, que es parte de módulo `random`, nos permite generar números aleatorios

`randint(a, b)` devuelve un número aleatorio entre a y b, incluyendo estos valores.

Es necesario importar en primer línea el módulo `random` antes de usar la función `randint()```

Para importar un módulo, usamos la sintaxis `import random`

**📄 Código :**

```python
## Valores aleatorios con la función randint

#import random
import random 

# Generar un numero aleatorio entre 1 y 10
numero = random.randint(1, 10)
print(f'Numero aleatorio entre 1 y 10: {numero}')

# Simular un dado de seis caras
dado = random.randint(1, 6)
print(f'Resultado de lanzar el dado: {dado}')
```

**🟢 Ejecutar:**

```console
Numero aleatorio entre 1 y 10: 4
Resultado de lanzar el dado: 4
```

## Reto Generador de ID Único

Con los datos recibidos el sistema deberá realizar lo siguiente:

1. Del valor recibido de nombre, usar sólo los 2 primeras letras y convertirlas a mayúsculas
2. Del valor de apellido, usar las 2 primeras letras y convertirlas a mayúsculas.
3. Del valor de año, tomar los 2 últimos digitos.

Además, el sistema deberá generar un valor aleatorio de 4 dígitos, con ayuda de la función rantint

Finalmente, con los datos obtenidos generar un ID único uniendo los valores como sigue:

**Ejemplo:**

```txt
Nombre -> Juan -> JU
Apellido -> Perez -> PE
Año nacimiento -> 1995 -> 95
Valor aleatorio -> randint -> 7326

Resultado ID Único: JUPE957326
```

**📄 Código :**

```python
from random import randint

print("*** Sistema Generador de ID Único ***")

nombre = str(input('¿Cuál es tu nombre?: '))
apellido = str(input('¿Cuál es tu apellido?: '))
anio_nacimiento = str(input('¿Cuál es tu año de nacimiento (YYYY)?: '))


# Normalizar los valores

nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:] # También puede ser [2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el valorr de id único
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}'

print(f'''\nHola {nombre},
      Tu nuevo número de identificación (ID) generador por el sistema es:
      {id_unico}
¡Felicitaciones!''')
```

**🟢 Ejecutar:**

```console
*** Sistema Generador de ID Único ***
¿Cuál es tu nombre?: Juan
¿Cuál es tu apellido?: Perz
¿Cuál es tu año de nacimiento (YYYY)?: 1995

Hola Juan,
      Tu nuevo número de identificación (ID) generador por el sistema es:
      JUPE952106
¡Felicitaciones!
```

## Sistema Generador de Email

Se solicita crear una nueva versión del sistema generador de emails.

Para generar un email se debe solicitar

- Nombre -> ej. Juan Carlos
- Apellido -> ej. Gómez lara
- Nombre Empresa -> ej. Global Mentoring
- Extensión Dominio -> Ej. .com.mx

El resultado debe ser:
`juan.carlos.gomez.lara@globalmentoring.com.mx`

**📄 Código :**

```python
print("*** Sistema Generador de Emails ***")
nombre = input("¿Cual es tu nombre?: ")
apellidos = input("¿Cuales son tus apellidos?: ")
empresa = input("¿Nombre de tu empresa?: ")
extension_dominio = input("¿Extensión de dominio de tu empresa?: ")

# Normalizamos los valores recibidos.
nombre = nombre.strip().lower().replace(" ", ".")
apellidos = apellidos.strip().lower().replace(" ", ".")
empresa = empresa.strip().lower().replace(" ", "")
extension_dominio = extension_dominio.strip().lower().replace(" ", "")

# Generar el email

email = f"{nombre}.{apellidos}@{empresa}{extension_dominio}"

print(
    f"""
Tu nuevo email generado por el sistema de es:
      {email}
¡Felicidades!"""
)
```

**🟢 Ejecutar:**

```console
*** Sistema Generador de Emails ***
¿Cual es tu nombre?: Juan Carlos
¿Cuales son tus apellidos?: Gomez Lara
¿Nombre de tu empresa?: Global Mentoring
¿Extensión de dominio de tu empresa?: .com.mx

Tu nuevo email generado por el sistema de es:
      juan.carlos.gomez.lara@globalmentoring.com.mx      
¡Felicidades!
```
