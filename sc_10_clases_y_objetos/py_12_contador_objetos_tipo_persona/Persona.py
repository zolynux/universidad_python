class Persona:
    # Atributo clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")


if __name__ == "__main__":
    print("*** Ejemplo Contador de objetos de tipo Persona ***")
    # Primer objeto
    persona1 = Persona("Gerardo", "Perez")
    persona1.mostrar_persona()

    # Segundo objeto
    persona2 = Persona("Daniel", "Sanchez")
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de Personas
    print(f"Contador objetos Persona: {Persona.contador_personas}")
