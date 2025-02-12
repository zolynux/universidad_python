# Polimorfismo


class Animal:
    def hacer_sonido(self):
        print("Hago un pitido")


class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")


class Gato(Animal):
    def hacer_sonido(self):
        print("Puedo maullar")


# Función polimorfismo (Duck Typing)
def hacer_sonido_anima(animal):  # DuckTyping
    animal.hacer_sonido()


# Programa principal
print("*** Ejemplo DuckTyping ***")

# Definimos un objeto de la clase Animal
print("Clase Padre - Animal:")
animal1 = Animal()
hacer_sonido_anima(animal1)  # DuckTyping

# Definimos un objeto de la clase Perro
print("\nClase hija - Perro:")
perro1 = Perro()
hacer_sonido_anima(perro1)  # DuckTyping

# Definimos un objeto de la clase Gato
print("\nClase hija - Gato:")
gato1 = Gato()
hacer_sonido_anima(gato1)  # DuckTyping
