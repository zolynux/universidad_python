# Funciones

## Funciones en Python

Las funciones son bloque de código para realizar una tarea en particular.

Las funciones se pueden reutilizar en diferentes partes de un programa.

````python
# sintaxis definición de una función
# 1. Definición de la función (verbo o accion)
def nombre_de_la_funcion(parametro1, parametro2):
    # 2. Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado  # Devuelve un valor # 8
````

````python
# Llamada a la función
resultado_final = nombre_de_la_funcion(5, 3)
print(resultado_final)  # Imprime 8
````

### Ventajas de las funciones

- **Modularidad:** Las funciones permiten dividir un programa en partes más pequeñas y manejables. Cada función puede
  ser desarrollada por separado e incluso por distintos programadores, creando al final programas más complejos.
- **Reutilización:** Una vez creada la función, podemos utilizarla tantas veces como necesitemos. Esto evita duplicación
  de código y minimiza los errores.
- **Mantenimiento:** Modificar un programa que usa funciones es más fácil. Podemos localizar los errores más rápidamente
  y corregirlos. Esto reduce el riesgo de efectos no deseados en otras partes del programa.
- **Parametrización:** Las funciones pueden ser diseñadas para aceptar parámetro, lo que hace más flexibles nuestros
  programas.
- **Colaboración:** En proyectos grandes, el uso de módulos (archivos con múltiples funciones) se hace imprescindible,
  al colaborar varios programadores

**📄 Código :**

```python
print("*** Funciones en Python ***")


# Definir una función para mandar a saludar
def saludar():  # Firma del método
    # Cuerpo de la función
    print("Saludos desde una función...")


# Programa principal, llamamos a la función
saludar()
saludar()
saludar()
```

**🟢 Ejecutar:**

```console
*** Funciones en Python ***
Saludos desde una función...
Saludos desde una función...
Saludos desde una función...
```

### Manejo de Parámetros en una función

**📄 Código :**

```python
print("*** Funciones en Python ***")


# Definir una función para mandar a saludar
# Definir un parámetro y puede ser (mensaje:str) es variable estática
def saludar(mensaje):  # Firma del método
    # Cuerpo de la función
    print(f"Mensaje Recibido: {mensaje}")


# Programa principal, llamamos a la función
saludar("Hola a todos")
```

**🟢 Ejecutar:**

```console
*** Funciones en Python ***
Mensaje Recibido: Hola a todos
```

### Función Suma

**📄 Código :**

```python
print("*** Función suma ***")


# Definimos la función
def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma


# Llamar a la función
resultado_funcion = sumar(8, 5)
print(f"Resultado función Suma: {resultado_funcion}")

resultado_funcion = sumar(9, 15)
print(f"Resultado función Suma: {resultado_funcion}")
```

**🟢 Ejecutar:**

```console
*** Función suma ***
Resultado función Suma: 13
Resultado función Suma: 24
```

### Módulos en Funciones

**📄 Código :**

```python
from py_03_sumar import sumar

print("*** Módulo Función Suma ***")

# Llamar a la función
if __name__ == "__main__":
    resultado_funcion = sumar(8, 5)
    print(f"Resultado función Suma: {resultado_funcion}")
```

**🟢 Ejecutar:**

```console
*** Módulo Función Suma ***
Resultado función Suma: 13
```

### Argumentos por nombres en una función

**📄 Código :**

```python
print("*** Función con argumentos por nombre ***")


def imprimir_persona(nombre, apellido="", edad=0):
    print(f"Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}")


# Primero llamamos la función pasando los argumentos de manera posicional
imprimir_persona("Ricardo", "Quintana", 32)
# Llamar la función usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=28, apellido="Rojas", nombre="Carlos")
# Argumentos con valor por default
imprimir_persona(nombre="Carlos")
imprimir_persona(nombre="Carlos", apellido="Rojas")
imprimir_persona(edad=28, nombre="Carlos")
```

**🟢 Ejecutar:**

```console
*** Función con argumentos por nombre ***
Persona: nombre = Ricardo, apellido = Quintana, edad = 32
Persona: nombre = Carlos, apellido = Rojas, edad = 28
Persona: nombre = Carlos, apellido = , edad = 0
Persona: nombre = Carlos, apellido = Rojas, edad = 0
Persona: nombre = Carlos, apellido = , edad = 28
```

### Regresar una tupla de valores desde una función

**📄 Código :**

```python
print("*** Regresar una tupla de valores desde una función ***")


# Definición de la función
def persona_mayusculas(nombre, apellido, edad):
    print(f"Esta función regresa varios valores (tuplas)")
    return nombre.upper(), apellido.upper(), edad


# Programa Principal
nombre, apellido, edad = persona_mayusculas("Sandra", "Jimenez", 42)
print(f"Resultado Persona: Nombre = {nombre}, apellido = {apellido}, edad = {edad}")
```

**🟢 Ejecutar:**

```console
*** Regresar una tupla de valores desde una función ***
Esta función regresa varios valores (tuplas)
Resultado Persona: Nombre = SANDRA, apellido = JIMENEZ, edad = 42
```

### Coordenadas en una función de Tuplas

**📄 Código :**

```python
print("*** Obtener coordenadas ***")


def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z


# Llama la función
resultado = obtener_coordenadas()
print(resultado)

# Unpacking de la tupla
x1, y1, z1 = resultado
print(f"Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}")
```

**🟢 Ejecutar:**

```console
*** Obtener coordenadas ***
(10, 20, 30)
Coordenada x = 10, Coordenada y = 20, Coordenada z = 30
```

### Alcance de Variables

Las variables pueden tener un alcance global o local dependiendo de dónde y cómo se declaren

Las variables globales son aquellos que están disponibles a lo largo de todo el programa

Mientras que las variables locales sólo están disponibles dentro del bloque de código o la función donde fueron
declaradas.

**📄 Código :**

```python
print("*** Alcance de Variables ***")

# Variable global
contador_global: int = 0


def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0
    # usar la variable global
    global contador_global
    # Incrementamos la variable global
    contador_global += 1
    # Incrementamos la variable local
    contador_local += 1
    # Imprimimos ambos contadores
    print("Contador local:", contador_local)
    print("Contador global:", contador_global, "\n")


#  Llamamos varias veces la función
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print("Valor variable global:", contador_global)
```

**🟢 Ejecutar:**

```console
*** Alcance de Variables ***
Contador local: 1
Contador global: 1 

Contador local: 1
Contador global: 2 

Contador local: 1
Contador global: 3 

Valor variable global: 3
```

### Argumentos variables *args

En Python, los argumentos variables permiten que una función acepte un número arbitrario de elementos. Hay dos tipos
principales

1. **Argumentos posicionales variables `*args`:** Permite pasar múltiples argumentos posicionales a una función,
   recibiéndolos como una tupla dentro de la función.
2. **Argumentos con Palabra Clave `**kwargs`:** Recibe los argumentos en forma de diccionario (llave - valor o key -
   value).

**📄 Código :**

```python
print("*** Argumentos Variables ***")


def superheroe_superpoderes(superheroe, nombre, *args):
    print(f"Superheroe: {superheroe} - {nombre} - {args}")
    for superporder in args:
        print(f"\tSuperpoder: {superporder}")


# Llama la función
superheroe_superpoderes("Spiderman", "Peter Parker", "Instinto Arácnido", "Teleraña")
superheroe_superpoderes("Ironman", "Tony Stark", "Armadura", "Playboy", "Millonario")

# Es opcional enviar argumentos variables
superheroe_superpoderes("Mi vecino", "Juan Perez")

```

**🟢 Ejecutar:**

```console
*** Argumentos Variables ***
Superheroe: Spiderman - Peter Parker - ('Instinto Arácnido', 'Teleraña')
	Superpoder: Instinto Arácnido
	Superpoder: Teleraña
Superheroe: Ironman - Tony Stark - ('Armadura', 'Playboy', 'Millonario')
	Superpoder: Armadura
	Superpoder: Playboy
	Superpoder: Millonario
Superheroe: Mi vecino - Juan Perez - ()
```

### Argumentos variables **kwargs

**📄 Código :**

```python
# *args -> argumentos = tuplas
# **kwargs -> keyword argumentos (key, value) como un dict

print("*** Argumentos Variables en forma de dict ***")


def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f"Superheroe: {nombre} - {args} - Más info: {kwargs}")


# Llama la función
superheroe_superpoderes("Spiderman", "Instinto Arácnido", edad=17, empresa="Marvel")
superheroe_superpoderes("Ironman", "Armadura", "Playboy", edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes("Mi vecino", personalidad="Buena onda!")

```

**🟢 Ejecutar:**

```console
*** Argumentos Variables en forma de dict ***
Superheroe: Spiderman - ('Instinto Arácnido',) - Más info: {'edad': 17, 'empresa': 'Marvel'}
Superheroe: Ironman - ('Armadura', 'Playboy') - Más info: {'edad': 45}
Superheroe: Mi vecino - () - Más info: {'personalidad': 'Buena onda!'}
```
