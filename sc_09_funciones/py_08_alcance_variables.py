print("*** Alcance de Variables ***")

# Variable global
contador_global: int = 0


def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0
    # usar la variable global
    global contador_global
    # Incrementamos la variable global
    contador_global += 1
    # Incrementamos la variable local
    contador_local += 1
    # Imprimimos ambos contadores
    print("Contador local:", contador_local)
    print("Contador global:", contador_global, "\n")


#  Llamamos varias veces la función
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print("Valor variable global:", contador_global)
