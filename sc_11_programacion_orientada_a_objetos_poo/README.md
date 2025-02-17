# Programación Orientada a Objetos (POO)

## Programación Orientada a Objetos (POO)

La **Programación Orientada a Objetos (POO)** es un paradigma de programación que organiza el código en estructuras
llamadas **objetos**, los cuales contienen **atributos** (datos) y **métodos** (funciones). Python es un lenguaje que
soporta POO de manera nativa.

### Herencia en Python

La **herencia** en Python es un concepto de la Programación Orientada a Objetos (POO) que permite que una clase (llamada
**clase hija** o **subclase**) herede atributos y métodos de otra clase (llamada **clase padre** o **superclase**). Esto
facilita la reutilización de código y la creación de jerarquías de clases.

- **Clase padre:** Contiene los atributos y métodos compartidos.
- **Clase hija:** Hereda de la clase padre y puede agregar o modificar funcionalidades específicas.
- **Sintaxis:**

  ```python
  class ClasePadre:
    pass
  
  class ClaseHija(ClasePadre):
    pass
  ```

- Permite extender o especializar comportamientos sin duplicar código.

**📄 Código :**

```python
class Animal:
    def comer(self):
        print("Como muchas veces el día")

    def dormir(self):
        print("Duermo muchas horas")


class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo lagdrar")


# Programa Principal
print("*** Ejemplo de Herencia en Python ***")
print("Clase Padre, soy un Animal")

animal1 = Animal()
animal1.comer()
animal1.dormir()

print("\nClase Hija, soy un Perro")
perro1 = Perro()
perro1.hacer_sonido()
perro1.dormir()
perro1.comer()

```

**🟢 Ejecutar:**

```console
*** Ejemplo de Herencia en Python ***
Clase Padre, soy un Animal
Como muchas veces el día
Duermo muchas horas

Clase Hija, soy un Perro
Puedo lagdrar
Duermo muchas horas
Como muchas veces el día
```

### Sobreescritura en Python

La **sobreescritura de métodos** en Python permite que una subclase proporcione una implementación específica de un
método que ya está definido en su superclase. Esto es fundamental en la programación orientada a objetos para
personalizar o extender comportamientos heredados.

**Conceptos Clave:**

- **Definición:** La sobreescritura ocurre cuando una subclase define un método con el mismo nombre que uno en su
  superclase, alterando o ampliando su funcionalidad.

- **Uso del método `super()`:** Dentro de la subclase, se puede invocar el método de la superclase utilizando
  `super().metodo()`. Esto es útil para mantener el comportamiento original y añadir nuevas funcionalidades.

**Ejemplo Práctico:**

```python
class Animal:
    def mover(self):
        print("El animal se mueve")


class Pajaro(Animal):
    def mover(self):
        super().mover()
        print("El pájaro vuela")


# Crear instancia de Pajaro
ave = Pajaro()
ave.mover()
```

**Salida:**

```
El animal se mueve
El pájaro vuela
```

En este ejemplo, la clase `Pajaro` hereda de `Animal` y sobreescribe el método `mover`. Al llamar a `mover` desde una
instancia de `Pajaro`, primero se ejecuta el método de la superclase gracias a `super().mover()`, y luego la
implementación específica de `Pajaro`.

**Consideraciones:**

- **Acceso al método original:** Si no se utiliza `super()`, la implementación de la superclase no se ejecutará cuando
  se llame al método sobreescrito desde la subclase.

- **Compatibilidad:** Es recomendable que la firma del método sobreescrito en la subclase coincida con la de la
  superclase para evitar errores y mantener la coherencia.

La sobreescritura de métodos es esencial para adaptar y extender comportamientos en jerarquías de clases, permitiendo
que las subclases implementen funcionalidades específicas sin alterar el código de las superclases.

![img.png](/screenshot/poo/img.png)

**📄 Código :**

```python
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
perro1.dormir()  # Se llama el método sobreescrito  de la clase hija
perro1.comer()

```

**🟢 Ejecutar:**

```console
*** Ejemplo de Sobreescritura en Python ***
Clase Padre, soy un Animal
Como muchas veces el día
Duermo muchas horas

Clase Hija, soy un Perro
Puedo lagdrar
Duermo 15 Horas al día
Como muchas veces el día
```

### Polimorfismo

El polimorfismo es un concepto fundamental en la Programación Orientada a Objetos (POO) que permite que una misma
interfaz o función se comporte de diferentes maneras según el objeto que la invoque. En Python, el polimorfismo se
manifiesta a través de la capacidad de usar un mismo método o función en distintos objetos, obteniendo resultados
específicos según la clase a la que pertenezcan.

**Ejemplos de polimorfismo en Python:**

- **Funciones incorporadas polimórficas:**
  - La función `len()` puede aplicarse tanto a cadenas como a listas, devolviendo la longitud correspondiente en cada
      caso.
    - `len("Hola")` devuelve `4`.
    - `len([1, 2, 3])` devuelve `3`.

- **Operadores polimórficos:**
  - El operador `+` se utiliza para sumar números y para concatenar cadenas.
    - `5 + 3` resulta en `8`.
    - `"Hola" + " Mundo"` resulta en `"Hola Mundo"`.

**Polimorfismo con métodos de clase:**

En Python, diferentes clases pueden tener métodos con el mismo nombre, y la ejecución del método dependerá del objeto
que lo invoque.

```python
class Perro:
    def hacer_sonido(self):
        print("Guau")


class Gato:
    def hacer_sonido(self):
        print("Miau")


def emitir_sonido(animal):
    animal.hacer_sonido()


perro = Perro()
gato = Gato()

emitir_sonido(perro)  # Salida: Guau
emitir_sonido(gato)  # Salida: Miau
```

En este ejemplo, la función `emitir_sonido` acepta cualquier objeto que tenga un método `hacer_sonido`, demostrando el
polimorfismo al invocar el método correspondiente según el objeto proporcionado.

**Polimorfismo y herencia:**

El polimorfismo también se relaciona con la herencia, donde una clase derivada puede sobrescribir métodos de su clase
base.

```python
class Ave:
    def volar(self):
        print("La mayoría de las aves pueden volar")


class Pinguino(Ave):
    def volar(self):
        print("Los pingüinos no pueden volar")


def describir_vuelo(ave):
    ave.volar()


ave = Ave()
pinguino = Pinguino()

describir_vuelo(ave)  # Salida: La mayoría de las aves pueden volar
describir_vuelo(pinguino)  # Salida: Los pingüinos no pueden volar
```

Aquí, la clase `Pinguino` sobrescribe el método `volar` de la clase `Ave`, y la función `describir_vuelo` demuestra el
polimorfismo al llamar al método adecuado según el objeto.

El polimorfismo en Python permite escribir código más flexible y reutilizable, facilitando la interacción con diferentes
tipos de objetos de manera uniforme.

![img_1.png](/screenshot/poo/img_1.png)

**📄 Código :**

```python
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

```

**🟢 Ejecutar:**

```console
*** Ejemplo Polimorfismo ***
Clase Padre - Animal:
Hago un pitido

Clase hija - Perro:
Puedo ladrar

Clase hija - Gato:
Puedo maullar
```

### Duck Typing en Python

El **Duck Typing** es un concepto fundamental en Python que se basa en la idea de que el tipo o la clase de un objeto es
menos importante que los métodos o atributos que posee. Esta filosofía se resume en la expresión: "Si algo camina como
un pato y suena como un pato, entonces probablemente sea un pato".

**Características principales:**

- **Tipado dinámico:** Python no requiere la declaración explícita de tipos; el intérprete determina el tipo de las
  variables en tiempo de ejecución.

- **Enfoque en comportamientos:** Lo relevante es si un objeto puede realizar ciertas acciones, independientemente de su
  tipo específico.

**Ejemplo de Duck Typing:**

```python
class Pato:
    def hablar(self):
        print("Cuac, cuac")


class Ganso:
    def hablar(self):
        print("Honk, honk")


def hacer_sonar(ave):
    ave.hablar()


pato = Pato()
ganso = Ganso()

hacer_sonar(pato)  # Imprime "Cuac, cuac"
hacer_sonar(ganso)  # Imprime "Honk, honk"
```

En este ejemplo, la función `hacer_sonar` acepta cualquier objeto que tenga un método `hablar`, sin importar su clase.
Esto demuestra cómo Python utiliza el Duck Typing para permitir una programación más flexible y genérica.

**Ventajas del Duck Typing:**

- **Flexibilidad:** Permite escribir código que puede trabajar con diferentes tipos de objetos, siempre que estos
  implementen los métodos o atributos esperados.

- **Menor acoplamiento:** Reduce la dependencia de tipos específicos, facilitando la reutilización y mantenimiento del
  código.

- **Código más limpio:** Al no requerir comprobaciones explícitas de tipos, el código es más legible y conciso.

**Consideraciones:**

- **Manejo de errores:** Es importante asegurarse de que los objetos pasados a funciones o métodos posean los métodos o
  atributos necesarios para evitar errores en tiempo de ejecución.

- **Legibilidad:** Aunque el Duck Typing ofrece flexibilidad, se debe tener cuidado para mantener la claridad y
  comprensión del código, especialmente en proyectos grandes o colaborativos.

En resumen, el Duck Typing es una característica poderosa de Python que promueve la escritura de código flexible y
reutilizable, centrándose en los comportamientos de los objetos más que en sus tipos específicos.

**📄 Código :**

```python
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

```

**🟢 Ejecutar:**

```console
*** Ejemplo DuckTyping ***
Clase Padre - Animal:
Hago un pitido

Clase hija - Perro:
Puedo ladrar

Clase hija - Gato:
Puedo maullar
```

### Clase `Object` en Python

En Python, la clase **`object`** es la clase base de todas las clases. Todas las clases en Python heredan directa o
indirectamente de `object`, lo que significa que es la raíz de la jerarquía de herencia. Proporciona métodos y
comportamientos básicos que están disponibles en todos los objetos.

#### Características Principales

1. **Clase Base Universal**: Si no se especifica una clase base al definir una clase, Python automáticamente hereda de
   `object`.

   ```python
   class MiClase:  # Equivalente a: class MiClase(object):
       pass
   ```

2. **Métodos Integrados**: La clase `object` define métodos comunes que pueden ser sobrescritos o utilizados por otras
   clases. Algunos de los más importantes son:
    - `__init__`: Constructor de la clase.
    - `__str__`: Devuelve una representación legible del objeto (usado por `print()`).
    - `__repr__`: Devuelve una representación formal del objeto (usado en la consola).
    - `__eq__`: Define el comportamiento de igualdad (`==`).
    - `__hash__`: Devuelve un valor hash para el objeto (usado en diccionarios y conjuntos).

3. **Herencia Implícita**: Incluso si no se especifica, todas las clases heredan de `object`.

   ```python
   class MiClase:
       pass

   print(issubclass(MiClase, object))  # Salida: True
   ```

#### Métodos Comunes de `object`

- **`__str__`**: Devuelve una cadena legible para humanos.

  ```python
  class MiClase:
      def __str__(self):
          return "Soy una instancia de MiClase"

  obj = MiClase()
  print(obj)  # Salida: Soy una instancia de MiClase
  ```

- **`__repr__`**: Devuelve una cadena que representa el objeto de manera formal.

  ```python
  class MiClase:
      def __repr__(self):
          return "MiClase()"

  obj = MiClase()
  print(repr(obj))  # Salida: MiClase()
  ```

- **`__eq__`**: Define cómo se comparan dos objetos.

  ```python
  class MiClase:
      def __init__(self, valor):
          self.valor = valor

      def __eq__(self, otro):
          return self.valor == otro.valor

  obj1 = MiClase(10)
  obj2 = MiClase(10)
  print(obj1 == obj2)  # Salida: True
  ```

- **`__hash__`**: Devuelve un valor hash para el objeto.

  ```python
  class MiClase:
      def __init__(self, valor):
          self.valor = valor

      def __hash__(self):
          return hash(self.valor)

  obj = MiClase(10)
  print(hash(obj))  # Salida: Valor hash de 10
  ```

#### Importancia de `object`

- **Base de la Jerarquía**: Todas las clases heredan de `object`, lo que garantiza que tengan métodos básicos.
- **Compatibilidad**: Proporciona una interfaz común para todos los objetos en Python.
- **Extensibilidad**: Permite personalizar el comportamiento de los objetos sobrescribiendo sus métodos.

#### Ejemplo de Uso

```python
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Objeto: {self.nombre}"


obj = MiClase("Ejemplo")
print(obj)  # Salida: Objeto: Ejemplo
```

En resumen, la clase `object` es la base de todo en Python y proporciona funcionalidades esenciales que pueden ser
extendidas o modificadas según sea necesario.

**📄 Código :**

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobrescribir el metodo __str__
    def __str__(self):
        return f"""Persona:
        Nombre = {self.nombre}
        Apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}"""


# Programa principal
print("*** Clase Object ***")
persona1 = Persona("Ana", "Martinez")
print(persona1)  # El metodo __str__ se llama automaticamente desde print
# print(persona1.__str__()) # Esto es opcional

```

**🟢 Ejecutar:**

```console
*** Clase Object ***
Persona:
        Nombre = Ana
        Apellido = Martinez
        Dir. mem. <__main__.Persona object at 0x000002849C324EC0>
```

### Mundo PC

La imagen representa un diagrama de clases en Programación Orientada a Objetos (POO) con Python. Se observan varias
clases relacionadas con la gestión de computadoras y sus componentes, organizadas mediante relaciones de agregación y
herencia.

### **Análisis del Diagrama**

1. **Clases principales**
    - `Computadora`: Contiene atributos como `id_computadora`, `nombre`, `monitor`, `teclado` y `raton`. Está
      relacionada con `Monitor`, `Teclado` y `Raton` mediante agregación.
    - `Orden`: Contiene un `id_ordenes` y una lista de `Computadoras`, con un método `agregar_computadora()`.

2. **Componentes de la Computadora**
    - `Monitor`: Tiene atributos `id_monitor`, `marca` y `tamaño`, y métodos `__init__()` y `__str__()`.
    - `Raton` y `Teclado` heredan de `DispositivoEntrada`, que define atributos `marca` y `tipo_entrada`.

3. **Relaciones**
    - **Agregación**: `Computadora` se compone de `Monitor`, `Teclado` y `Raton`, lo que indica que estos objetos pueden
      existir independientemente.
    - **Herencia**: `Raton` y `Teclado` heredan de `DispositivoEntrada`, lo que sugiere reutilización de código.

Este diagrama representa una implementación de POO en Python para modelar un sistema de gestión de computadoras, con
clases bien estructuradas y relaciones claras.

![img_2.png](/screenshot/poo/img_2.png)

**📄 Código :**

**Dispositivo Entrada:**

```python
class DispositivoEntrada:
    # Constructor
    def __init__(self, marca, tipo_entrada):
        self.marca = marca
        self.tipo_entrada = tipo_entrada

```

**Clase Ratón:**

```python
from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f"Id: {self.id_raton}, Marca: {self.marca}, Tipo Entrada: {self.tipo_entrada}"


# Codigo principal
if __name__ == "__main__":
    raton1 = Raton("HP", "USB")
    print(raton1)
    raton2 = Raton("Acer", "Bluetooth")
    print(raton2)

```

**Clase Teclado:**

```python
from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f"ID: {self.id_teclado}, Marca: {self.marca}, Tipo Entrada: {self.tipo_entrada}"


# Código principal
if __name__ == "__main__":
    teclado1 = Teclado("HP", "Bluetooth")
    print(teclado1)
    teclado2 = Teclado("Gamer", "USB")

```

**Clase Monitor:**

```python
class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return f"ID: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamanio}"


if __name__ == "__main__":
    monitor1 = Monitor("HP", 15)
    print(monitor1)
    monitor2 = Monitor("Dell", 27)
    print(monitor2)

```

**Clase Computadora:**

```python
from teclado import Teclado
from monitor import Monitor
from raton import Raton


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f"""{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Ratón: {self.raton}
        """


if __name__ == "__main__":
    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("HP", "USB")
    monitor1 = Monitor("HP", 27)
    computadora1 = Computadora("HP", monitor1, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado("Gamer", "Bluetooth")
    raton2 = Raton("Gamer", "Bluetooth")
    monitor2 = Monitor("Gamer", 34)
    computadora2 = Computadora("Gamer", monitor2, teclado2, raton2)
    print(computadora2)

```

**Clase Orden:**

```python
class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        # Recibimos la lista de objetos de tipo computadora
        self.computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for computadora in self.computadoras:
            computadoras_str += "\n" + computadora.__str__()
        return f"""Orden: {self.id_orden}
        Computadoras: {computadoras_str}"""

```

**Mundo PC *App*:**

```python
from computadora import Computadora
from monitor import Monitor
from teclado import Teclado
from raton import Raton
from orden import Orden

print("*** Mundo PC ***")

# Computadora 1

teclado1 = Teclado("HP", "USB")
raton1 = Raton("HP", "USB")
monitor1 = Monitor("HP", 27)
computadora1 = Computadora("HP", monitor1, teclado1, raton1)

# Computadora 2
teclado2 = Teclado("Gamer", "Bluetooth")
raton2 = Raton("Gamer", "Bluetooth")
monitor2 = Monitor("Gamer", 34)
computadora2 = Computadora("Gamer", monitor2, teclado2, raton2)

# crear la lista de computadora
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
# print(orden1)

# Computadora 3
teclado3 = Teclado("Dell", "Bluetooth")
raton3 = Raton("Dell", "Bluetooth")
monitor3 = Monitor("Dell", 27)
computadora3 = Computadora("Dell", monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)

```

**🟢 Ejecutar:**

```console

*** Mundo PC ***
Orden: 1
        Computadoras: 
HP: 1
        Monitor: ID: 1, Marca: HP, Tamaño: 27
        Teclado: ID: 1, Marca: HP, Tipo Entrada: USB
        Ratón: Id: 1, Marca: HP, Tipo Entrada: USB
        
Gamer: 2
        Monitor: ID: 2, Marca: Gamer, Tamaño: 34
        Teclado: ID: 2, Marca: Gamer, Tipo Entrada: Bluetooth
        Ratón: Id: 2, Marca: Gamer, Tipo Entrada: Bluetooth
        
Dell: 3
        Monitor: ID: 3, Marca: Dell, Tamaño: 27
        Teclado: ID: 3, Marca: Dell, Tipo Entrada: Bluetooth
        Ratón: Id: 3, Marca: Dell, Tipo Entrada: Bluetooth
```
