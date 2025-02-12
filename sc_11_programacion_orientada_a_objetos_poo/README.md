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
