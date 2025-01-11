from random import randint

print("*** Sistema Generador de ID Único ***")

nombre = str(input('¿Cuál es tu nombre?: '))
apellido = str(input('¿Cuál es tu apellido?: '))
anio_nacimiento = str(input('¿Cuál es tu año de nacimiento (YYYY)?: '))


# Normalizar los valores

nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:] # También puede ser [2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el valorr de id único
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}'

print(f'''\nHola {nombre},
      Tu nuevo número de identificación (ID) generador por el sistema es:
      {id_unico}
¡Felicitaciones!''')