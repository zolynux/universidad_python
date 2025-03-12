import psycopg2

# Establecer la conexión con la base de datos
conexion = psycopg2.connect(
    database="test_db", user="postgres", password="admin", host="localhost", port="5432"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # Definir la consulta SQL
            sentencia = (
                "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
            )
            # Definir los valores
            valores = (
                ("Marcos", "Cantu", "mcantu@mail.com"),
                ("Angel", "Quintana", "aquintana@mail.com"),
                ("Maria", "Gonzalez", "mgonzalez@mail.com"),
            )
            # Ejercutar la consulta
            cursor.executemany(sentencia, valores)
            # conexion.commit() # Es importante confirmar los cambios con conexion.commit() (a menos que uses un bloque with).
            # Obtener el número de registros insertados
            registro_insertado = cursor.rowcount
            print(f"Registro Insertado: {registro_insertado}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    # Cerrar la conexión
    conexion.close()
