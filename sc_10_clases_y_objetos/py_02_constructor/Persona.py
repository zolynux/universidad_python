# Definición de una clase
class Persona:
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(
            f"""Persona:
    Nombre: {self.nombre}
    Apellido: {self.apellido}"""
        )


# Creación de objetos
if __name__ == "__main__":
    # Creación de un primer objeto
    persona1 = Persona("Layla", "Acosta")  # Crea un objeto vacio en memoria
    # persona1.inicializar_persona("Layla", "Acosta")
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona("Ian", "Sánchez")  # Crea un objeto vacío en memoria
    # persona2.inicializar_persona("Ian", "Sánchez")
    persona2.mostrar_persona()
