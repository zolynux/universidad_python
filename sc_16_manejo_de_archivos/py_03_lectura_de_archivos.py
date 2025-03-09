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
