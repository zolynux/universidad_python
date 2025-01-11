from sc_03_manejo_de_cadenas.py_08_largo_cadena import cadena

# Universidad Python - Cero a Experto (+86 horas) 🐍

## Tabla de Contenido

- [Universidad Python - Cero a Experto (+86 horas) 🐍](#universidad-python---cero-a-experto-86-horas-)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Introducción a Python](#introducción-a-python)
    - [Instalación de Python](#instalación-de-python)
    - [Hola Mundo con Python](#hola-mundo-con-python)
    - [Ejercicio Preséntate](#ejercicio-preséntate)
  - [Variables](#variables)
    - [Sintaxis para definir una variable](#sintaxis-para-definir-una-variable)
      - [Variables y la Memoria RAN](#variables-y-la-memoria-ran)
    - [Variables y la Memoria RAM](#variables-y-la-memoria-ram)
      - [Variables y Memoria Simplificado](#variables-y-memoria-simplificado)
    - [Ejemplo de Variables](#ejemplo-de-variables)
    - [Modificar Variables](#modificar-variables)
    - [Modificar variables](#modificar-variables-1)
    - [Reglas y buenas prácticas en nombres de variables](#reglas-y-buenas-prácticas-en-nombres-de-variables)
      - [Convenciones y buenas prácticas](#convenciones-y-buenas-prácticas)
    - [Ejemplo de regla de nombre de variables](#ejemplo-de-regla-de-nombre-de-variables)
    - [Tipos de datos](#tipos-de-datos)
    - [Ejemplo de Tipos de datos](#ejemplo-de-tipos-de-datos)
    - [Sistema de Reserva de Hoteles](#sistema-de-reserva-de-hoteles)
    - [Sistema Tienda Online](#sistema-tienda-online)
    - [Constantes](#constantes)
  - [Manejo de Cadenas](#manejo-de-cadenas)
    - [Detalle de una Cadena](#detalle-de-una-cadena)
    - [Inmutabilidad de una Cadena](#inmutabilidad-de-una-cadena)
    - [Caractéres Especiales](#caractéres-especiales)
    - [Concatenación de Cadenas](#concatenación-de-cadenas)
    - [Formateo de Cadenas](#formateo-de-cadenas)
    - [Métodos de cadenas](#métodos-de-cadenas)
    - [Largo de una cadena](#largo-de-una-cadena)
    - [Subcadenas](#subcadenas)
    - [Búsqueda de subcadenas](#búsqueda-de-subcadenas)
    - [Reemplazar subcadena](#reemplazar-subcadena)
    - [Separar en Subcadenas](#separar-en-subcadenas)
    - [Multiplicación de cadenas](#multiplicación-de-cadenas)
    - [Generador de Email](#generador-de-email)
  - [Entrada de Datos](#entrada-de-datos)
    - [Ejemplo de Conversión de Tipos de Datos](#ejemplo-de-conversión-de-tipos-de-datos)
    - [Entrada de Datos por Conosla](#entrada-de-datos-por-conosla)
      - [Características de la función `input`](#características-de-la-función-input)
    - [Sistema de Empleados](#sistema-de-empleados)
    - [Receta de Cocina](#receta-de-cocina)
    - [Generar valores aleatorios](#generar-valores-aleatorios)
    - [Reto Generador de ID Único](#reto-generador-de-id-único)

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
| ---- | ------------------ | ---- | ------------------ |
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

### Caractéres Especiales

Las cadenas pueden incluir caractéres especiales

Estos caracteres se introducen usando el caracter de diagonal invertida (`\`). Ejemplo:

- **Nueva línea: `\n`** Inserta un salto de línea
- **Tabulación: `\t`** Inserta un tabulador horizontal, útil para alinear texto.
- **Comilla Simple: `\'`** Permite incluir comillas Simples en una cadena delimitada por comillas simples.
- **Comilla Doble: `\"`** Permite incluir comillas Dobles en una cadena delimitada por comillas simples.
- **Barra invertida:  `\\`** Permite incluir una barra invertida en la cadena

Existen más caracteres especiales, pero esto son los esenciales.

**📄 Código :**

```python
# Caracteres Especiales
print("Hola \nMundo")  # \n salto de linea
print("\t\tPython \t\tes genial")  # \t agrega un tabulador
print("Juan ' \"Perez")
print('Karla " Gomez')
print("Caracter \\ diagonal invertida")
```

**🟢 Ejecutar:**

```console
Hola 
Mundo
		Python 		es genial
Juan ' "Perez
Karla " Gomez
Caracter \ diagonal invertida
```

### Concatenación de Cadenas

La concatenación de cadenas es una operación que permite combinar dos o más cadenas para formar una nueva cadena.

En python existen varias formas, vamos a ver varias.

- **Uso del operador +:** El operador `+` es el más directo para concatenas. Simplemente tenemos que poner el operador
  `+` entre las cadenas que deseamos unir.

**Ejemplo:**

```python
concatenacion = "Hola" + "Mundo"
```

- **Uso de la función `join`:** La función `join` nos permite unir tantas cadenas como necesitemos. Solo necesitamos
  pasar cada cadena a concatenar separadas por coma y entre paréntesis.

**Ejemplo:**

```python
"".join(["cadena1", "cadena2", "cadena3"])
```

--

**📄 Código :**

```python
# Concatenación de Cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = cadena1 + " " + cadena2

print(concatenacion)

# Utilizando el metodo join

concatenacion = "".join([cadena1, " ", cadena2])
print(concatenacion)
```

**🟢 Ejecutar:**

```console
Hola Mundo
Hola Mundo
```

### Formateo de Cadenas

Python ofrece varias maneras de formatear cadenas, que incluyen la capacidad de concatenar texto, variables e incluso
dar indicar el número de decimales a utilizar en el formato.

- **f-string (Python 3.6+)**: Esta es la opción más recomendan, por ser la más sencilla, rápida y legible.

```python
resultado = f'hola {variable}'
```

- **Método format** Es muy versátil y poderoso permite construir cadenas muy complejas.

```python
resultado = 'Hola {}'.format(variable)
```

### Métodos de cadenas

Las cadenas en Python vienen con una serie de métodos útiles que facilitan su manipulación. Por ejemplo:

- `upper()` -> Cambiar las letras a mayúsculas.
- `lower()` -> Cambiar las letras a minúsculas.
- `strip()` -> Elimina espacios en blanco al inicio y al final de la cadena

**📄 Código :**

```python
# Método de cadenas

cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}')
mayusculas = cadena1.upper()  # Convertir a mayúsculas
print(f'Cadena en mayúsculas: {mayusculas}')
print(f'Cadena en minúsculas: {cadena1.lower()}')  # Convertir a minúsculas
cadena2 = ' Juan Perez '
print(f'Cadena con espacios: {cadena2}')
print(f'Cadena sin espacios: {cadena2.strip()}')  # Eliminar espacio al inicio y al final
```

**🟢 Ejecutar:**

```console
Cadena original: Hola Mundo
Cadena en mayúsculas: HOLA MUNDO
Cadena en minúsculas: hola mundo
Cadena con espacios:  Juan Perez 
Cadena sin espacios: Juan Perez
```

### Largo de una cadena

**Obtener el largo de una cadena:**

Para obtener la longitud de una cadena, utilizamos la función incorporada `len()`

La función `len` funciona con varios tipos de datos incluyendo cadenas, listas, etc.

Cuando se calcula el largo de una cadena se toman en cuenta todos los caracteres de una cena, incluyendo espacios en
blanco, caracteres especiales, etc.

````python
cadena1 = 'Hola, Mundo!'
longitud = len(cadena1)  # -> devuelve largo de 12
````

**📄 Código :**

```python
# Largo de una cadena
cadena = "Hola, mundo!"
largo_cadena = len(cadena)
print(f"Cadena original: {cadena}")
print(f"Largo de la cadena: {largo_cadena}")
```

**🟢 Ejecutar:**

```console
Cadena original: Hola, mundo!
Largo de la cadena: 12
```

### Subcadenas

Una subcadena es una parte de una cadena principal, y hay varias maneras de extraer subcadenas en Python

Podemos extraer subcadenas, buscarlas, reemplazarlas, entre otras operaciones.

- **Extracción cadenas (Slicing):** El slicing o segmentación permite indicar el índice de inicio y el índice final (sin
  incluir este último caracter)

```python
subcadena = cadena[inicio:fin]
```

**📄 Código :**

```python
# Manejo de subcadenas
cadena = "Hola, Mundo!"
# Obtenemos la subcadena de hola[inicio:fin (sin incluirlo)]
subcadena_hola = cadena[0:4]
print(f"Subcadena de hola: {subcadena_hola}")
# Obtene la subcadena de mundo
subcadena_mundo = cadena[6:11]
print(f"Subcadena de mundo: {subcadena_mundo}")
```

**🟢 Ejecutar:**

```console
Subcadena de hola: Hola
Subcadena de mundo: Mundo
```

### Búsqueda de subcadenas

- **Buscar subcadenas (`find`):** El método `find()` devuelve el índice de la primera aparición de la subcadena. Si no
  encuentra la subcadena, devuelve -1

```python
cadena = 'Hola Mundo'
posicion = cadena.find("Mundo")
print(posicion)  # Imprime 5
```

**📄 Código :**

```python
# Buscar subcadenas
cadena = "Hola, mundo"
indice = cadena.find("mundo")
print(f"Indice de la subcadena mundo: {indice}")
# Obtener el indicie de la subcadena de Hola
indice = cadena.find("Hola")
print(f"Indice la subcadena de Hola: {indice}")
```

**🟢 Ejecutar:**

```console
Indice de la subcadena mundo: 6
Indice la subcadena de Hola: 0
```

### Reemplazar subcadena

- **Reemplazar subcadena (`replace`)** El método `replace()` reemplaza una subcadena por otra dentro de una cadena principaal

```python
cadena = 'Hola mundo'
nueva_cadena = cadena.replace('mundo', 'a todos')
print(nueva_cadena) # 'Hola a todos'
```

**📄 Código :**

```python
# Reemplazar subcadenas
cadena = 'Hola, mundo!'
print(f'Cadena original: {cadena}')
nueva_cadena = cadena.replace('mundo', 'a todos')
print(f'Nueva cadena reemplazada:  {nueva_cadena}')
# Sustituir hola por adios
nueva_cadena = cadena.replace('Hola', 'Adiós')
print(f'Nueva cadena reemplazada: {nueva_cadena}')
```

**🟢 Ejecutar:**

```console
Cadena original: Hola, mundo!
Nueva cadena reemplazada:  Hola, a todos!
Nueva cadena reemplazada: Adiós, mundo!
```

### Separar en Subcadenas

- **Extraer subcadenas por separadores (`split`):** La función `split()` permite dividir una cadena en una lista de subcadenas basadas en un caracter separador.

**Ejemplo:**

```python
datos = 'Juan, 30, Colombia'
lista = datos.split(',')
print(lista) # ['Juan', '30', 'Colombia']
```

**📄 Código :**

```python
# Separar cadenas (split)
datos = "Hola Mundo"
lista = datos.split()  # Por defualt separa cada elemento por espacios en blanco
print(lista)

datos = "Juan,30,Colombia"
lista = datos.split(",")
print(lista)
```

**🟢 Ejecutar:**

```console
['Hola', 'Mundo']
['Juan', '30', 'Colombia']
```

### Multiplicación de cadenas

**📄 Código :**

```python
print("*** Multiplicación de Cadenas ***")

texto = "Hola"
veces = 4

resultado = texto * veces
print(resultado)
```

**🟢 Ejecutar:**

```console
*** Multiplicación de Cadenas ***
HolaHolaHolaHola
```

### Generador de Email

Crea un programa para generar un email a partir de los siguientes datos:

- **Nombre:** Ubaldo Acosta Soto
- **Empresa:** Global Mentoring
- **Dominio:** com.mx

Resutlado Final:

**Email:** `ubaldo.acosta.soto@globalmentoring.com.mx`

Este es el resultado del programa:

```console
*** Generador de Email ***
Nombre Usuario: Ubaldo Acosta Soto
Nombre Usuario normalizado: ubaldo.acosta.soto

Nombre Empresa: Global Mentoring
Extensión del dominio: com.mx
Dominio de email normalizado: @globalmentoringcom.mx  

Email final generado: ubaldo.acosta.soto@globalmentoringcom.mx
```

**📄 Código :**

```python
# Generador de Email
print("*** Generador de Email ***")

nombre_completo = "Ubaldo Acosta Soto"
print(f"Nombre Usuario: {nombre_completo}")
nombre_normalizado = nombre_completo.strip().lower().replace(" ", ".")
print(f"Nombre Usuario normalizado: {nombre_normalizado}")
print()
empresa = "Global Mentoring"
print(f"Nombre Empresa: {empresa}")
empresa_normalizado = empresa.strip().lower().replace(" ", "")
dominio = "com.mx"
print(f"Extensión del dominio: {dominio}")
dominio_email = "".join(["@", empresa_normalizado, dominio])
print(f"Dominio de email normalizado: {dominio_email}")
print()
print(f"Email final generado: {nombre_normalizado + dominio_email}")
```

**🟢 Ejecutar:**

```console
*** Generador de Email ***
Nombre Usuario: Ubaldo Acosta Soto
Nombre Usuario normalizado: ubaldo.acosta.soto

Nombre Empresa: Global Mentoring
Extensión del dominio: com.mx
Dominio de email normalizado: @globalmentoringcom.mx  

Email final generado: ubaldo.acosta.soto@globalmentoringcom.mx
```

## Entrada de Datos

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

### Ejemplo de Conversión de Tipos de Datos

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

### Entrada de Datos por Conosla

En Python, la entrada de datos se realiza usando la función `input()`

Esta función puasa la ejecución del programa y espera a que el usuario introduzca algún texto desde el teclado.

Una vez que el usuario presiona Enter, el texto introducido se devuelve como una cadena (str)

#### Características de la función `input`

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

### Sistema de Empleados

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

### Receta de Cocina

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

### Generar valores aleatorios

La función `randint()`, que es parte de módulo `random`, nos permite generar números aleatorios

`randint(a, b)` devuelve un número aleatorio entre a y b, incluyendo estos valores.

Es necesario importar en primer línea el módulo `random` antes de usar la función `randint()```

Para importar un módulo, usamos la sintaxis `import random`


**📄 Código :**

```python
### Valores aleatorios con la función randint

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

### Reto Generador de ID Único

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
