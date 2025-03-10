# Abrir el archivo "prueba.txt" en modo lectura ("r") con codificación UTF-8.
# "r" significa que solo vamos a leer el archivo, no modificarlo.
# "utf-8" es la codificación de caracteres que se usa para leer el archivo correctamente.
# La función `open()` devuelve un objeto de archivo que se asigna a la variable `archivo`.
# El uso de `with` asegura que el archivo se cierre automáticamente al salir del bloque.
with open("prueba.txt", "r", encoding="utf-8") as archivo:

    # Leer todo el contenido del archivo usando el método `read()`.
    # `archivo.read()` devuelve una cadena con todo el texto del archivo.
    # Luego, este contenido se pasa a la función `print()` para mostrarlo en la consola.
    print(archivo.read())

# Al salir del bloque `with`, el archivo se cierra automáticamente.
# Esto libera los recursos del sistema y asegura que no haya fugas de memoria.
