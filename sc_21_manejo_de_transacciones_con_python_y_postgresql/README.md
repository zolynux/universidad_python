## Manejo de transacciones con Python y Postgres

El **manejo de transacciones** en Python y PostgreSQL se refiere a la capacidad de ejecutar múltiples operaciones en la base de datos como una sola unidad de trabajo. Las transacciones garantizan que todas las operaciones se completen correctamente (y se confirmen) o que ninguna se aplique (y se deshagan), manteniendo así la integridad de los datos.

---

#### **¿Qué es una transacción?**
Una transacción es una secuencia de operaciones (como inserciones, actualizaciones o eliminaciones) que se ejecutan como una sola unidad. Las transacciones siguen el principio **ACID**:
1. **Atomicidad**: Todas las operaciones se completan o ninguna.
2. **Consistencia**: La base de datos pasa de un estado válido a otro.
3. **Aislamiento**: Las operaciones no interfieren entre sí.
4. **Durabilidad**: Los cambios son permanentes una vez confirmados.

---

#### **Manejo de transacciones en Python y PostgreSQL**
En Python, usando la biblioteca `psycopg2`, puedes manejar transacciones de la siguiente manera:

1. **Iniciar una transacción**: Se inicia automáticamente al ejecutar la primera consulta SQL.
2. **Confirmar una transacción**: Usa `conexion.commit()` para guardar los cambios.
3. **Deshacer una transacción**: Usa `conexion.rollback()` para revertir los cambios en caso de error.

---

#### **Ejemplo básico de manejo de transacciones**

```python
import psycopg2

# Datos de conexión
config = {
    "dbname": "test_db",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432",
}

# Conectar a la base de datos
conexion = psycopg2.connect(**config)

try:
    # Crear un cursor
    cursor = conexion.cursor()

    # Iniciar una transacción (implícitamente al ejecutar la primera consulta)
    cursor.execute("INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)", 
                   ("Juan", "Pérez", "juan.perez@example.com"))

    # Ejecutar otra operación dentro de la misma transacción
    cursor.execute("UPDATE persona SET email = %s WHERE nombre = %s", 
                   ("juan.nuevo@example.com", "Juan"))

    # Confirmar la transacción (guardar los cambios)
    conexion.commit()
    print("Transacción confirmada.")

except Exception as e:
    # Si ocurre un error, deshacer la transacción
    conexion.rollback()
    print(f"Error: {e}. Transacción revertida.")

finally:
    # Cerrar el cursor y la conexión
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()
```

---

#### **Explicación del código**

1. **Conexión a la base de datos**:
   - Se establece una conexión con PostgreSQL usando `psycopg2.connect()`.

2. **Bloque `try`**:
   - Se inicia una transacción implícitamente al ejecutar la primera consulta SQL.
   - Se ejecutan dos operaciones: una inserción y una actualización.

3. **Confirmar la transacción**:
   - Si todas las operaciones tienen éxito, se llama a `conexion.commit()` para guardar los cambios en la base de datos.

4. **Bloque `except`**:
   - Si ocurre un error, se llama a `conexion.rollback()` para deshacer todas las operaciones de la transacción.

5. **Bloque `finally`**:
   - Se cierran el cursor y la conexión para liberar recursos.

---

#### **Uso de `with` para manejo automático de transacciones**
Puedes usar el bloque `with` para manejar automáticamente la confirmación o reversión de la transacción:

```python
try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)", 
                           ("Ana", "Gómez", "ana.gomez@example.com"))
            cursor.execute("UPDATE persona SET email = %s WHERE nombre = %s", 
                           ("ana.nuevo@example.com", "Ana"))
    print("Transacción confirmada automáticamente.")
except Exception as e:
    print(f"Error: {e}. Transacción revertida automáticamente.")
```

---

#### **Ventajas del manejo de transacciones**
1. **Atomicidad**: Garantiza que todas las operaciones se completen o ninguna.
2. **Consistencia**: Mantiene la integridad de los datos.
3. **Aislamiento**: Evita interferencias entre transacciones concurrentes.
4. **Durabilidad**: Los cambios confirmados son permanentes.

---

#### **Resumen**
- Las transacciones permiten ejecutar múltiples operaciones como una sola unidad.
- Usa `commit()` para confirmar los cambios y `rollback()` para deshacerlos en caso de error.
- El bloque `with` simplifica el manejo de transacciones al confirmar o revertir automáticamente.

### Correcciones de Mensajes de Error de Postgresql y Python

#### Abrir la configuración de postgresql

Abrir un archivo `postgresql.conf` en tu máquina.

```editorconfig
# ...
# Ruta del archivo a modificar, la versión puede variar
# NO agregar lineas extra al final del archivo
# C:\Program Files\PostgreSQL\13\data\postgresql.conf
# agregar al final del archivo
# Configuracion para que aparezcan los mensajes en python
lc_messages = 'en-US'
lc_monetary = 'en-US'
lc_numeric = 'en-US'
lc_time = 'en-US'
```

### Manejo de Transacciones con Python y Postgresql - Parte 1

![img.png](/screenshot/manejo_de_transacciones/img.png)

#### Código con comentarios explicativos

**📄 Código :**

```python
# Importar el módulo psycopg2 para conectarse a PostgreSQL
import psycopg2 as bd

# Establecer la conexión con la base de datos
# Se usan los parámetros de conexión: nombre de la base de datos, usuario, contraseña, host y puerto
conexion = bd.connect(
    database="test_db",  # Nombre de la base de datos
    user="postgres",     # Usuario de PostgreSQL
    password="admin",    # Contraseña del usuario
    host="localhost",    # Host donde está la base de datos
    port="5432"          # Puerto de PostgreSQL (por defecto es 5432)
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
```

**🟢 Ejecutar:**

```console
Termina la transacción
```

![img_1.png](/screenshot/manejo_de_transacciones/img_1.png)

---

#### Resumen del código

1. **Conexión a la base de datos**:
   - Se usa `psycopg2` para conectarse a PostgreSQL.
   - Se proporcionan los detalles de la conexión: nombre de la base de datos, usuario, contraseña, host y puerto.

2. **Manejo de transacciones**:
   - Se desactiva el modo `autocommit` para controlar manualmente cuándo se confirman (`commit`) o se deshacen (`rollback`) los cambios.
   - Esto es útil para garantizar que las operaciones se completen correctamente antes de guardar los cambios.

3. **Ejecución de una consulta**:
   - Se define una sentencia SQL para insertar datos en la tabla `persona`.
   - Se ejecuta la consulta con los valores proporcionados.

4. **Confirmación o deshacer cambios**:
   - Si todo funciona correctamente, se confirma la transacción con `commit`.
   - Si ocurre un error, se deshace la transacción con `rollback`.

5. **Cierre de la conexión**:
   - Finalmente, se cierra la conexión con la base de datos para liberar recursos.

---

#**Explicación de conceptos clave**

- **Transacción**: Es una secuencia de operaciones que se ejecutan como una sola unidad de trabajo. Si una operación falla, todas las operaciones anteriores se deshacen.
- **Commit**: Confirma los cambios realizados en la base de datos.
- **Rollback**: Deshace los cambios realizados en caso de error.
- **Cursor**: Es un objeto que permite ejecutar consultas SQL y recuperar resultados.

---

#### **Flujo del código**

1. Conectarse a PostgreSQL.
2. Desactivar `autocommit` para manejar manualmente la transacción.
3. Insertar datos en la tabla `persona`.
4. Si no hay errores, confirmar los cambios (`commit`).
5. Sí hay errores, deshacer los cambios (`rollback`).
6. Cerrar la conexión.

---

**¿Por qué es importante manejar transacciones?**

El manejo de transacciones es crucial para garantizar la **integridad de los datos**. Por ejemplo, si estás realizando múltiples operaciones (como insertar en varias tablas), quieres asegurarte de que todas se completen correctamente o que ninguna se aplique si hay un error. Esto evita que la base de datos quede en un estado inconsistente.

### Manejo de Transacciones con Python y Postgresql - Parte 2


Para cambiar la longitud de una columna `VARCHAR` en PostgreSQL, por ejemplo, cambiar la longitud de la columna `apellido` a `VARCHAR(10)`, puedes usar el comando `ALTER TABLE`. Si estás ejecutando PostgreSQL en un contenedor Docker, el proceso es el mismo, pero debes conectarte a la base de datos dentro del contenedor.

Aquí te explico cómo hacerlo paso a paso:

---

#### 1. **Conéctate al contenedor de PostgreSQL**

Primero, abre una terminal y conéctate al contenedor de PostgreSQL. Suponiendo que el nombre del contenedor es `pgdev`, ejecuta:

```bash
docker exec -it pgdev bash
```

Esto te dará acceso a una terminal dentro del contenedor.

---

#### 2. **Conéctate a la base de datos**

Dentro del contenedor, usa el cliente `psql` para conectarte a la base de datos. Por ejemplo, si tu base de datos se llama `test_db` y el usuario es `postgres`, ejecuta:

```bash
psql -U postgres -d test_db
```

---

#### 3. **Cambia la longitud de la columna `apellido`**

Una vez conectado a la base de datos, ejecuta el siguiente comando SQL para cambiar la longitud de la columna `apellido` a `VARCHAR(10)`:

```sql
ALTER TABLE persona
ALTER COLUMN apellido TYPE VARCHAR(10);
```

##### Explicación:
- **`ALTER TABLE persona`**: Especifica la tabla en la que deseas realizar el cambio.
- **`ALTER COLUMN apellido`**: Indica la columna que deseas modificar.
- **`TYPE VARCHAR(10)`**: Cambia el tipo de dato de la columna a `VARCHAR` con una longitud máxima de 10 caracteres.

---

#### 4. **Verifica el cambio**

Para asegurarte de que el cambio se aplicó correctamente, puedes ver la estructura de la tabla con el comando `\d`:

```sql
\d persona
```

Esto mostrará la definición de la tabla, incluyendo la columna `apellido` con su nuevo tipo `VARCHAR(10)`.

![img_2.png](/screenshot/manejo_de_transacciones/img_2.png)

---

#### 5. **Salir de `psql` y del contenedor**

Cuando hayas terminado, puedes salir de `psql` con el comando:

```sql
\q
```

Luego, sal del contenedor con:

```bash
exit
```

---

#### Alternativa: Ejecutar el comando SQL directamente desde fuera del contenedor

Si prefieres no entrar al contenedor, puedes ejecutar el comando SQL directamente desde tu máquina usando `docker exec`. Por ejemplo:

```bash
docker exec -it pgdev psql -U postgres -d test_db -c "ALTER TABLE persona ALTER COLUMN apellido TYPE VARCHAR(10);"
```

##### Explicación:
- **`docker exec`**: Ejecuta un comando dentro del contenedor.
- **`psql -U postgres -d test_db`**: Conéctate a la base de datos `test_db` como usuario `postgres`.
- **`-c "ALTER TABLE ..."`**: Ejecuta el comando SQL directamente.

---

#### Resumen

1. Conéctate al contenedor de PostgreSQL con `docker exec`.
2. Usa `psql` para conectarte a la base de datos.
3. Ejecuta el comando `ALTER TABLE` para cambiar la longitud de la columna `apellido`.
4. Verifica el cambio con `\d persona`.
5. Sal de `psql` y del contenedor.

**📄 Código :**

```python
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
    valores = ("Carlos", "Lara", "clara@mail.com")
    # Ejecutar la sentencia SQL con los valores proporcionados
    cursor.execute(sentencia, valores)

    sentencia = (
        "UPDATE persona SET apellido = %s, email = %s WHERE nombre = %s WHERE id = %s"
    )
    valores = ("Juan Carlos", "Juarez", "jcjuarez@mail.com", 1)
    # Ejecutar la sentencia SQL con los valores proporcionados
    cursor.execute(sentencia, valores)

    # Confirmar la transacción (guardar los cambios en la base de datos)
    conexion.commit()
    # Mensaje de éxito
    print(f"Termina la transacción, se hizo commit entre insertado e actualizado")
except Exception as e:
    # Si ocurre un error, deshacer la transacción (rollback)
    conexion.rollback()
    # Mostrar el error que ocurrió
    print(f"Ocurrió un error: {e}")
finally:
    # Cerrar la conexión con la base de datos, independientemente de si hubo un error o no
    conexion.close()

```

**🟢 Ejecutar:**

```console
Termina la transacción, se hizo commit entre insertado e actualizado
```

![img_3.png](/screenshot/manejo_de_transacciones/img_3.png)

### Manejo de Transacciones con with


**📄 Código :**

```python
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

```

**🟢 Ejecutar:**

```console
Termina la transacción, se hizo commit entre insertado e actualizado
```

![img_4.png](/screenshot/manejo_de_transacciones/img_4.png)