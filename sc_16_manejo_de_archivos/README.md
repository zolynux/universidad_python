## Manejo de Archivos en Python

El **manejo de archivos en Python** se refiere a las operaciones para leer, escribir, crear o modificar archivos (como textos, CSV, JSON, etc.) desde un programa. Python ofrece funciones y métodos integrados para interactuar con archivos de manera eficiente, permitiendo almacenar o recuperar datos de forma persistente.

---

#### **Pasos básicos para manejar archivos**
1. **Abrir el archivo**: Usar la función `open()` para acceder al archivo en un modo específico (lectura, escritura, etc.).
2. **Operaciones**: Leer o escribir contenido.
3. **Cerrar el archivo**: Cerrar el archivo con `close()` para liberar recursos (o usar el contexto `with`).

---

#### **Modos de apertura de archivos**
Al abrir un archivo con `open()`, se especifica el modo de acceso:

| Modo | Descripción                                                                 |
|------|-----------------------------------------------------------------------------|
| `r`  | Lectura (default). Error si el archivo no existe.                           |
| `w`  | Escritura. Crea el archivo si no existe, o **sobrescribe** el contenido.    |
| `a`  | Append (agregar). Escribe al final del archivo sin borrar lo existente.     |
| `r+` | Lectura y escritura.                                                        |
| `b`  | Modo binario (ejemplo: `rb` para leer un archivo binario como una imagen).  |

---

#### **Ejemplos de manejo de archivos**

##### 1. **Leer un archivo de texto**:
```python
# Usando 'with' para cerrar automáticamente el archivo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()  # Lee todo el contenido
    print(contenido)

# Leer línea por línea
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina saltos de línea
```

##### 2. **Escribir en un archivo**:
```python
# Sobrescribe el archivo (si existe)
with open("saludo.txt", "w") as archivo:
    archivo.write("¡Hola, mundo!\n")
    archivo.write("Segunda línea.")

# Agregar contenido (modo 'a')
with open("saludo.txt", "a") as archivo:
    archivo.write("\nTercera línea (append).")
```

##### 3. **Leer todas las líneas como una lista**:
```python
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)  # Ejemplo: ['Línea 1\n', 'Línea 2\n']
```

---

#### **Manejo de excepciones en archivos**
Es importante capturar errores como archivos no encontrados o permisos denegados:
```python
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("Error: El archivo no existe.")
except PermissionError:
    print("Error: No tienes permisos para leer el archivo.")
```

---

#### **Métodos útiles de archivos**
| Método            | Descripción                                    |
|--------------------|------------------------------------------------|
| `read()`           | Lee todo el contenido.                        |
| `readline()`       | Lee una línea del archivo.                    |
| `readlines()`      | Retorna una lista con todas las líneas.       |
| `write(texto)`     | Escribe texto en el archivo.                  |
| `writelines(lista)`| Escribe una lista de cadenas en el archivo.   |
| `seek(posición)`   | Mueve el cursor a una posición específica.    |

---

#### **Mejores prácticas**
1. **Usar `with`**: Garantiza que el archivo se cierre automáticamente, incluso si hay errores.
2. **Evitar modos inseguros**: Usar `w` con cuidado, ya que borra el contenido existente.
3. **Manejar excepciones**: Capturar errores comunes como `FileNotFoundError`.
4. **Trabajar con rutas**: Usar el módulo `os` o `pathlib` para rutas multiplataforma.

---

#### **Ejemplo avanzado: Leer y procesar un CSV**
```python
import csv

with open("datos.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(f"Fila: {fila}")
```

---

#### **Resumen**
El manejo de archivos en Python permite:
- Leer datos desde un archivo para procesarlos en tu programa.
- Escribir resultados o información en un archivo para almacenamiento permanente.
- Trabajar con diferentes formatos (texto, CSV, JSON, etc.).
- Gestionar errores y recursos de manera eficiente con `with` y excepciones.

### Manejo de Archivos


**📄 Código :**

```python
try:
    archivo = open("prueba.txt", "w")
    archivo.write("Agregamos informacion al archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:
    archivo.close()

```

**🟢 Ejecutar:**

**prueba.txt:**

```console
Agregamos informacion al archivoAdios
```

### Especificar el Juego de Caracteres de un Archivo de Texto

**📄 Código :**

```python
try:
    archivo = open("prueba.txt", "w", encoding="utf-8")
    archivo.write("Agregamos información al archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:
    archivo.close()
    print("Fin del archivo")
    # archivo.write('nueva info')

```

**🟢 Ejecutar:**

```console
Agregamos información al archivo
Adios
```

### Lectura de Archivos


**📄 Código :**

```python
# Intentar abrir un archivo con ruta absoluta (comentado)
# archivo = open("C:\\Cursos\\Python\\prueba.txt", "r", encoding="utf-8")

# Abrir el archivo 'prueba.txt' en modo lectura ('r') con codificación UTF-8
archivo = open("prueba.txt", "r", encoding="utf-8")

# Leer y mostrar TODO el contenido del archivo (comentado para no ejecutarse)
# print(archivo.read())

# Leer los primeros 5 caracteres del archivo (comentado)
# print(archivo.read(5))  # Ejemplo: si el texto es "Hola mundo", mostraría "Hola "

# Leer los siguientes 3 caracteres (comentado)
# print(archivo.read(3))  # Continuando del ejemplo anterior, mostraría "mun"

# Leer la PRIMERA línea completa del archivo (hasta encontrar un salto de línea \n)
print(archivo.readline())  # Ejemplo: Línea 1: "Hola Python\n"

# Leer la SEGUNDA línea completa del archivo (continúa desde donde quedó el cursor)
print(archivo.readline())  # Ejemplo: Línea 2: "Manejo de archivos\n"

# IMPORTANTE: Cerrar el archivo para liberar recursos (no incluido en el código original)
archivo.close()

```

**🟢 Ejecutar:**

```console
Agregamos información al archivo

Adios
```

### Más formas de trabajar con Archivos

**📄 Código :**

```python
# Abrir el archivo "prueba.txt" en modo lectura ("r") con codificación UTF-8.
# "r" significa que solo vamos a leer el archivo, no modificarlo.
# "utf-8" es la codificación de caracteres que se usa para leer el archivo correctamente.
archivo = open("prueba.txt", "r", encoding="utf-8")

# Opción 1: Iterar el archivo línea por línea.
# Esto lee el archivo línea a línea y la imprime.
# Descomenta el siguiente bloque para usarlo:
# for linea in archivo:
#     print(linea)  # Imprime cada línea del archivo.

# Opción 2: Leer todas las líneas del archivo y devolverlas como una lista.
# Descomenta la siguiente línea para usarlo:
# print(archivo.readlines())  # Imprime una lista con todas las líneas del archivo.

# Opción 3: Acceder a una línea específica de la lista de líneas.
# Descomenta la siguiente línea para usarlo:
# print(archivo.readlines()[0])  # Imprime la primera línea del archivo.

# Abrir un nuevo archivo llamado "copia.txt" en modo "a" (append).
# "a" significa que vamos a agregar información al final del archivo sin borrar su contenido.
# Si el archivo no existe, se crea automáticamente.
# "utf-8" es la codificación de caracteres que se usa para escribir el archivo correctamente.
archivo2 = open("copia.txt", "a", encoding="utf-8")

# Leer todo el contenido del archivo original ("prueba.txt") y escribirlo en el archivo "copia.txt".
# archivo.read() lee todo el contenido del archivo original.
# archivo2.write() escribe ese contenido en el archivo "copia.txt".
archivo2.write(archivo.read())

# Cerrar ambos archivos para liberar recursos del sistema.
# Es importante cerrar los archivos después de usarlos.
archivo.close()
archivo2.close()

# Mensaje final que indica que el proceso de leer y copiar archivos ha terminado.
print("Se ha terminado el proceso de leer y copiar archivos")

```

**🟢 Ejecutar:**

```console
Se ha terminado el proceso de leer y copiar archivos
```
