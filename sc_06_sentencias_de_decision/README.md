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
