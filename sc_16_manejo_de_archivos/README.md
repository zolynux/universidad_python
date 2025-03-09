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
