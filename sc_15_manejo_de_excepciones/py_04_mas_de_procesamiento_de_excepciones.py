resultado = None

try:
    a = int(input("Introduce un número de 'a': "))
    b = int(input("Introduce un número de 'b': "))
    resultado = a / b
except ZeroDivisionError as e:
    print(f"ZeroDivisionError - Ocurrió un error: {e}, {type(e)}")
except TypeError as e:
    print(f"TypeError - Ocurrió un error: {e}, {type(e)}")

except Exception as e:
    print(f"Exception - Ocurrió un error: {e}, {type(e)}")

print(f"Resultado: {resultado}")
print("Continua...")
