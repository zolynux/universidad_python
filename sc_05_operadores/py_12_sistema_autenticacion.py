print("*** Sistema Autenticación ***")

USUARIO_VALIDO = "admin"
PASSWORD_VALIDO = "123"
usuario = input("¿Cuál es tu usuario?: ")
password = input("¿Cuál es tu contraseña?: ")

valido = usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO

print(f"¿Datos correctos?: {valido}")
