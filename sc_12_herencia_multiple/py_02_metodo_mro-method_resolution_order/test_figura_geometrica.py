from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'Rojo')
print(f'Calculo área cuadrado: {cuadrado1.calcular_area()}')

# MRO - Method Resolution Order
print(Cuadrado.mro())