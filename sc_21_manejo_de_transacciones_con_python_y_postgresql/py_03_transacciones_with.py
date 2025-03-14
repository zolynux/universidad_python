# Importar el módulo psycopg2 para conectarse a PostgreSQL
import psycopg2 as bd

# Establecer la conexión con la base de datos
# Se usan los parámetros de conexión: nombre de la base de datos, usuario, contraseña, host y puerto
conexion = bd.connect(
    database="test_db",  # Nombre de la base de datos
    user="postgres",  # Usuario de PostgreSQL
    password="admin",  # Contraseña del usuario
    host="localhost",  # Host donde está la base de datos
    port="5432",  # Puerto de PostgreSQL (por defecto es 5432)
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # Definir la sentencia SQL para insertar datos en la tabla "persona"
            sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
            # Definir los valores que se insertarán en la tabla
            valores = ("Alex", "Rojas", "arojas@mail.com")
            # Ejecutar la sentencia SQL con los valores proporcionados
            cursor.execute(sentencia, valores)

            sentencia = (
                "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id = %s"
            )
            valores = ("Juan", "Perez", "jperez@mail.com", 1)
            # Ejecutar la sentencia SQL con los valores proporcionados
            cursor.execute(sentencia, valores)

            # Mensaje de éxito
except Exception as e:
    # Si ocurre un error, deshacer la transacción (rollback)
    conexion.rollback()
    # Mostrar el error que ocurrió
    print(f"Ocurrió un error: {e}")
finally:
    # Cerrar la conexión con la base de datos, independientemente de si hubo un error o no
    conexion.close()
print(f"Termina la transacción, se hizo commit entre insertado e actualizado")
