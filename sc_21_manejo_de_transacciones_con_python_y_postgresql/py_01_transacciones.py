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
    # Desactivar el modo "autocommit" para manejar manualmente las transacciones
    conexion.autocommit = False

    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Definir la sentencia SQL para insertar datos en la tabla "persona"
    sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"

    # Definir los valores que se insertarán en la tabla
    valores = ("Maria", "Esparza", "mesparza@mail.com")

    # Ejecutar la sentencia SQL con los valores proporcionados
    cursor.execute(sentencia, valores)

    # Confirmar la transacción (guardar los cambios en la base de datos)
    conexion.commit()

    # Mensaje de éxito
    print(f"Termina la transacción")

except Exception as e:
    # Si ocurre un error, deshacer la transacción (rollback)
    conexion.rollback()

    # Mostrar el error que ocurrió
    print(f"Ocurrió un error: {e}")

finally:
    # Cerrar la conexión con la base de datos, independientemente de si hubo un error o no
    conexion.close()
