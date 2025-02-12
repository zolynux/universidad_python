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


# Programa principal
print("*** Ejemplo Polimorfismo ***")

# Definimos un objeto de la clase Animal
print("Clase Padre - Animal:")
animal1 = Animal()
animal1.hacer_sonido()

# Definimos un objeto de la clase Perro
print("\nClase hija - Perro:")
perro1 = Perro()
perro1.hacer_sonido()  # Polimorfismo

# Definimos un objeto de la clase Gato
print("\nClase hija - Gato:")
gato1 = Gato()
gato1.hacer_sonido()  # Polimorfismo
