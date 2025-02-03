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

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


# Programa principal
if __name__ == "__main__":
    print("*** Métodos get y set ***")
    # Creación de un primer objeto coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean públicos
    coche1.set_marca("Toyota 2")
    coche1.set_modelo("Yaris 2")
    coche1.set_color("Azul 2")
    coche1.conducir()
