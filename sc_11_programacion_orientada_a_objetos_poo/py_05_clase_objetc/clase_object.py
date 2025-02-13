class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobrescribir el metodo __str__
    def __str__(self):
        return f"""Persona:
        Nombre = {self.nombre}
        Apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}"""


# Programa principal
print("*** Clase Object ***")
persona1 = Persona("Ana", "Martinez")
print(persona1)  # El metodo __str__ se llama automaticamente desde print
# print(persona1.__str__()) # Esto es opcional
