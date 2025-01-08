# Universidad Python - Cero a Experto (+86 horas) 🐍

## Tabla de Contenido

* [Universidad Python - Cero a Experto (+86 horas) 🐍](#universidad-python---cero-a-experto-86-horas-)
    * [Tabla de Contenido](#tabla-de-contenido)
    * [Introducción a Python](#introducción-a-python)
        * [Instalación de Python](#instalación-de-python)
        * [Hola Mundo con Python](#hola-mundo-con-python)
        * [Ejercicio Preséntate](#ejercicio-preséntate)
    * [Variables](#variables)
        * [Sintaxis para definir una variable](#sintaxis-para-definir-una-variable)
            * [Variables y la Memoria RAN](#variables-y-la-memoria-ran)
        * [Variables y la Memoria RAM](#variables-y-la-memoria-ram)
            * [Variables y Memoria Simplificado](#variables-y-memoria-simplificado)
        * [Ejemplo de Variables](#ejemplo-de-variables)
        * [Modificar Variables](#modificar-variables)
        * [Modificar variables](#modificar-variables-1)
        * [Reglas y buenas prácticas en nombres de variables](#reglas-y-buenas-prácticas-en-nombres-de-variables)
            * [Convenciones y buenas prácticas](#convenciones-y-buenas-prácticas)
        * [Ejemplo de regla de nombre de variables](#ejemplo-de-regla-de-nombre-de-variables)
        * [Tipos de datos](#tipos-de-datos)
        * [Ejemplo de Tipos de datos](#ejemplo-de-tipos-de-datos)
        * [Sistema de Reserva de Hoteles](#sistema-de-reserva-de-hoteles)
        * [Sistema Tienda Online](#sistema-tienda-online)
        * [Constantes](#constantes)
    * [Manejo de Cadenas](#manejo-de-cadenas)
        * [Manejo de Cadenas](#manejo-de-cadenas-1)
        * [Detalle de una Cadena](#detalle-de-una-cadena)

## Introducción a Python

![img.png](img.png)

Python es un lenguaje de programación muy popular que es conocido por ser fácil de aprender y utilizar. Fue creado por
Guido van Rossum y lanza por primera vez en 1992. La simplicidad de Python permite a los programadores escribir menos
líneas de código para realizar tareas en comparación con otros lenguajes de programación. Esto lo hace ideal para
principiantes, así como para desarrolladores experimentados que buscan desarrollar proyectos de manera rápida y
eficiente.
Python es muy versátil, lo que significa que se puede usar en una variedad de aplicaciones, desde desarrollo web hasta
ciencia de datos, inteligencia artificial y más. Es apoyado por una gran comunidad de desarrolladores que contribuyen
constantemente con nuevas bibliotecas y herramientas para hacer que el lenguaje sea aún más poderoso y accesible.
Además, Python es un lenguaje de programación de alto nivel, lo que significa que se parece mucho al Inglés, facilitando
su comprensión y aprendizaje.
Python tiene varias características que lo hacen muy atractivo para una amplia gama de programadores, desde
principiantes hasta expertos. Aquí te detallo algunas de las principales:

1. **Sintaxis clara y legible:** Python fue diseñado con la legibilidad en mente, lo que significa que su código se
   asemeja al inglés. Esto facilita su comprensión y aprendizaje, además de permitir a los desarrolladores escribir
   código limpio y bien estructurado.
2. **Tipado dinámico:** En Python, no necesitas declarar el tipo de una variable cuando la creas. El tipo de dato de una
   variable se determina en tiempo de ejecución, lo que hace que el lenguaje sea más flexible y fácil de usar.
3. **Gestión automática de memoria:** Python maneja automáticamente la memoria, lo que significa que el programador no
   tiene que preocuparse por detalles complejos como la asignación y liberación de memoria.
4. **Bibliotecas extensas:** Python viene con una gran biblioteca estándar que incluye módulos para realizar una gran
   variedad de tareas, desde expresiones regulares hasta la creación de servidores web. Además, hay muchas más
   bibliotecas disponibles que extienden aún más las capacidades de Python.
5. **Multiparadigma:** Aunque es principalmente un lenguaje de programación orientado a objetos, Python también soporta
   otros paradigmas de programación, como la programación imperativa y funcional.
6. **Portabilidad:** Los programas escritos en Python pueden ejecutarse en múltiples plataformas sin necesidad de
   cambiar el código. Python es compatible con sistemas operativos como Windows, MacOS, Linux, entre otros.
7. **Interpretado:** Python es un lenguaje interpretado, lo que significa que los programas se ejecutan directamente
   desde el código fuente, sin necesidad de un paso de compilación previo.
8. **Extensible:** Si necesitas un bloque de código que debe ejecutarse muy rápido o quieres reutilizar bibliotecas de
   otros lenguajes como C o C++, Python permite integrar estas partes fácilmente.
9. **Comunidad grande y activa:** Python tiene una comunidad muy grande y activa de desarrolladores y usuarios que
   contribuyen regularmente con herramientas, documentación y soporte, lo que facilita encontrar recursos y aprender.

Estas características hacen que python sea una opción muy popular para todo tipo de proyectos, desde aplicaciones web
simples hasta sistemas complejos de aprendizaje automático.

### Instalación de Python

Instalar Python en tu computadora es un proceso bastante sencillo, y lo mejor de todo es que puedes comenzar a programar
rápidamente después de la instalación.

### Hola Mundo con Python

**Código 📄:**

```python
# Programa de Hola Mundo con Python
print("Hola Mundo")
print("Saludos")
```

**🟢 Ejecutar:**

```console
Hola Mundo
Saludos
```

### Ejercicio Preséntate

Realizar un programa un Python para presentarte.

La salida de tu programa debe ser similar al siguiente:

````text
Nombre: Juan 
Edad: 29
Pais: Colombia
````

**Código 📄:**

````python
# Ejercicio de Presentación con Python
print("Nombre: Juan")
print("Edad: 29")
print("País: Colombia")
````

**🟢 Ejecutar:**

```console
Nombre: Juan 
Edad: 29
Pais: Colombia
```

## Variables

Una variable en Python es un nombre que almacena valor guardado en la memoria temporal de la computadora o dispositivo.

Las variables en Python son dinámicas, por lo que pueden almacenar cualquier tipo en cualquier momento.

Algunos tipos de datos o valores que puede almacenar una variable son texto (cadenas o string), números enteros o con
punto flotante, valores lógicos o booleanos, lista, entre varios tipos más.

### Sintaxis para definir una variable

```python
# Sintaxis para definir una variable
nombre_de_la_variable = valor
```

**Ejemplo de Variables:**

```python
# Declaración de variables y asignación de valores
nombre = "María"
edad = 30
peso = 65.5
es_casado = False
```

#### Variables y la Memoria RAN

En Python, cada vez que creamos una variable y le asignamos un valor, estamos reservando espacio en memoria RAN (Random
Access Memory) o memoria de corto plazo

**Ejemplo:**

| Paso | Variable y valores | RAM  | Dir. Memoria (hex) |
|------|--------------------|------|--------------------|
| 1    | edad = 30          | 30   | 0x333              |
| 2    | edad=60.5          | 60.5 | 0x444              |
| 3    | edad = 32          | 32   | ...                |

### Variables y la Memoria RAM

En Python, cada vez que creamos una variable y le asignamos un valor, estamos reservando espacio en la memoria RAM.

**Ejemplo:**

````python
edad = 30
altura = 1.75
````

![img_1.png](img_1.png)

#### Variables y Memoria Simplificado

Para simplificar la explicación de creación de variables, de momento usaremos la siguiente explicación:

````python
edad = 30
altura = 1.68
````

![img_2.png](img_2.png)

### Ejemplo de Variables

**Código 📄:**

```python
# Variables en Python

# Declaración e inicialización de variables
edad = 28
altura = 1.65
pais = "Colombia"

# Acceder a las variables
print("Edad:", edad)
print("Altura:", altura)
print("Pais", pais)
```

**🟢 Ejecutar:**

```console
Edad: 28
Altura: 1.65
Pais Colombia
```

### Modificar Variables

**Código 📄:**

```python
# Variables en Python

# Declaración e inicialización de variables
edad = 28
altura = 1.65
pais = "Colombia"

# Acceder a las variables
print("Edad:", edad)
print("Altura:", altura)
print("Pais", pais)
```

**🟢 Ejecutar:**

```console
Edad: 28
Altura: 1.65
Pais Colombia
```

### Modificar variables

**Código 📄:**

````python
# Variables en Python

# Declaración e inicialización de variables
edad = 28
altura = 1.65
pais = "Colombia"

# Acceder a las variables
print("Valores iniciales: ")
print("Edad:", edad)
print("Altura:", altura)
print("Pais", pais)

# Modificar el valor de una variable
edad = 30
altura = 1.68

# Acceder a las variables
print("Valores Modificados: ")
print("Edad:", edad)
print("Altura:", altura)
print("Pais", pais)

# En Python el tipo es dinámico
edad = "treinta"
print("Edad:", edad)

# Si queremos acceder a una variable no declarada manda error
telefono = "23156165"
print("Teléfono:", telefono)
````

**🟢 Ejecutar:**

````console
Valores iniciales: 
Edad: 28
Altura: 1.65
Pais Colombia
Valores Modificados: 
Edad: 30
Altura: 1.68
Pais Colombia
Edad: treinta
````

### Reglas y buenas prácticas en nombres de variables

- Los nombres de variables pueden tener letras (mayúsculas o minúsculas), dígitos, y guiones bajos (_)
- El nombre NO puede comenzar con dígitos
- No se puede usar palabras reservadas del lenguaje (keyword), Ejemplo: `for`, `if`, `class` , `try`, etc.
- Python es sensible a mayúsculas y minúsculas. Ejemplo: mi_nombre es distinto a Mi_nombre

#### Convenciones y buenas prácticas

- **snake case:** Es recomendable usar la notación de snake case, es decir, palabras en minúsculas separadas por guion
  bajo. Ejemplo: nombre_usuario, nombre_completo, etc.
- Nombres descriptivos: Los nombres de las variables deben reflejar el contenido de la variable. Ejemplo; no usar e,
  sino
  edad. No usar n, sino nombre, etc.
- Evitar nombres de un sólo caracter, ya que no son descriptivos y pueden ser confusos.

### Ejemplo de regla de nombre de variables

**Código 📄:**

```python
# Regla y convenciones en nombres de variables

# Ejemplo de reglas estrictas
nombre_usuario = "Juan Perez"
# 1nombre_usuario = "Karla Gomez"

# No podemos usar las palabras reservadas
# class = "Mi clase"
klass = 'Mi clase'

# Sensibles a mayusculas y minusculas
nombre = 'Juan'
Nombre = 'Karla'
print(nombre)
print(Nombre)
# print(NOMBRE) # esta variable no ha sido definido

# snake case
nombre_completo = "Ricardo Esparza"

# Prefijos y sufijos
es_casado = False
nombre_txt = 'archivo.txt'
```

**🟢 Ejecutar:**

```console
Juan
Karla
```

### Tipos de datos

Python es un lenguaje de tipado dinámico, por lo que no hay necesidad de indicar el tipo de la variable al momento de
declararla.

Los valores que pueden almacenar las variables son de distintos tipos, como:

- **Número (`int`):** Son números sin la parte decimal, Ej: 43, -34
- **Número con punto flotante (`float`):** Ejemplo, 3.1416, -0.032
- **Cadenas de texto (`str`):** Secuencia de caracteres, Ejemplo, 'Hola Mundo'
- **Booleanos:** Almacenan un valor lógico de verdadero (`True`) o falso (`False`). Este tipo de valores los usaremos
  para controlar el flujo de programas
- **`None`:** Es un tipo especial en Pytho que representa ausencia de valor

Estos son los tipos más básicos y estudiaremos más tipos posteriormente.

### Ejemplo de Tipos de datos

**Código 📄:**

```python
# Ejemplo de tipos de datos

# Entero
edad = 28
print(edad)

# Numero con punto flotante
altura = -1.56
print(altura)

# cadena de texto
nombre = "Juan"
print(nombre)

# Tipo boolean
es_estudiante = False
print("Es estudiante?", es_estudiante)

# None, ausencia de valor
direccion = None
print("Dirección:", direccion)
```

**🟢 Ejecutar:**

```console
30
1.56
Juan
Es estudiante? False
Dirección: None
```

### Sistema de Reserva de Hoteles

Crea un Sistema de reserva de hoteles que contenga la siguiente información de una reserva:

- Nombre del cliente
- Días de estancia
- Tarifa diaria
- Indicar si el cuarto tiene vista al mar
- Después mandar a imprimir los valores de cada variable
- Hacer algunos cambias y re-imprimir

El resultado debe ser similar al siguiente:

```console
*** Sistema de Reserva de Hoteles ***
Cliente: Laura Martínez
Días de estancia: 5
Tarifa diaria: 1200.0
Habitación con vista al mar? True
```

**Solución:**

**Código 📄:**

```python
print("*** Sistema de Reserva de Hoteles ***")
# Definimos las variables
nombre_cliente = "Laura Martínez"
dias_estancia = 5
tarifa_diaria = 1200.00
vista_al_mar = True

# Mostrar el detalle de la reserva
print("Cliente:", nombre_cliente)
print("Días de estancia:", dias_estancia)
print("Tarifa diaria:", tarifa_diaria)
print("Habitación con vista al mar?:", vista_al_mar)

# Realizamos algunas modificaciones
dias_estancia = 7
tarifa_diaria = 1000.00
vista_al_mar = False

# Mostrar el detalle de la reserva
print()
print("Cliente:", nombre_cliente)
print("Días de estancia:", dias_estancia)
print("Tarifa diaria:", tarifa_diaria)
print("Habitación con vista al mar?:", vista_al_mar)
```

**🟢 Ejecutar:**

```console
*** Sistema de Reserva de Hoteles ***
Cliente: Laura Martínez
Días de estancia: 5
Tarifa diaria: 1200.0
Habitación con vista al mar?: True

Cliente: Laura Martínez
Días de estancia: 7
Tarifa diaria: 1000.0
Habitación con vista al mar?: False
```

### Sistema Tienda Online

Crear el detalle de un producto de una tienda online.

El detalle del producto debe tener:

- Nombre del producto
- Precio del producto
- Cantidad en el Inventario
- Indicar si está disponible

Hacer algunos cambios y mandar a imprimir nuevamente el nuevo valor de las variables.

El resultado debe ser similar al siguiente:

```console
*** Sistema de Tienda Online ***
Producto: Cámara digital
Precio: $ 399.9
Cantidad inventario: 20
Disponible: True
```

---

**Solución:**

**Código 📄:**

```python
print('*** Sistema de Tienda Online ***')

# Definir las variables de un producto
nombre_producto = 'Cámara digital'
precion_producto = 399.9
cantidad_inventario = 20
disponible_producto = True

# Mostrar información del producto
print('Producto:', nombre_producto)
print('Precio: $', precion_producto)
print('Cantidad en el Inventario:', cantidad_inventario)
print('Disponible:', disponible_producto)

# Hacemos algunos cambio
precion_producto = 399.9
cantidad_inventario = 20
disponible_producto = True

# MOstrar información del producto
print()
print('Producto:', nombre_producto)
print('Precio: $', precion_producto)
print('Cantidad en el Inventario:', cantidad_inventario)
print('Disponible:', disponible_producto)
```

**🟢 Ejecutar:**

```console
*** Sistema de Tienda Online ***
Producto: Cámara digital
Precio: $ 399.9
Cantidad en el Inventario: 20
Disponible: True

Producto: Cámara digital
Precio: $ 399.9
Cantidad en el Inventario: 20
Disponible: True
```

### Constantes

A diferencia de otros lenguajes de programación, en Python no existe un tipo específico para definir una constante de
manera estricta. Sólo es una convención

Python no impide cambiar el valor de una variable, pero podemos seguir la siguiente convención de declarar el nombre de
una variable en mayúsculas y con ello indicamos que el valor de esta variable NO debe modificarse una vez inicializada,
es decir, esta variable se debe tratar como una constante.

```python
# Sintaxis para una constante
NOMBRE_CONSTANTE = valor
```

```python
# Ejemplo de constantes
PI = 3.14159
MENSAJE_ERROR = 'Usuario Inválido'
NOMBRE_USUARIO_VALIDO = 'admin'
```

---

**Código 📄:**

```python
import math

print('*** Constantes en Python ***')

PI = 3.14159
print('El valor de PI es:', PI)

NOMBRE_BASE_DATOS = 'clientes_db'
print('Nombre de la base de datos:', NOMBRE_BASE_DATOS)

# Esto NO se debe hacer, no se debe modificar el valor una constante
NOMBRE_BASE_DATOS = "listado_cliente_db"
print("No cambiar el valor de una constante:", NOMBRE_BASE_DATOS)

# User uan constante del lenguaje Python, aunque en este caso no esta en mayusculas
print("Valor de math.pi", math.pi)
```

**🟢 Ejecutar:**

```console
*** Constantes en Python ***
El valor de PI es: 3.14159
Nombre de la base de datos: clientes_db
No cambiar el valor de una constante: listado_cliente_db 
Valor de math.pi 3.141592653589793
```

## Manejo de Cadenas

Una cadena o string en inglés es un tipo de dato que se utiliza para almacenar una secuencia de caracteres

Las cadenas se deben encerrar entra comillas dobles o comillas simples.

Los caracteres pueden ser letras, números, símbolos o espacios.

```python
# Cadenas en Python
cadena1 = "Hola Mundo"
```

![img_3.png](img_3.png)

### Manejo de Cadenas

**Código 📄:**

```python
# Cadenas en Python
cadena1 = "Hola Mundo"
cadena1 = "Adios"
cadena2 = "Python es Genial"
cadena3 = """Este es un ejemplo
de multiples líneas
en una cadena"""

print(cadena1)
print(cadena2)
print(cadena3)
```

**🟢 Ejecutar:**

```console
Adios
Python es Genial
Este es un ejemplo
de multiples líneas
en una cadena
```

### Detalle de una Cadena

Los caracteres de una cadena están indexados de manera secuencial.

Por lo tanto, podemos acceder cada caracter indicando el índice del caracter que deseamos recuperar

![img_4.png](img_4.png)

**📄 Código :**

```python
# Manejo de índice en una cadena
cadena1 = "Hola Mundo"
print(cadena1)
# Recuperara el primer caracter
primer_caracter = cadena1[0]  # recuperar 'H'
print(primer_caracter)
ultimo_caracter = cadena1[9]  # recuperar 'o'
print(ultimo_caracter)
```

**🟢 Ejecutar:**

```console
Hola Mundo
H
o
```

### Inmutabilidad de una Cadena

Una vez que se crea una cadena, los caractéres dentro de ella no pueden ser modificados

Si deseamos modificar una cadena, entonces tenemos que crear una nueva cadena.

Las cadenas no se pueden modificar, son inmutables:

![img_5.png](img_5.png)

Nuevo valor.

**📄 Código :**

```python
# Inmutabilidad en cadenas
cadena1 = "Hola Mundo"
# cadena1 [0] = 'h' # no podemos modificar los carateres
cadena2 = cadena1
cadena1 = "Adios"
print(cadena1)
print(cadena2)
```

**🟢 Ejecutar:**

```console
Adios
Hola Mundo
```