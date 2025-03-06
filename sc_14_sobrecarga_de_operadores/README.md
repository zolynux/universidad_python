## Sobrecarga de Operadores

La **sobrecarga de operadores** en Python es la capacidad de definir o cambiar el comportamiento de los operadores (como `+`, `-`, `*`, `/`, `==`, etc.) para objetos de una clase. Esto se logra implementando métodos especiales (también conocidos como "métodos mágicos" o "dunder methods") en la clase. Estos métodos tienen nombres que comienzan y terminan con doble guion bajo (`__`), como `__add__`, `__sub__`, `__eq__`, entre otros.

#### ¿Por qué es útil la sobrecarga de operadores?

La sobrecarga de operadores permite que los objetos de una clase se comporten de manera intuitiva cuando se usan con operadores estándar. Por ejemplo, puedes definir qué significa sumar dos objetos de una clase o compararlos usando `==`.

---

#### Métodos especiales comunes para sobrecarga de operadores

Aquí hay algunos de los métodos especiales más utilizados para sobrecargar operadores:

| Operador | Método especial       | Descripción                                  |
|----------|-----------------------|----------------------------------------------|
| `+`      | `__add__(self, other)`| Define el comportamiento de la suma (`+`).   |
| `-`      | `__sub__(self, other)`| Define el comportamiento de la resta (`-`).  |
| `*`      | `__mul__(self, other)`| Define el comportamiento de la multiplicación (`*`). |
| `/`      | `__truediv__(self, other)`| Define el comportamiento de la división (`/`). |
| `==`     | `__eq__(self, other)` | Define el comportamiento de la igualdad (`==`). |
| `!=`     | `__ne__(self, other)` | Define el comportamiento de la desigualdad (`!=`). |
| `<`      | `__lt__(self, other)` | Define el comportamiento de "menor que" (`<`). |
| `>`      | `__gt__(self, other)` | Define el comportamiento de "mayor que" (`>`). |
| `<=`     | `__le__(self, other)` | Define el comportamiento de "menor o igual que" (`<=`). |
| `>=`     | `__ge__(self, other)` | Define el comportamiento de "mayor o igual que" (`>=`). |
| `str()`  | `__str__(self)`       | Define la representación en cadena del objeto. |
| `len()`  | `__len__(self)`       | Define el comportamiento de la función `len()`. |

---

#### Ejemplo básico: Sobrecarga del operador `+`

Supongamos que tienes una clase `Punto` que representa un punto en un plano 2D. Puedes sobrecargar el operador `+` para sumar dos puntos:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecarga del operador +
    def __add__(self, otro):
        nuevo_x = self.x + otro.x
        nuevo_y = self.y + otro.y
        return Punto(nuevo_x, nuevo_y)

    # Representación en cadena del objeto
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

# Uso
p1 = Punto(1, 2)
p2 = Punto(3, 4)
p3 = p1 + p2  # Llama a __add__
print(p3)    # Salida: Punto(4, 6)
```

---

#### Ejemplo: Sobrecarga del operador `==`

Puedes sobrecargar el operador `==` para comparar dos objetos de la clase `Punto`:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecarga del operador ==
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

# Uso
p1 = Punto(1, 2)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(p1 == p2)  # Salida: True
print(p1 == p3)  # Salida: False
```

---

#### Ejemplo: Sobrecarga del operador `*`

Puedes sobrecargar el operador `*` para multiplicar un punto por un escalar:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecarga del operador *
    def __mul__(self, escalar):
        return Punto(self.x * escalar, self.y * escalar)

    # Representación en cadena del objeto
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

# Uso
p1 = Punto(2, 3)
p2 = p1 * 3  # Llama a __mul__
print(p2)    # Salida: Punto(6, 9)
```

---

#### Ejemplo: Sobrecarga de `__str__`

El método `__str__` define cómo se representa un objeto como una cadena cuando se usa `print()` o `str()`:

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Representación en cadena del objeto
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

# Uso
p = Punto(5, 10)
print(p)  # Salida: Punto(5, 10)
```

---

#### Ejemplo: Sobrecarga de `__len__`

El método `__len__` define el comportamiento de la función `len()`:

```python
class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    # Sobrecarga de len()
    def __len__(self):
        return len(self.elementos)

# Uso
lista = MiLista([1, 2, 3, 4, 5])
print(len(lista))  # Salida: 5
```

---

#### Resumen

- La **sobrecarga de operadores** permite definir el comportamiento de los operadores para objetos de una clase.
- Se implementa usando métodos especiales (como `__add__`, `__eq__`, `__str__`, etc.).
- Es útil para hacer que los objetos de una clase se comporten de manera intuitiva con operadores estándar.
- Algunos métodos comunes incluyen `__add__` para `+`, `__eq__` para `==`, `__str__` para `str()`, y `__len__` para `len()`.

La sobrecarga de operadores es una característica poderosa que hace que el código sea más legible y expresivo, especialmente cuando trabajas con clases que representan conceptos matemáticos o estructuras de datos.


**📄 Código :**

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        return f"{self.nombre} {otro.nombre}"

    def __sub__(self, otro):
        return self.edad - otro.edad


# obj1 + obj2
# obj1.__add__(obj2)
persona1 = Persona("Juan", 28)
persona2 = Persona("Carlos", 20)
print(persona1 + persona2)
print(persona1 - persona2)

```

**🟢 Ejecutar:**

```console
Juan Carlos
8
```
