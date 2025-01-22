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
