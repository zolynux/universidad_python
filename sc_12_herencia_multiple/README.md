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

### MRO (Method Resolution Order)

El **MRO (Method Resolution Order)** en Python es el orden en el que el intérprete de Python busca métodos y atributos en una jerarquía de clases, especialmente en casos de herencia múltiple. El MRO determina cuál método o atributo se ejecuta o se accede cuando hay ambigüedades debido a que una clase hereda de varias clases base.

#### ¿Por qué es importante el MRO?

En Python, una clase puede heredar de múltiples clases (herencia múltiple). Esto puede llevar a situaciones en las que dos o más clases base define un método o atributo con el mismo nombre. El MRO resuelve este problema definiendo un orden claro y predecible para buscar métodos y atributos.

#### ¿Cómo funciona el MRO?

Python utiliza un algoritmo llamado **C3 Linearización** para calcular el MRO. Este algoritmo garantiza que:

1. El orden sea consistente y predecible.
2. Se respecte el orden de herencia definido por el programador.
3. No haya ciclos en la jerarquía de herencia.

El MRO sigue estos principios:

- Una clase siempre tiene prioridad sobre sus clases base.
- Si una clase hereda de múltiples clases, el orden en que se específican las clases base importa.
- Se respecta el orden de herencia de izquierda a derecha.

**Ejemplo básico de MRO:**

````python
class A:
    def metodo(self):
        print("Método de A")

class B(A):
    def metodo(self):
        print("Método de B")

class C(A):
    def metodo(self):
        print("Método de C")

class D(B, C):
    pass

objeto = D()
objeto.metodo()  # ¿Qué método se ejecuta?
````

En este caso, el MRO de la clase `D` se calcula como:

1. `D` (la clase actual).
2. `B` (la primera clase base).
3. `C` (la segunda clase base).
4. `A` (la clase base común).
5. `object` (la clase base de todas las clases en Python).

Puedes ver el MRO usando el método `mro()` o el atributo `__mro__`:

```python
print(D.mro())
# Salida: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

En este ejemplo, cuando llamas a `objeto.metodo()`, Python sigue el MRO y ejecuta el método de la clase `B`, porque `B` aparece antes que `C` en el orden de herencia.

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

# MRO - Method Resolution Order
print(Cuadrado.mro())
```

**🟢 Ejecutar:**

```console
Calculo área cuadrado: 25
[<class 'Cuadrado.Cuadrado'>, <class 'FiguraGeometrica.FiguraGeometrica'>, <class 'Color.Color'>, <class 'object'>]
```