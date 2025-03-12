import psycopg2

# Establecer la conexión con la base de datos
conexion = psycopg2.connect(
    database="test_db", user="postgres", password="admin", host="localhost", port="5432"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = (
                "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s"
            )
            valores = (
                ("Juan", "Perez", "jperez@mail.com", 1),
                ("Ivonne", "Gutierrez", "igutierrez@mail.com", 2),
            )
            cursor.executemany(sentencia, valores)
            registro_actualizado = cursor.rowcount
            print(f"Registro Actualizado: {registro_actualizado}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    # Cerrar la conexión
    conexion.close()
