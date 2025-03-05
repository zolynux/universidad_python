from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("Creación Objeto Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(lado=5, color="rojo")
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f"Calculo área cuadrado: {cuadrado1.calcular_area()}")
print(cuadrado1)

print("Creación Objeto Rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(alto=2, ancho=8, color="verde")
rectangulo1.ancho = 9
rectangulo1.alto = 8

print(f"Calculo área rectangulo: {rectangulo1.calcular_area()}")
print(rectangulo1)
