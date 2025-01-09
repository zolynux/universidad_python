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
