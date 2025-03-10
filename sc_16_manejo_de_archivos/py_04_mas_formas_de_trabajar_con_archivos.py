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
