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
implementación específica de `Pajaro`. citeturn0search2

**Consideraciones:**

- **Acceso al método original:** Si no se utiliza `super()`, la implementación de la superclase no se ejecutará cuando
  se llame al método sobreescrito desde la subclase.

- **Compatibilidad:** Es recomendable que la firma del método sobreescrito en la subclase coincida con la de la
  superclase para evitar errores y mantener la coherencia.

La sobreescritura de métodos es esencial para adaptar y extender comportamientos en jerarquías de clases, permitiendo
que las subclases implementen funcionalidades específicas sin alterar el código de las superclases.

![img.png](img.png)

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
