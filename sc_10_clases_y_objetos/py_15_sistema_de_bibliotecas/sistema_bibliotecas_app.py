from biblioteca import Biblioteca
from libro import Libro

biblioteca_nacional = Biblioteca("Biblioteca Nacional")
print(f"*** Bienvenido a la {biblioteca_nacional.nombre} ***")

# Definición de libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Comedia")
libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Ficción")
libro4 = Libro("Pedro Páramo", "Juan Rulfo", "Ficción")
libro5 = Libro("Pantaleón y las visitadores", "Mario Vargas Llosa", "Comedia")

# Agrega los libros a la biblioteca
libros_lista = [libro1, libro2, libro3, libro4, libro5]
for libro in libros_lista:
    biblioteca_nacional.agregar_libro(libro)

# Buscar libros por autor
autor = "Gabriel García Márquez"
print(f"\nLibros de: {autor}")
biblioteca_nacional.buscar_libros_por_autor(autor)

# Buscar libros por género
genero = "Ficción"
print(f"\nLibros de {genero}")
biblioteca_nacional.buscar_libros_por_genero(genero)

# Mostrar todos los libros de la biblioteca
biblioteca_nacional.mostrar_todos_los_libros()
