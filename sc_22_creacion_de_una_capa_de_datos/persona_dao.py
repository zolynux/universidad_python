from conexion import Conexion
from persona import Persona
from logger_base import log


class PersonaDAO:
    # DAO (Data Access Object)
    # CRUD (Create-Read-Update-Delete)
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    _ACTUALIZAR = (
        "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id = %s"
    )
    _ELIMINAR = "DELETE FROM persona WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(
                        registro[0], registro[1], registro[2], registro[3]
                    )
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Persona insertada: {persona}")
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f"Persona actualizada: {persona}")
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_conexion() as cursor:
                valores = persona.id
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f"Persona eliminada: {persona}")
                return cursor.rowcount


if __name__ == "__main__":
    """
    # Insertar un registro
    perosna1 = Persona(nombre="Pedro", apellido="Najera", email="pnajera@mail.com")
    personas_insertadas = PersonaDAO.insertar(perosna1)
    log.debug(f"Personas insertadas:{personas_insertadas}".center(40, "="))
    """

    """
    # Actualizar un registro
    persona1 = Persona(1, "Juan Carlos", "Juarez", "cjjuarez@mail.com")
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actualizadas:{personas_actualizadas}".center(40, "="))
    """

    """
    # Eliminar un registro
    persona1 = Persona(id_persona=20)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas eliminadas:{personas_eliminadas}".center(40, "="))
    """

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
