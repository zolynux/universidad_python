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
    print("*** Mejora de Encapsulamiento ***")
    # Creación de un primer objeto coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
    # No deberíamos acceder a los atributos que no sean públicos
    coche1.marca = "Toyota 2"
    coche1.modelo = "Yaris 2"
    coche1.color = "Azul 2"
    coche1.conducir()
    # Atributo de marca del coche1
    coche1.marca = "Toyota 3"
    print(f"Atributo marcha coche1: {coche1.marca}")
