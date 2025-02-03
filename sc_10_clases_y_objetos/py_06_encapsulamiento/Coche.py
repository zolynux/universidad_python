# Definimos la clase coche
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca  # atributo publico
        self._modelo = modelo  # Atributo Protegido
        self.__color = color  # Atributo Privado

    def conducir(self):
        print(
            f"""Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}"""
        )


# Programa principal
if __name__ == "__main__":
    print("*** Encapsulamiento ***")
    # Creación de un primer objeto coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
    coche1.marca = "Toyota 2"
    coche1._modelo = "Yaris 2"  # Esto no es una buena práctica
    coche1.__color = "Azul 2"  # Ignoro la modificación
    coche1._Coche__color = "Azul 3"  # Es una mala práctica
    coche1.conducir()
