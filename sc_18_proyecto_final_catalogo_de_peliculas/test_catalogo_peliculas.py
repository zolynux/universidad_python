from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print("Opciones:")
        print("1. Agregar Película")
        print("2. Listar Película")
        print("3. Eliminar Película")
        print("4. Salir")
        opcion = int(input("Escribe tu opción (1-4): "))

        match opcion:
            case 1:
                nombre_pelicula = input("Proporciona el nombre de la película: ")
                pelicula = Pelicula(nombre_pelicula)
                cp.agregar_pelicula(pelicula)
                break
            case 2:
                cp.listar_peliculas()
                break
            case 3:
                cp.eliminar_pelicula()
                break

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        opcion = None


else:
    print("Saliendo...")
