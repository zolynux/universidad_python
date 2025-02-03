# Definimos la clase coche
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # atributo publico
        self._modelo = modelo  # Atributo Protegido
        self._color = color  # Atributo Privado

    def conducir(self):
        print(
            f"""Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}"""
        )

    # def get_marca(self):
    #     return self._marca
    @property  # Definir el método get de manera más pythonica
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == "__main__":
    print("*** Atributos dinámicos ***")
    # Creación de un primer objeto coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
    # No deberíamos acceder a los atributos que no sean públicos
    coche1.marca = "Toyota 2"
    coche1.modelo = "Yaris 2"
    coche1.color = "Azul 2"
    coche1.conducir()
    # Intentar agregar un nuevo atributo
    setattr(coche1, "nuevo_atributo", "valor nuevo atributo")
    coche1.nuevo_atributo2 = "Valor nuevo atributo 2"
    print(f"Atributo del coche1: {coche1.__dict__}")
    coche1.conducir()
    print(coche1.nuevo_atributo)
    print(f"Nuevo atributo coche1 {coche1.nuevo_atributo2}")
    # segundo objeto
    coche2 = Coche("Chevrolet", "Trax", "Blanco")
    coche2.conducir()
    print(f"Atributo del coche2: {coche2.__dict__}")
    # print(f"Nuevo atributo coche2 {coche2.nuevo_atributo}")
    # print(f"Nuevo atributo 2 coche2 {coche2.nuevo_atributo2}")
