# Clases Abstractas

## Clases Abstractas

Las **clases abstractas** en Python son clases que no pueden ser instancias directamente, sino que qe están diseñadas para ser heredadas por otras clases. Su propósito principal es definir una interfaz común o un conjunto de métodos que las subclases deben implementar. Las clases abstractas son útiles para garantizar que ciertos métodos estén presentes en las clases derivadas, lo que promueve un diseño más estructurado y coherente.

#### Características de las clases abstractas

1. **No se pueden instanciar:** No puedes crear un objeto directamente de una clase abstracta.
2. **Definen métodos abstractos:** Pueden declarar métodos que deben ser implementados por las subclases.
3. **Pueden tener métodos concretos:** También pueden incluir métodos con implementación predeterminada que las subclases pueden usar o sobreescribir.

#### Módulo `abc`

Python proporciona el módulo `abc` (Abstract Base Classes) para trabajar con clases abstractas. Este módulo incluye herramientas para definir clases abstractas y métodos abstractos.

- **`ABC`:** Una clase base para definir clases abstractas.
- **`abstractmethod:`** Un decorador para declarar métodos abstractos.

#### Ejemplo básico de una clase abstracta

```python
from abc import ABC, abstractmethod

# Definimos una clase abstracta.
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass # Las subclases deben implementar este método

    def dormir(self):
        print("Zzz...") # Método concreto (opcional)

# subclase que implemente la clase abstracta
class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")

# Subclase que implementa la clase abstracta
class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")

# Uso
perro = Perro()
perro.hacer_sonido()    # Salida: ¡Guau!
perro.dormir()          # Salida:  Zzz...

gato = Gato()
gato.hacer_sonido()     # Salida: ¡Miau!

# Esto daría un error, ya que no se puede instanciar una clase abstracta
# animal = Animal()
```

#### Explicación del ejemplo

1. **Clase abstracta `Animal`:**
   - Tiene un método abstracto `hacer_sonido()`, que debe ser implementado por las subclases.
   - También tiene un método concreto `dormir()`, que las subclases pueden usar directamente o sobreescribir.
2. **Subclase `Perro` y `Gato`:**
   - Implementan el método abstracto `hacer_sonido()`.
   - Heredan el método concreto `dormir()`.
3. **Instanciación:**
   - No se puede crear un objeto de la clase `Animal` porque es abstracta.
   - Solo se pueden crear objetos de las subclases que implementan todos los métodos abstractos.

#### Métodos abstractos y concretos

- **Métodos abstractos:** Son declarados con el decorador `@abstractmethod` y no tienen implementación en la clase abstracta. Las subclases deben proporcionar una implementación.
- **Métodos concretos:** Tienen una implementación en la clase abstracta y pueden ser usados directamente por las subclases o sobreescribir.

#### ¿Por qué usar clases abstractas?

1. **Forzar la implementación de métodos:** Asegura que todas las subclases implementen ciertos métodos.
2. **Definir una interfaz común:** Proporciona un contrato que las subclases deben cumplir.
3. **Evitar in instanciación directa:** Impide que se creen objetos de una clase que no está diseñada para ser usada directamente.
4. **Promover la reutilización de código:** Los métodos concretos pueden ser reutilizados por las subclases.

#### Ejemplo avanzado: Clase abstracta con propiedades

Las clases abstractas también pueden definir propiedades abstractas usando el decorador `@abstractmethod` junto con `@property`.

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @property
    @abstractmethod
    def area(self):
        pass  # Las subclases deben implementar esta propiedad

    @property
    @abstractmethod
    def perimetro(self):
        pass  # Las subclases deben implementar esta propiedad

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    @property
    def area(self):
        return self.lado * self.lado

    @property
    def perimetro(self):
        return 4 * self.lado

# Uso
cuadrado = Cuadrado(5)
print(cuadrado.area)      # Salida: 25
print(cuadrado.perimetro) # Salida: 20
```

#### Resumen

- Las clases abstractas son clases que no se pueden instanciar directamente.
- Se usan para definir una interfaz común y garantizar que las subclases implementen ciertos métodos.
- En Python, se implementan usando el módulo `abc` y los decoradores `@abstractmethod` y `ABC`.
- Son útiles para diseñar jerarquías de clases bien estructuradas y evitar la duplicación de código.

![img.png](/screenshot/clases_abstractas/img.png)

