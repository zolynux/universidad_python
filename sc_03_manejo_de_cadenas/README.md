# Manejo de Cadenas

Una cadena o string en inglés es un tipo de dato que se utiliza para almacenar una secuencia de caracteres

Las cadenas se deben encerrar entra comillas dobles o comillas simples.

Los caracteres pueden ser letras, números, símbolos o espacios.

```python
# Cadenas en Python
cadena1 = "Hola Mundo"
```

![img_3.png](/screenshot/img_3.png)

**Código 📄:**

```python
# Cadenas en Python
cadena1 = "Hola Mundo"
cadena1 = "Adiós"
cadena2 = "Python es Genial"
cadena3 = """Este es un ejemplo
de múltiples líneas
en una cadena"""

print(cadena1)
print(cadena2)
print(cadena3)
```

**🟢 Ejecutar:**

```console
Adiós
Python es Genial
Este es un ejemplo
de múltiples líneas
en una cadena
```

## Detalle de una Cadena

Los caracteres de una cadena están indexados de manera secuencial.

Por lo tanto, podemos acceder cada carácter indicando el índice del carácter que deseamos recuperar

![img_4.png](/screenshot/img_4.png)

**📄 Código :**

```python
# Manejo de índice en una cadena
cadena1 = "Hola Mundo"
print(cadena1)
# Recuperara el primer caracter
primer_caracter = cadena1[0]  # recuperar 'H'
print(primer_caracter)
ultimo_caracter = cadena1[9]  # recuperar 'o'
print(ultimo_caracter)
```

**🟢 Ejecutar:**

```console
Hola Mundo
H
o
```

## Inmutabilidad de una Cadena

Una vez que se crea una cadena, los caracteres dentro de ella no pueden ser modificados

Si deseamos modificar una cadena, entonces tenemos que crear una nueva cadena.

Las cadenas no se pueden modificar, son inmutables:

![img_5.png](/screenshot/img_5.png)

Nuevo valor.

**📄 Código :**

```python
# Inmutabilidad en cadenas
cadena1 = "Hola Mundo"
# cadena1 [0] = 'h' # no podemos modificar los carateres
cadena2 = cadena1
cadena1 = "Adios"
print(cadena1)
print(cadena2)
```

**🟢 Ejecutar:**

```console
Adios
Hola Mundo
```

## Caractéres Especiales

Las cadenas pueden incluir caractéres especiales

Estos caracteres se introducen usando el caracter de diagonal invertida (`\`). Ejemplo:

- **Nueva línea: `\n`** Inserta un salto de línea
- **Tabulación: `\t`** Inserta un tabulador horizontal, útil para alinear texto.
- **Comillas Simple: `\'`** Permite incluir comillas Simples en una cadena delimitada por comillas simples.
- **Comillas Doble: `\"`** Permite incluir comillas Dobles en una cadena delimitada por comillas simples.
- **Barra invertida:  `\\`** Permite incluir una barra invertida en la cadena

Existen más caracteres especiales, pero esto son los esenciales.

**📄 Código :**

```python
# Caracteres Especiales
print("Hola \nMundo")  # \n salto de linea
print("\t\tPython \t\tes genial")  # \t agrega un tabulador
print("Juan ' \"Perez")
print('Karla " Gomez')
print("Caracter \\ diagonal invertida")
```

**🟢 Ejecutar:**

```console
Hola 
Mundo
    Python 		es genial
Juan ' "Perez
Karla " Gomez
Caracter \ diagonal invertida
```

## Concatenación de Cadenas

La concatenación de cadenas es una operación que permite combinar dos o más cadenas para formar una nueva cadena.

En python existen varias formas, vamos a ver varias.

- **Uso del operador +:** El operador `+` es el más directo para concatenar. Simplemente, tenemos que poner el operador
  `+` entre las cadenas que deseamos unir.

**Ejemplo:**

```python
concatenacion = "Hola" + "Mundo"
```

- **Uso de la función `join`:** La función `join` nos permite unir tantas cadenas como necesitemos. Solo necesitamos
  pasar cada cadena a concatenar separadas por coma y entre paréntesis.

**Ejemplo:**

```python
"".join(["cadena1", "cadena2", "cadena3"])
```

--

**📄 Código :**

```python
# Concatenación de Cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = cadena1 + " " + cadena2

print(concatenacion)

# Utilizando el metodo join

concatenacion = "".join([cadena1, " ", cadena2])
print(concatenacion)
```

**🟢 Ejecutar:**

```console
Hola Mundo
Hola Mundo
```

## Formateo de Cadenas

Python ofrece varias maneras de formatear cadenas, que incluyen la capacidad de concatenar texto, variables e incluso
dar indicar el número de decimales a utilizar en el formato.

- **f-string (Python 3.6+)**: Esta es la opción más recomendada, por ser la más sencilla, rápida y legible.

```python
resultado = f'hola {variable}'
```

- **Método format** Es muy versátil y poderoso permite construir cadenas muy complejas.

```python
resultado = 'Hola {}'.format(variable)
```

## Métodos de cadenas

Las cadenas en Python vienen con una serie de métodos útiles que facilitan su manipulación. Por ejemplo:

- `upper()` -> Cambiar las letras a mayúsculas.
- `lower()` -> Cambiar las letras a minúsculas.
- `strip()` -> Elimina espacios en blanco al inicio y al final de la cadena

**📄 Código :**

```python
# Método de cadenas

cadena1 = 'Hola Mundo'
print(f'Cadena original: {cadena1}')
mayusculas = cadena1.upper()  # Convertir a mayúsculas
print(f'Cadena en mayúsculas: {mayusculas}')
print(f'Cadena en minúsculas: {cadena1.lower()}')  # Convertir a minúsculas
cadena2 = ' Juan Perez '
print(f'Cadena con espacios: {cadena2}')
print(f'Cadena sin espacios: {cadena2.strip()}')  # Eliminar espacio al inicio y al final
```

**🟢 Ejecutar:**

```console
Cadena original: Hola Mundo
Cadena en mayúsculas: HOLA MUNDO
Cadena en minúsculas: hola mundo
Cadena con espacios:  Juan Perez 
Cadena sin espacios: Juan Perez
```

## Largo de una cadena

**Obtener el largo de una cadena:**

Para obtener la longitud de una cadena, utilizamos la función incorporada `len()`

La función `len` funciona con varios tipos de datos incluyendo cadenas, listas, etc.

Cuando se calcula el largo de una cadena se toman en cuenta todos los caracteres de una cena, incluyendo espacios en
blanco, caracteres especiales, etc.

````python
cadena1 = 'Hola, Mundo!'
longitud = len(cadena1)  # -> devuelve largo de 12
````

**📄 Código :**

```python
# Largo de una cadena
cadena = "Hola, mundo!"
largo_cadena = len(cadena)
print(f"Cadena original: {cadena}")
print(f"Largo de la cadena: {largo_cadena}")
```

**🟢 Ejecutar:**

```console
Cadena original: Hola, mundo!
Largo de la cadena: 12
```

## Subcadenas

Una subcadena es una parte de una cadena principal, y hay varias maneras de extraer subcadenas en Python

Podemos extraer subcadenas, buscarlas, reemplazarlas, entre otras operaciones.

- **Extracción cadenas (Slicing):** El slicing o segmentación permite indicar el índice de inicio y el índice final (sin
  incluir este último caracter)

```python
subcadena = cadena[inicio:fin]
```

**📄 Código :**

```python
# Manejo de subcadenas
cadena = "Hola, Mundo!"
# Obtenemos la subcadena de hola[inicio:fin (sin incluirlo)]
subcadena_hola = cadena[0:4]
print(f"Subcadena de hola: {subcadena_hola}")
# Obtene la subcadena de mundo
subcadena_mundo = cadena[6:11]
print(f"Subcadena de mundo: {subcadena_mundo}")
```

**🟢 Ejecutar:**

```console
Subcadena de hola: Hola
Subcadena de mundo: Mundo
```

## Búsqueda de subcadenas

- **Buscar subcadenas (`find`):** El método `find()` devuelve el índice de la primera aparición de la subcadena. Si no
  encuentra la subcadena, devuelve -1

```python
cadena = 'Hola Mundo'
posicion = cadena.find("Mundo")
print(posicion)  # Imprime 5
```

**📄 Código :**

```python
# Buscar subcadenas
cadena = "Hola, mundo"
indice = cadena.find("mundo")
print(f"Indice de la subcadena mundo: {indice}")
# Obtener el indicie de la subcadena de Hola
indice = cadena.find("Hola")
print(f"Indice la subcadena de Hola: {indice}")
```

**🟢 Ejecutar:**

```console
Indice de la subcadena mundo: 6
Indice la subcadena de Hola: 0
```

## Reemplazar subcadena

- **Reemplazar subcadena (`replace`)** El método `replace()` reemplaza una subcadena por otra dentro de una cadena
  principal

```python
cadena = 'Hola mundo'
nueva_cadena = cadena.replace('mundo', 'a todos')
print(nueva_cadena)  # 'Hola a todos'
```

**📄 Código :**

```python
# Reemplazar subcadenas
cadena = 'Hola, mundo!'
print(f'Cadena original: {cadena}')
nueva_cadena = cadena.replace('mundo', 'a todos')
print(f'Nueva cadena reemplazada:  {nueva_cadena}')
# Sustituir hola por adios
nueva_cadena = cadena.replace('Hola', 'Adiós')
print(f'Nueva cadena reemplazada: {nueva_cadena}')
```

**🟢 Ejecutar:**

```console
Cadena original: Hola, mundo!
Nueva cadena reemplazada:  Hola, a todos!
Nueva cadena reemplazada: Adiós, mundo!
```

## Separar en Subcadenas

- **Extraer subcadenas por separadores (`split`):** La función `split()` permite dividir una cadena en una lista de
  subcadenas basadas en un caracter separador.

**Ejemplo:**

```python
datos = 'Juan, 30, Colombia'
lista = datos.split(',')
print(lista)  # ['Juan', '30', 'Colombia']
```

**📄 Código :**

```python
# Separar cadenas (split)
datos = "Hola Mundo"
lista = datos.split()  # Por defualt separa cada elemento por espacios en blanco
print(lista)

datos = "Juan,30,Colombia"
lista = datos.split(",")
print(lista)
```

**🟢 Ejecutar:**

```console
['Hola', 'Mundo']
['Juan', '30', 'Colombia']
```

## Multiplicación de cadenas

**📄 Código :**

```python
print("*** Multiplicación de Cadenas ***")

texto = "Hola"
veces = 4

resultado = texto * veces
print(resultado)
```

**🟢 Ejecutar:**

```console
*** Multiplicación de Cadenas ***
HolaHolaHolaHola
```

## Generador de Email

Crea un programa para generar un email a partir de los siguientes datos:

- **Nombre:** Ubaldo Acosta Soto
- **Empresa:** Global Mentoring
- **Dominio:** com.mx

Resultado Final:

**Email:** `ubaldo.acosta.soto@globalmentoring.com.mx`

Este es el resultado del programa:

```console
*** Generador de Email ***
Nombre Usuario: Ubaldo Acosta Soto
Nombre Usuario normalizado: ubaldo.acosta.soto

Nombre Empresa: Global Mentoring
Extensión del dominio: com.mx
Dominio de email normalizado: @globalmentoringcom.mx  

Email final generado: ubaldo.acosta.soto@globalmentoringcom.mx
```

**📄 Código :**

```python
# Generador de Email
print("*** Generador de Email ***")

nombre_completo = "Ubaldo Acosta Soto"
print(f"Nombre Usuario: {nombre_completo}")
nombre_normalizado = nombre_completo.strip().lower().replace(" ", ".")
print(f"Nombre Usuario normalizado: {nombre_normalizado}")
print()
empresa = "Global Mentoring"
print(f"Nombre Empresa: {empresa}")
empresa_normalizado = empresa.strip().lower().replace(" ", "")
dominio = "com.mx"
print(f"Extensión del dominio: {dominio}")
dominio_email = "".join(["@", empresa_normalizado, dominio])
print(f"Dominio de email normalizado: {dominio_email}")
print()
print(f"Email final generado: {nombre_normalizado + dominio_email}")
```

**🟢 Ejecutar:**

```console
*** Generador de Email ***
Nombre Usuario: Ubaldo Acosta Soto
Nombre Usuario normalizado: ubaldo.acosta.soto

Nombre Empresa: Global Mentoring
Extensión del dominio: com.mx
Dominio de email normalizado: @globalmentoringcom.mx  

Email final generado: ubaldo.acosta.soto@globalmentoringcom.mx
```
