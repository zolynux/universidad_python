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
            # En este caso, la consulta selecciona todos los registros de la tabla "persona".
            sentencia = "SELECT * FROM persona"

            # Ejecutar la consulta SQL definida en la variable `sentencia`.
            cursor.execute(sentencia)

            # Recuperar todos los registros obtenidos por la consulta SQL.
            # `fetchall()` devuelve una lista de tuplas, donde cada tupla representa una fila de la tabla.
            registros = cursor.fetchall()

            # Imprimir los registros obtenidos.
            # Esto mostrará en la consola todas las filas de la tabla "persona".
            print(registros)

# Capturar cualquier excepción que ocurra durante la ejecución del código.
except Exception as e:
    # Imprimir un mensaje de error que incluye la descripción de la excepción.
    print(f"Ocurrió un error: {e}")

# Bloque finally: Este bloque se ejecuta siempre, haya o no ocurrido una excepción.
finally:
    # Cerrar la conexión con la base de datos para liberar recursos.
    conexion.close()
