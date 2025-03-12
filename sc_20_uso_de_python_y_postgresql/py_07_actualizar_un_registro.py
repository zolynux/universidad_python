import psycopg2

# Establecer la conexión con la base de datos
conexion = psycopg2.connect(
    database="test_db", user="postgres", password="admin", host="localhost", port="5432"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # Definir la consulta SQL para actualizar un registro en la tabla "persona".
            # La consulta actualiza los campos "nombre", "apellido" y "email" donde el "id" coincide con un valor específico.
            # Los valores a actualizar se pasan como parámetros (%s) para evitar inyecciones SQL.
            sentencia = (
                "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id=%s"
            )

            # Definir los valores que se usarán en la consulta SQL.
            # Estos valores reemplazarán los marcadores de posición (%s) en la consulta.
            # En este caso, se actualiza el nombre a "Juan Carlos", el apellido a "Juarez", el email a "jcjuarez@mail.com" para el registro con id = 1.
            valores = ("Juan Carlos", "Juarez", "jcjuarez@mail.com", 1)

            # Ejecutar la consulta SQL con los valores proporcionados.
            # Esto actualiza el registro en la base de datos.
            cursor.execute(sentencia, valores)

            # Obtener el número de registros actualizados.
            # `cursor.rowcount` devuelve la cantidad de filas afectadas por la consulta.
            registro_actualizado = cursor.rowcount

            # Imprimir el número de registros actualizados.
            # Esto muestra en la consola cuántos registros se modificaron.
            print(f"Registro Actualizado: {registro_actualizado}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    # Cerrar la conexión
    conexion.close()
