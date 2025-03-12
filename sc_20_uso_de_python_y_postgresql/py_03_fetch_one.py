# Importar la biblioteca psycopg2, que permite la conexión y manipulación de bases de datos PostgreSQL desde Python.
import psycopg2

# Establecer una conexión con la base de datos PostgreSQL.
# Se utilizan los siguientes parámetros:
# - database: El nombre de la base de datos a la que se desea conectar (en este caso, "test_db").
# - user: El nombre de usuario de la base de datos (en este caso, "postgres").
# - password: La contraseña del usuario (en este caso, "admin").
# - host: La dirección del servidor donde está alojada la base de datos (en este caso, "localhost").
# - port: El puerto en el que PostgreSQL está escuchando (por defecto, 5432).
conexion = psycopg2.connect(
    database="test_db", user="postgres", password="admin", host="localhost", port="5432"
)

# Iniciar un bloque try para manejar posibles excepciones (errores) que puedan ocurrir durante la ejecución del código.
try:
    # Usar el bloque 'with' para gestionar la conexión.
    # Esto asegura que la conexión se cierre automáticamente al salir del bloque, incluso si ocurre una excepción.
    with conexion:
        # Usar otro bloque 'with' para gestionar el cursor.
        # Esto asegura que el cursor se cierre automáticamente al salir del bloque.
        with conexion.cursor() as cursor:
            # Definir la consulta SQL que se va a ejecutar.
            # En este caso, la consulta selecciona todos los registros de la tabla "persona" donde el campo "id" coincide con un valor proporcionado.
            # El valor se pasa como parámetro para evitar inyecciones SQL.
            sentencia = "SELECT * FROM persona WHERE id = %s"

            # Solicitar al usuario que introduzca el valor de "id_persona".
            # Este valor se usará para buscar un registro específico en la tabla.
            id_persona = input("Introduce el valor de id persona: ")

            # Ejecutar la consulta SQL definida en la variable `sentencia`.
            # El valor de `id_persona` se pasa como una tupla (por eso tiene una coma al final).
            cursor.execute(sentencia, (id_persona,))

            # Recuperar un solo registro obtenido por la consulta SQL.
            # `fetchone()` devuelve una tupla que representa la primera fila que coincide con la consulta.
            # Si no hay coincidencias, devuelve `None`.
            registros = cursor.fetchone()

            # Imprimir el registro obtenido.
            # Esto mostrará en la consola la fila de la tabla "persona" que coincide con el "id" proporcionado.
            print(registros)

# Capturar cualquier excepción que ocurra durante la ejecución del código.
except Exception as e:
    # Imprimir un mensaje de error que incluye la descripción de la excepción.
    print(f"Ocurrió un error: {e}")

# Bloque finally: Este bloque se ejecuta siempre, haya o no ocurrido una excepción.
finally:
    # Cerrar la conexión con la base de datos para liberar recursos.
    conexion.close()
