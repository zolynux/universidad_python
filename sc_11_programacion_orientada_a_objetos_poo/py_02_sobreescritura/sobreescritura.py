class Animal:
    def comer(self):
        print("Como muchas veces el día")

    def dormir(self):
        print("Duermo muchas horas")


class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo lagdrar")

    # Sobreescritura del metodo dormir
    def dormir(self):
        print("Duermo 15 Horas al día")


# Programa Principal
print("*** Ejemplo de Sobreescritura en Python ***")
print("Clase Padre, soy un Animal")

animal1 = Animal()
animal1.comer()
animal1.dormir()

print("\nClase Hija, soy un Perro")
perro1 = Perro()
perro1.hacer_sonido()
perro1.dormir()  #  Se llama el método sobreescrito  de la clase hija
perro1.comer()
