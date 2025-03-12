import psycopg2

# Establecer la conexión con la base de datos
conexion = psycopg2.connect(
    database="test_db", user="postgres", password="admin", host="localhost", port="5432"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM persona WHERE id IN %s"
            entrada = input("Proporciona los id a eliminar (separados por comas): ")
            valores = (tuple(entrada.split(",")),)
            cursor.execute(sentencia, valores)
            registro_eliminado = cursor.rowcount
            print(f"Registros Eliminados: {registro_eliminado}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    # Cerrar la conexión
    conexion.close()
