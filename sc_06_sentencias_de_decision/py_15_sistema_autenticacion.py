print("*** Sistema de Autenticación ***")

USUARIO_VALIDO = "admin"
PASSWORD_VALIDO = "123"

usuario = str(input("Ingresa tu usuario: "))
password = str(input("Ingresa tu password: "))

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print("Bienvenido al sistema")
elif usuario == USUARIO_VALIDO:
    print("password es inválido, favor de corregirlo!")
elif password == PASSWORD_VALIDO:
    print("Usuario es inválido, favor de corregirlo!")
else:
    print("usuario y password son inválidos, favor de corregirlo!")
