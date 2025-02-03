# Clases y Objetos

## Clases y Objetos

Python es un lenguaje orientado a objetos.
Un objeto es una representación de una entidad de la vida real en nuestro programa.
Para crear un objeto primero necesitamos crear una clase o plantilla.
Una clase representa las características en común de nuestros objetos. Es una abstracción.
Por ejemplo, si queremos construir un edificio, primero necesitamos su plano, es decir, una clase o plantilla, y a
partir de ese plano, podemos generar muchos edificios similares, es decir, los objetos

### Elementos de una Clase

Una clase se compone de atributos y métodos.
Los atributos son las características de nuestros objetos.

Los métodos son las acciones que pueden realizar nuestros objetos. En sí, estas acciones son funciones, pero cuando se
asocian con una clase se les llama métodos.

Una vez que hemos definido nuestra clase, podemos crear objetos, a esto se le llama instancia una clase.

![img.png](img.png)

**📄 Código :**

```python
# Definición de una clase
class Persona:
    def inicializar_persona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(
            f"""Persona:
    Nombre: {self.nombre}
    Apellido: {self.apellido}"""
        )


# Creación de objetos
if __name__ == "__main__":
    # Creación de un primer objeto
    persona1 = Persona()  # Crea un objeto vacio en memoria
    persona1.inicializar_persona("Layla", "Acosta")
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona()  # Crea un objeto vacío en memoria
    persona2.inicializar_persona("Ian", "Sánchez")
    persona2.mostrar_persona()

```

**🟢 Ejecutar:**

```console
Persona:
    Nombre: Layla
    Apellido: Acosta
Persona:
    Nombre: Ian
    Apellido: Sánchez
```

### Constructores

Un constructor es un método especial y se utiliza para crear un objeto, o instancia una clase.

Además, nos puede servir para crear e inicializar los atributos de un nuevo objeto.

````python
# Sintaxis de un constructor
class NombreDeLaClase:
    # __init()__ -> El método init se conoce como un método mágico o de tipo dunder (double underscore)
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
````

````python
# Ejemplo de un contructor
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
````

**📄 Código :**

```python
# Definición de una clase
class Persona:
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(
            f"""Persona:
    Nombre: {self.nombre}
    Apellido: {self.apellido}"""
        )


# Creación de objetos
if __name__ == "__main__":
    # Creación de un primer objeto
    persona1 = Persona("Layla", "Acosta")  # Crea un objeto vacio en memoria
    # persona1.inicializar_persona("Layla", "Acosta")
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona("Ian", "Sánchez")  # Crea un objeto vacío en memoria
    # persona2.inicializar_persona("Ian", "Sánchez")
    persona2.mostrar_persona()

```

**🟢 Ejecutar:**

```console
Persona:
    Nombre: Layla
    Apellido: Acosta
Persona:
    Nombre: Ian
    Apellido: Sánchez
```

### Dirección de Memoria de Objetos

La dirección de memoria de un objeto en Python es un identificador único que permite acceder y gestionar su ubicación en
la memoria.

**📄 Código :**

```python
# Definición de una clase
class Persona:
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(
            f"""Persona:
    Nombre: {self.nombre}
    Apellido: {self.apellido}"""
        )
        print(f"Dir. mem self: {id(self)}")
        print(f"Dir. mem hex self: {hex(id(self))}")


# Creación de objetos
if __name__ == "__main__":
    # Creación de un primer objeto
    persona1 = Persona("Layla", "Acosta")  # Crea un objeto vacio en memoria
    persona1.mostrar_persona()
    print(f"Dir. mem persona1: {id(persona1)}")
    print(f"Dir. mem hex persona1: {hex(id(persona1))}")

    # Creamos un segundo objeto
    persona2 = Persona("Ian", "Sánchez")  # Crea un objeto vacío en memoria
    persona2.mostrar_persona()
    print(f"Dir. mem persona2: {id(persona2)}")
    print(f"Dir. mem hex persona2: {hex(id(persona2))}")

```

**🟢 Ejecutar:**

```console
Persona:
    Nombre: Layla
    Apellido: Acosta
Dir. mem self: 2035009539776
Dir. mem hex self: 0x1d9d0054ec0
Dir. mem persona1: 2035009539776
Dir. mem hex persona1: 0x1d9d0054ec0
Persona:
    Nombre: Ian
    Apellido: Sánchez
Dir. mem self: 2035036933008
Dir. mem hex self: 0x1d9d1a74b90
Dir. mem persona2: 2035036933008
Dir. mem hex persona2: 0x1d9d1a74b90
```

### Clase Aritmética

![img_1.png](img_1.png)

**📄 Código :**

```python
class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f"Resultado de la suma: {resultado}")

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f"Resultado de la resta: {resultado}")

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f"Resultado de la multiplicación: {resultado}")

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f"Resultado de la división: {resultado}")


# Programa principal
if __name__ == "__main__":
    print("*** Ejemplo clase Aritmética ***")
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    # Segundo objeto
    aritmetica2 = Aritmetica(12, 16)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()

```

**🟢 Ejecutar:**

```console
*** Ejemplo clase Aritmética ***
Resultado de la suma: 12
Resultado de la resta: -2
Resultado de la multiplicación: 35
Resultado de la división: 0.7142857142857143

Resultado de la suma: 28
Resultado de la resta: -4
```

### Flexibilidad de Constructores

**📄 Código :**

```python
class Aritmetica:
    # Python Solamente toma el ultimo constructor
    # def __init__(self, operando1):
    #     self.operando1 = operando1

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f"Resultado de la suma: {resultado}")

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f"Resultado de la resta: {resultado}")

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f"Resultado de la multiplicación: {resultado}")

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f"Resultado de la división: {resultado}")


# Programa principal
if __name__ == "__main__":
    print("*** Ejemplo clase Aritmética ***")
    # Primer objeto
    print("Primer objeto")
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    # Segundo objeto
    print()
    print("Segundo objeto")
    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.restar()
    # Tercer Objeto
    print("Tercer Objeto")
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    aritmetica3.sumar()
    # Cuarto objeto
    print("Cuarto objeto")
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()
    # Quinto objeto
    print("Quinto objeto")
    aritmetica5 = Aritmetica(operando2=4, operando1=3)
    aritmetica5.sumar()

```

**🟢 Ejecutar:**

```console
*** Ejemplo clase Aritmética ***
Primer objeto
Resultado de la suma: 12
Resultado de la resta: -2
Resultado de la multiplicación: 35
Resultado de la división: 0.7142857142857143

Segundo objeto
Resultado de la suma: 28
Resultado de la resta: -4
Tercer Objeto
Resultado de la suma: 16
Cuarto objeto
Resultado de la suma: 10
Quinto objeto
Resultado de la suma: 7
```

### Encapsulamiento

El encapsulamiento nos permite ocultar la información que almacena un objeto, también conocido como el estado del
objeto.

Para aplicar el concepto de encapsulamiento se deben aplicar dos características:

1. **Atributos protegidos o privados**

    ````python
    self._nombre # Atributo protegido
    self.__apellido # Atributo privado
    ````

2. **Crear los métodos conocidos como `get` (leer) y `set` (modificar)**

![img_2.png](img_2.png)

**📄 Código :**

```python
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

```

**🟢 Ejecutar:**

```console
*** Encapsulamiento ***
Conduciendo el coche:
        Marca: Toyota
        Modelo: Yaris
        Color: Azul
Conduciendo el coche:
        Marca: Toyota 2
        Modelo: Yaris 2
        Color: Azul 3
```

### Métodos get y set

![img_3.png](img_3.png)

**📄 Código :**

```python
# Definimos la clase coche
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # atributo publico
        self._modelo = modelo  # Atributo Protegido
        self._color = color  # Atributo Privado

    def conducir(self):
        print(
            f"""Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}"""
        )

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


# Programa principal
if __name__ == "__main__":
    print("*** Métodos get y set ***")
    # Creación de un primer objeto coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean públicos
    coche1.set_marca("Toyota 2")
    coche1.set_modelo("Yaris 2")
    coche1.set_color("Azul 2")
    coche1.conducir()

```

**🟢 Ejecutar:**

```console
*** Métodos get y set ***
Conduciendo el coche:
        Marca: Toyota
        Modelo: Yaris
        Color: Azul
Conduciendo el coche:
        Marca: Toyota 2
        Modelo: Yaris 2
        Color: Azul 2
```

### Mejora de Encapsulamiento

**📄 Código :**

```python
# Definimos la clase coche
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # atributo publico
        self._modelo = modelo  # Atributo Protegido
        self._color = color  # Atributo Privado

    def conducir(self):
        print(
            f"""Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}"""
        )

    # def get_marca(self):
    #     return self._marca
    @property  # Definir el método get de manera más pythonica
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == "__main__":
    print("*** Mejora de Encapsulamiento ***")
    # Creación de un primer objeto coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
    # No deberíamos acceder a los atributos que no sean públicos
    coche1.marca = "Toyota 2"
    coche1.modelo = "Yaris 2"
    coche1.color = "Azul 2"
    coche1.conducir()
    # Atributo de marca del coche1
    coche1.marca = "Toyota 3"
    print(f"Atributo marcha coche1: {coche1.marca}")

```

**🟢 Ejecutar:**

```console
*** Mejora de Encapsulamiento ***
Conduciendo el coche:
        Marca: Toyota
        Modelo: Yaris
        Color: Azul
Conduciendo el coche:
        Marca: Toyota 2
        Modelo: Yaris 2
        Color: Azul 2
Atributo marcha coche1: Toyota 3
```

### Atributos dinámicos

**📄 Código :**

```python
# Definimos la clase coche
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # atributo publico
        self._modelo = modelo  # Atributo Protegido
        self._color = color  # Atributo Privado

    def conducir(self):
        print(
            f"""Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}"""
        )

    # def get_marca(self):
    #     return self._marca
    @property  # Definir el método get de manera más pythonica
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == "__main__":
    print("*** Atributos dinámicos ***")
    # Creación de un primer objeto coche
    coche1 = Coche("Toyota", "Yaris", "Azul")
    coche1.conducir()
    # No deberíamos acceder a los atributos que no sean públicos
    coche1.marca = "Toyota 2"
    coche1.modelo = "Yaris 2"
    coche1.color = "Azul 2"
    coche1.conducir()
    # Intentar agregar un nuevo atributo
    setattr(coche1, "nuevo_atributo", "valor nuevo atributo")
    coche1.nuevo_atributo2 = "Valor nuevo atributo 2"
    print(f"Atributo del coche1: {coche1.__dict__}")
    coche1.conducir()
    print(coche1.nuevo_atributo)
    print(f"Nuevo atributo coche1 {coche1.nuevo_atributo2}")
    # segundo objeto
    coche2 = Coche("Chevrolet", "Trax", "Blanco")
    coche2.conducir()
    print(f"Atributo del coche2: {coche2.__dict__}")
    # print(f"Nuevo atributo coche2 {coche2.nuevo_atributo}")
    # print(f"Nuevo atributo 2 coche2 {coche2.nuevo_atributo2}")

```

**🟢 Ejecutar:**

```console
*** Atributos dinámicos ***
Conduciendo el coche:
        Marca: Toyota
        Modelo: Yaris
        Color: Azul
Conduciendo el coche:
        Marca: Toyota 2
        Modelo: Yaris 2
        Color: Azul 2
Atributo del coche1: {'_marca': 'Toyota 2', '_modelo': 'Yaris 2', '_color': 'Azul 2', 'nuevo_atributo': 'valor nuevo atributo', 'nuevo_atributo2': 'Valor nuevo atributo 2'}
Conduciendo el coche:
        Marca: Toyota 2
        Modelo: Yaris 2
        Color: Azul 2
valor nuevo atributo
Nuevo atributo coche1 Valor nuevo atributo 2
Conduciendo el coche:
        Marca: Chevrolet
        Modelo: Trax
        Color: Blanco
Atributo del coche2: {'_marca': 'Chevrolet', '_modelo': 'Trax', '_color': 'Blanco'}

```
