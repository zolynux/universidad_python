## Conexión a Bases de Datos con Python y Postgresql

La **conexión a bases de datos con Python y PostgreSQL** se refiere al proceso de interactuar con una base de datos PostgreSQL desde un programa en Python. Esto permite realizar operaciones como consultas, inserciones, actualizaciones y eliminaciones de datos almacenados en la base de datos. Para lograr esto, se utiliza un **driver** o **adaptador** que permite la comunicación entre Python y PostgreSQL.

---

#### **Componentes principales**

1. **PostgreSQL**:
   - Es un sistema de gestión de bases de datos relacional (RDBMS) open source.
   - Soporta SQL estándar y ofrece características avanzadas como transacciones, triggers y procedimientos almacenados.

2. **Python**:
   - Es un lenguaje de programación que permite conectarse a PostgreSQL mediante bibliotecas específicas.

3. **Driver/Adaptador**:
   - Es un módulo que permite la comunicación entre Python y PostgreSQL.
   - El más utilizado es **`psycopg2`**, aunque también existen alternativas como **`pg8000`** o **`asyncpg`** (para programación asíncrona).

---

**Pasos para conectar Python con PostgreSQL**

1. **Instalar el driver**:
   - Instala el módulo `psycopg2` usando `pip`:
     ```bash
     pip install psycopg2
     ```

2. **Conectar a la base de datos**:
   - Usa la función `psycopg2.connect()` para establecer una conexión con la base de datos.

3. **Crear un cursor**:
   - Un cursor es un objeto que permite ejecutar consultas SQL y recuperar resultados.

4. **Ejecutar consultas**:
   - Usa el cursor para ejecutar comandos SQL como `SELECT`, `INSERT`, `UPDATE`, `DELETE`, etc.

5. **Manejar transacciones**:
   - Confirma los cambios con `commit()` o deshazlos con `rollback()`.

6. **Cerrar la conexión**:
   - Cierra el cursor y la conexión para liberar recursos.

---

**Ejemplo básico de conexión**

```python
import psycopg2

# Datos de conexión
config = {
    "dbname": "nombre_basedatos",
    "user": "usuario",
    "password": "contraseña",
    "host": "localhost",  # o la dirección del servidor
    "port": 5432,         # Puerto por defecto de PostgreSQL
}

try:
    # Establecer la conexión
    conexion = psycopg2.connect(**config)
    print("¡Conexión exitosa!")

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar una consulta SQL
    cursor.execute("SELECT version();")
    version = cursor.fetchone()  # Obtener el resultado
    print("Versión de PostgreSQL:", version)

    # Ejecutar una consulta SELECT
    cursor.execute("SELECT * FROM mi_tabla;")
    filas = cursor.fetchall()  # Obtener todas las filas
    for fila in filas:
        print(fila)

    # Ejecutar una consulta INSERT
    cursor.execute("INSERT INTO mi_tabla (columna1, columna2) VALUES (%s, %s);", ("valor1", "valor2"))

    # Confirmar los cambios
    conexion.commit()
    print("Inserción exitosa.")

except psycopg2.Error as e:
    print("Error al conectar a PostgreSQL:", e)

finally:
    # Cerrar el cursor y la conexión
    if cursor:
        cursor.close()
    if conexion:
        conexion.close()
        print("Conexión cerrada.")
```

---

**Explicación del código**

1. **Importar `psycopg2`**:
   - El módulo `psycopg2` es necesario para interactuar con PostgreSQL.

2. **Datos de conexión**:
   - Se especifican los detalles de la base de datos (`dbname`, `user`, `password`, `host`, `port`).

3. **Establecer la conexión**:
   - `psycopg2.connect(**config)` abre una conexión con la base de datos.

4. **Crear un cursor**:
   - `conexion.cursor()` crea un cursor para ejecutar consultas.

5. **Ejecutar consultas**:
   - `cursor.execute()` ejecuta comandos SQL.
   - `cursor.fetchone()` o `cursor.fetchall()` recuperan los resultados de una consulta.

6. **Manejar transacciones**:
   - `conexion.commit()` confirma los cambios en la base de datos.
   - `conexion.rollback()` deshace los cambios en caso de error.

7. **Cerrar la conexión**:
   - `cursor.close()` y `conexion.close()` liberan los recursos.

---

**Operaciones comunes**

1. **Consultar datos**:
   ```python
   cursor.execute("SELECT * FROM mi_tabla;")
   filas = cursor.fetchall()
   for fila in filas:
       print(fila)
   ```

2. **Insertar datos**:
   ```python
   cursor.execute("INSERT INTO mi_tabla (columna1, columna2) VALUES (%s, %s);", ("valor1", "valor2"))
   conexion.commit()
   ```

3. **Actualizar datos**:
   ```python
   cursor.execute("UPDATE mi_tabla SET columna1 = %s WHERE id = %s;", ("nuevo_valor", 1))
   conexion.commit()
   ```

4. **Eliminar datos**:
   ```python
   cursor.execute("DELETE FROM mi_tabla WHERE id = %s;", (1,))
   conexion.commit()
   ```

---

**Buenas prácticas**

1. **Usar `with`**:
   - Puedes usar el bloque `with` para manejar la conexión y el cursor automáticamente:
     ```python
     with psycopg2.connect(**config) as conexion:
         with conexion.cursor() as cursor:
             cursor.execute("SELECT * FROM mi_tabla;")
             print(cursor.fetchall())
     ```

2. **Manejar excepciones**:
   - Captura excepciones específicas de `psycopg2` para manejar errores de conexión o consultas.

3. **Usar parámetros en consultas**:
   - Siempre usa parámetros (`%s`) en lugar de concatenar cadenas para evitar inyecciones SQL.

4. **Cerrar recursos**:
   - Asegúrate de cerrar el cursor y la conexión para liberar recursos.

---

**Resumen**
- La conexión a PostgreSQL desde Python se realiza usando el módulo `psycopg2`.
- Permite ejecutar consultas SQL, manejar transacciones y recuperar datos.
- Es importante seguir buenas prácticas como el uso de `with`, manejo de excepciones y cierre de recursos.

Conectar **PostgreSQL en Docker** con **Azure Data Studio** en tu máquina local es un proceso que implica varios pasos. A continuación, te explico cómo hacerlo de manera detallada.

---

**1. Instalar Docker**
Si no tienes Docker instalado, descárgalo e instálalo desde [docker.com](https://www.docker.com/).

---

**2. Descargar y ejecutar PostgreSQL en Docker**
1. **Descargar la imagen de PostgreSQL**:
   Abre una terminal y ejecuta:
   ```bash
   docker pull postgres
   ```

2. **Ejecutar un contenedor de PostgreSQL**:
   Crea y ejecuta un contenedor con PostgreSQL:
   ```bash
   docker run --name mi-postgres -e POSTGRES_PASSWORD=mi_contraseña -d -p 5432:5432 postgres
   ```
   - `--name mi-postgres`: Asigna un nombre al contenedor.
   - `-e POSTGRES_PASSWORD=mi_contraseña`: Define la contraseña del usuario `postgres`.
   - `-d`: Ejecuta el contenedor en segundo plano.
   - `-p 5432:5432`: Mapea el puerto 5432 del contenedor al puerto 5432 de tu máquina local.
   - `postgres`: Especifica la imagen a usar.

3. **Verificar que el contenedor esté en ejecución**:
   ```bash
   docker ps
   ```
   Deberías ver el contenedor `mi-postgres` en la lista.

---

**3. Instalar Azure Data Studio**
Si no lo tienes instalado, descarga Azure Data Studio desde [aquí](https://learn.microsoft.com/en-us/sql/azure-data-studio/download-azure-data-studio).

---

**4. Conectar Azure Data Studio a PostgreSQL**
Azure Data Studio es principalmente una herramienta para SQL Server, pero puedes usarla con PostgreSQL instalando una extensión.

1. **Instalar la extensión de PostgreSQL**:
   - Abre Azure Data Studio.
   - Ve a la pestaña **Extensions** (Extensiones).
   - Busca **"PostgreSQL"** e instala la extensión oficial.

2. **Crear una conexión a PostgreSQL**:
   - Haz clic en **New Connection** (Nueva Conexión).
   - En **Connection Type** (Tipo de Conexión), selecciona **PostgreSQL**.
   - Completa los detalles de la conexión:
     - **Server name**: `localhost`
     - **Port**: `5432`
     - **Database**: `postgres` (base de datos predeterminada).
     - **User name**: `postgres` (usuario predeterminado).
     - **Password**: `mi_contraseña` (la que definiste al crear el contenedor).
   - Haz clic en **Connect** (Conectar).

3. **Explorar la base de datos**:
   - Una vez conectado, verás la base de datos `postgres` en el panel izquierdo.
   - Puedes ejecutar consultas SQL, crear tablas, insertar datos, etc.

---

**5. Ejemplo de uso**

**Crear una tabla y insertar datos**:
1. Abre una nueva pestaña de consulta en Azure Data Studio.
2. Ejecuta el siguiente SQL:
   ```sql
   CREATE TABLE mi_tabla (
       id SERIAL PRIMARY KEY,
       nombre VARCHAR(50),
       edad INT
   );

   INSERT INTO mi_tabla (nombre, edad) VALUES ('Juan', 25);
   INSERT INTO mi_tabla (nombre, edad) VALUES ('Ana', 30);
   ```

3. Consulta los datos:
   ```sql
   SELECT * FROM mi_tabla;
   ```

---

**6. Detener y reiniciar el contenedor**
- **Detener el contenedor**:
  ```bash
  docker stop mi-postgres
  ```
- **Reiniciar el contenedor**:
  ```bash
  docker start mi-postgres
  ```

---

**7. Eliminar el contenedor (opcional)**
Si ya no necesitas el contenedor, puedes eliminarlo:
```bash
docker rm -f mi-postgres
```

---

**Resumen**
1. **Docker**: Ejecuta PostgreSQL en un contenedor.
2. **Azure Data Studio**: Conéctate a PostgreSQL usando la extensión oficial.
3. **Interactúa**: Crea tablas, inserta datos y ejecuta consultas.

Para crear una base de datos llamada `test_db` en PostgreSQL usando una consulta SQL (`SQLQuery`), sigue estos pasos:

---

**1. Conéctate a PostgreSQL**
Primero, asegúrate de estar conectado a tu instancia de PostgreSQL. Puedes hacerlo desde:
- Una terminal usando `psql`.
- Una herramienta gráfica como **pgAdmin**, **DBeaver** o **Azure Data Studio**.
- Un contenedor de Docker si estás usando PostgreSQL en Docker.

---

**2. Ejecuta la consulta SQL**
Una vez conectado, ejecuta la siguiente consulta SQL para crear la base de datos `test_db`:

```sql
CREATE DATABASE test_db;
```

---

**3. Verifica la creación de la base de datos**
Para asegurarte de que la base de datos se ha creado correctamente, puedes listar todas las bases de datos con:

```sql
\l
```

Esto mostrará una lista de todas las bases de datos en tu servidor PostgreSQL. Deberías ver `test_db` en la lista.

---

**4. Conéctate a la nueva base de datos**
Si estás usando `psql`, puedes conectarte a la nueva base de datos con:

```bash
\c test_db
```

Si estás usando una herramienta gráfica, selecciona `test_db` en la lista de bases de datos.

---

**5. Ejemplo completo en `psql`**
Si estás usando `psql` desde la terminal, el proceso completo sería:

```bash
# Conéctate a PostgreSQL (usando el usuario postgres)
psql -U postgres

# Crea la base de datos test_db
CREATE DATABASE test_db;

# Verifica la creación de la base de datos
\l

# Conéctate a la nueva base de datos
\c test_db
```

---

**6. Ejemplo en Docker**
Si estás usando PostgreSQL en Docker, puedes ejecutar la consulta directamente en el contenedor:

```bash
# Conéctate al contenedor de PostgreSQL
docker exec -it mi-postgres psql -U postgres

# Crea la base de datos test_db
CREATE DATABASE test_db;

# Verifica la creación de la base de datos
\l

# Conéctate a la nueva base de datos
\c test_db
```

Para crear una tabla llamada `Persona` en el esquema `public` de una base de datos PostgreSQL, puedes usar la siguiente consulta SQL. Asegúrate de estar conectado a la base de datos donde deseas crear la tabla (por ejemplo, `test_db`).

---

### Creación de Bases de Datos y Table de Persona

**Crear la tabla `Persona`**
Ejecuta la siguiente consulta SQL para crear la tabla `Persona` en el esquema `public`:

```sql
CREATE TABLE public.Persona (
    id SERIAL PRIMARY KEY NOT NULL,          -- Columna de tipo SERIAL para un ID autoincremental
    nombre VARCHAR(50),    -- Columna para el nombre (máximo 50 caracteres)
    apellido VARCHAR(50),  -- Columna para el apellido (máximo 50 caracteres)
    email VARCHAR(100)       -- Columna para el email (máximo 100 caracteres, único)
);
```

---

**Explicación de la consulta**
- **`public.Persona`**: Crea la tabla `Persona` en el esquema `public`. Si no especificas el esquema, PostgreSQL usa `public` por defecto.
- **`id SERIAL PRIMARY KEY`**:
  - `SERIAL`: Crea un número entero autoincremental.
  - `PRIMARY KEY`: Define la columna `id` como clave primaria.
- **`nombre VARCHAR(50) NOT NULL`**:
  - `VARCHAR(50)`: Almacena una cadena de texto con un máximo de 50 caracteres.
  - `NOT NULL`: La columna no puede estar vacía.
- **`apellido VARCHAR(50) NOT NULL`**: Similar a `nombre`.
- **`email VARCHAR(100) UNIQUE`**:
  - **`VARCHAR(100)`**: Almacena una cadena de texto con un máximo de 100 caracteres.

---

**Insertar datos en la tabla**

Una vez creada la tabla, puedes insertar datos:

```sql
INSERT INTO PUBLIC.Persona (nombre, apellido, email)
VALUES ('Juan', 'Perez', 'jperez@mail.com');
    
INSERT INTO PUBLIC.Persona (nombre, apellido, email)
VALUES ('Karla', 'Gomez', 'kgomez@mail.com');
```

---

**Consultar los datos**
Para ver los datos insertados, ejecuta:

```sql
SELECT * FROM public.Persona;
```

### Consultas SQL Básicas

¡Correcto! Has resumido muy bien las operaciones básicas de **CRUD** (Create, Read, Update, Delete) en SQL. Vamos a explicar cada una de las consultas que has mencionado y cómo funcionan en el contexto de una tabla llamada `persona`.

---

**Operaciones CRUD**

**1. SELECT - Seleccionar Registros**
```sql
SELECT * FROM persona WHERE id IN (1, 2);
```
- **Qué hace**: Selecciona todos los registros de la tabla `persona` donde el `id` sea 1 o 2.
- **Resultado**: Devuelve las filas con `id = 1` e `id = 2`.

---

**2. INSERT - Agregar Registros**
```sql
INSERT INTO persona(nombre, apellido, email) VALUES ('Susana', 'Lara', 'slara@mail.com');
```
- **Qué hace**: Inserta un nuevo registro en la tabla `persona` con los valores especificados.
- **Resultado**: Se agrega una nueva fila con los datos de Susana Lara.

---

**3. SELECT - Ver todos los registros**
```sql
SELECT * FROM persona;
```
- **Qué hace**: Selecciona todos los registros de la tabla `persona`.
- **Resultado**: Devuelve todas las filas de la tabla.

---

**4. UPDATE - Actualizar Registros**
```sql
UPDATE persona SET nombre = 'Ivonne', email = 'ieparza@mail.com' WHERE id = 3;
```
- **Qué hace**: Actualiza los campos `nombre` y `email` del registro con `id = 3`.
- **Resultado**: La fila con `id = 3` ahora tiene `nombre = 'Ivonne'` y `email = 'ieparza@mail.com'`.

---

**5. SELECT - Ver todos los registros**
```sql
SELECT * FROM persona;
```
- **Qué hace**: Selecciona todos los registros de la tabla `persona` después de la actualización.
- **Resultado**: Devuelve todas las filas de la tabla, incluyendo los cambios realizados.

---

**6. DELETE - Eliminar Registros**
```sql
DELETE FROM persona WHERE id = 3;
```
- **Qué hace**: Elimina el registro con `id = 3` de la tabla `persona`.
- **Resultado**: La fila con `id = 3` se elimina permanentemente.

---

**7. SELECT - Ver todos los registros**
```sql
SELECT * FROM persona;
```
- **Qué hace**: Selecciona todos los registros de la tabla `persona` después de la eliminación.
- **Resultado**: Devuelve todas las filas de la tabla, excluyendo la fila eliminada.

---

**Ejemplo completo**

Supongamos que la tabla `persona` tiene la siguiente estructura y datos iniciales:

```sql
CREATE TABLE persona (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO persona (nombre, apellido, email) VALUES
('Juan', 'Pérez', 'juan.perez@mail.com'),
('Ana', 'Gómez', 'ana.gomez@mail.com'),
('Carlos', 'López', 'carlos.lopez@mail.com');
```

**Datos iniciales**:
```
 id | nombre | apellido |          email
----+--------+----------+------------------------
  1 | Juan   | Pérez    | juan.perez@mail.com
  2 | Ana    | Gómez    | ana.gomez@mail.com
  3 | Carlos | López    | carlos.lopez@mail.com
```

**Ejecución de las consultas**:

1. **SELECT con `IN`**:
   ```sql
   SELECT * FROM persona WHERE id IN (1, 2);
   ```
   **Resultado**:
   ```
    id | nombre | apellido |          email
   ----+--------+----------+------------------------
     1 | Juan   | Pérez    | juan.perez@mail.com
     2 | Ana    | Gómez    | ana.gomez@mail.com
   ```

2. **INSERT**:
   ```sql
   INSERT INTO persona(nombre, apellido, email) VALUES ('Susana', 'Lara', 'slara@mail.com');
   ```
   **Resultado**:
   ```
    id | nombre | apellido |          email
   ----+--------+----------+------------------------
     1 | Juan   | Pérez    | juan.perez@mail.com
     2 | Ana    | Gómez    | ana.gomez@mail.com
     3 | Carlos | López    | carlos.lopez@mail.com
     4 | Susana | Lara     | slara@mail.com
   ```

3. **SELECT todos los registros**:
   ```sql
   SELECT * FROM persona;
   ```
   **Resultado**:
   ```
    id | nombre | apellido |          email
   ----+--------+----------+------------------------
     1 | Juan   | Pérez    | juan.perez@mail.com
     2 | Ana    | Gómez    | ana.gomez@mail.com
     3 | Carlos | López    | carlos.lopez@mail.com
     4 | Susana | Lara     | slara@mail.com
   ```

4. **UPDATE**:
   ```sql
   UPDATE persona SET nombre = 'Ivonne', email = 'ieparza@mail.com' WHERE id = 3;
   ```
   **Resultado**:
   ```
    id | nombre | apellido |          email
   ----+--------+----------+------------------------
     1 | Juan   | Pérez    | juan.perez@mail.com
     2 | Ana    | Gómez    | ana.gomez@mail.com
     3 | Ivonne | López    | ieparza@mail.com
     4 | Susana | Lara     | slara@mail.com
   ```

5. **SELECT todos los registros**:
   ```sql
   SELECT * FROM persona;
   ```
   **Resultado**:
   ```
    id | nombre | apellido |          email
   ----+--------+----------+------------------------
     1 | Juan   | Pérez    | juan.perez@mail.com
     2 | Ana    | Gómez    | ana.gomez@mail.com
     3 | Ivonne | López    | ieparza@mail.com
     4 | Susana | Lara     | slara@mail.com
   ```

6. **DELETE**:
   ```sql
   DELETE FROM persona WHERE id = 3;
   ```
   **Resultado**:
   ```
    id | nombre | apellido |          email
   ----+--------+----------+------------------------
     1 | Juan   | Pérez    | juan.perez@mail.com
     2 | Ana    | Gómez    | ana.gomez@mail.com
     4 | Susana | Lara     | slara@mail.com
   ```

7. **SELECT todos los registros**:
   ```sql
   SELECT * FROM persona;
   ```
   **Resultado**:
   ```
    id | nombre | apellido |          email
   ----+--------+----------+------------------------
     1 | Juan   | Pérez    | juan.perez@mail.com
     2 | Ana    | Gómez    | ana.gomez@mail.com
     4 | Susana | Lara     | slara@mail.com
   ```

---

**Resumen**
- **SELECT**: Para consultar datos.
- **INSERT**: Para agregar nuevos registros.
- **UPDATE**: Para modificar registros existentes.
- **DELETE**: Para eliminar registros.
