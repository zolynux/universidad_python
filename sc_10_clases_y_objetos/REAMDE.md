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
