print("*** Bienvenido a la casa de los espejos ***")

edad = int(input("¿Cuál es tu edad?: "))
tienes_miedo_oscuridad = input("¿Tienes miedo a la oscuridad (Si/No)?: ")
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower() == "si"

if not tienes_miedo_oscuridad and edad >= 10:
    print("Puedes entrar a la casa de los espejos")
else:
    print("Lo siento, la casa de los espejos podría darte miedo")
