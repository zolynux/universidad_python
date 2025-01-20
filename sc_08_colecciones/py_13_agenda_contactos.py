print("*** Agenda de contactos ***")

agenda = {
    "Carlos": {
        "telefono": "34235435",
        "email": "carlos@mail.com",
        "direccion": "Calle Principal 132",
    },
    "María": {
        "telefono": "4353344",
        "email": "maria@mail.com",
        "direccion": "Avenida Central 453",
    },
    "Pedro": {
        "telefono": "4334344",
        "email": "pedro@mail.com",
        "direccion": "Plaza Mayor 898",
    },
}

print(agenda)

# Acceder a la información de un contacto en especifico
print(
    f"""Información del contacto de María:
Teléfono: {agenda['María']['telefono']}
Email: {agenda.get('María').get('email')}
Dirección: {agenda.get('María').get('direccion')}
"""
)

# Agregar un nuevo contacto
agenda["Ana"] = {
    "telefono": "453563443",
    "email": "ana@mail.com",
    "direccion": "Calle Salvador Diaz 321",
}

print(agenda)

# Eliminar un contacto existente
agenda.pop("Pedro")
# del agenda["Pedro"]
print(agenda)

# Mostramos los contactos de la agenda
# Usar iterable
print()
print("Contactos en la agena".center(35, "="))
for nombre, detalles in agenda.items():
    print(
        f"""
{'='*50}
Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}"""
    )
