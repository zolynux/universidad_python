# Herencia Multiple

## Herencia Múltiple

La **herencia múltiple** en Python es un mecanismo que permite a una clase heredar atributos y métodos de más de una clase base. Esto significa que una clase derivada puede tener múltiples clases padre, combinando así sus funcionalidades.

#### Ejemplo básico

```python
class ClaseA:
    def metodo_a(self):
        print("Método de Clase A")

class ClaseB:
    def metodo_b(self):
        print("Método de Clase B")

class ClaseC(ClaseA, ClaseB):  # Herencia múltiple
    def metodo_c(self):
        print("Método de Clase C")

objeto = ClaseC()
objeto.metodo_a()  # Salida: Método de Clase A
objeto.metodo_b()  # Salida: Método de Clase B
objeto.metodo_c()  # Salida: Método de Clase C
```

En este ejemplo, `ClaseC` hereda de `ClaseA` y `ClaseB`, por lo que puede acceder a los métodos de ambas clases.

#### Orden de resolución de métodos (MRO)

Cuando una clase hereda de múltiples clases, Python utiliza el **MRO (Method Resolution Order)** para determinar el orden en que se buscan los métodos y atributos. El MRO sigue el algoritmo **C3 Linearization**, que garantiza un orden consistente y evita ambigüedades.

Puedes ver el MRO de una clase usando el método `mro()` o el atributo `__mro__`:

```python
print(ClaseC.mro())
# Salida: [<class '__main__.ClaseC'>, <class '__main__.ClaseA'>, <class '__main__.ClaseB'>, <class 'object'>]
```

#### Consideraciones

1. **Conflictos de nombres**: Si dos clases base tienen métodos o atributos con el mismo nombre, el MRO determina cuál se usará. Por ejemplo, si `ClaseA` y `ClaseB` tienen un método llamado `metodo`, se usará el de `ClaseA` porque aparece primero en el MRO.

2. **Complejidad**: El uso excesivo de herencia múltiple puede hacer que el código sea difícil de entender y mantener. Es recomendable usarla con cuidado.

3. **Alternativas**: En muchos casos, es preferible usar **composición** (incluir objetos de otras clases como atributos) en lugar de herencia múltiple.

#### Ejemplo con conflicto de nombres

```python
class ClaseA:
    def metodo(self):
        print("Método de Clase A")

class ClaseB:
    def metodo(self):
        print("Método de Clase B")

class ClaseC(ClaseA, ClaseB):
    pass

objeto = ClaseC()
objeto.metodo()  # Salida: Método de Clase A (porque ClaseA aparece primero en el MRO)
```

En resumen, la herencia múltiple es una herramienta poderosa en Python, pero debe usarse con precaución para evitar complicaciones en el diseño del código.


**📄 Código :**

**FiguraGeometrica:**

```python
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
```

**Color:**

```python
class Color:
    def __init__(self, color):
        self.color = color
```

**Cuadrado:**

```python
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self,lado,color):
        # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
```

**test_figura_geometrica:**

```python
from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'Rojo')
print(f'Calculo área cuadrado: {cuadrado1.calcular_area()}')
```

**🟢 Ejecutar:**

```console
Calculo área cuadrado: 25
```


