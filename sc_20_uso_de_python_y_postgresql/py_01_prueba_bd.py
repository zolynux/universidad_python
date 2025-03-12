# Importar la biblioteca psycopg2, que permite la conexión y manipulación de bases de datos PostgreSQL desde Python.
import psycopg2

# Establecer una conexión con la base de datos PostgreSQL.
# Se utilizan los siguientes parámetros:
# - user: El nombre de usuario de la base de datos (en este caso, "postgres").
# - password: La contraseña del usuario (en este caso, "admin").
# - host: La dirección del servidor donde está alojada la base de datos (en este caso, "localhost").
# - port: El puerto en el que PostgreSQL está escuchando (por defecto, 5432).
# - database: El nombre de la base de datos a la que se desea conectar (en este caso, "test_db").
conexion = psycopg2.connect(
    user="postgres", password="admin", host="localhost", port="5432", database="test_db"
)

# Crear un cursor. Un cursor es un objeto que permite ejecutar consultas SQL y recuperar resultados.
cursor = conexion.cursor()

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

# Nota: En un programa real, es importante cerrar el cursor y la conexión para liberar recursos.
cursor.close()
conexion.close()
