print("*** Función par ***")


# Función para saber si un número es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# LLamamos a la función
if __name__ == "__main__":
    numero = int(input("Proporciona un valor numérico: "))
    print("¿Número par?:", es_par(numero))
