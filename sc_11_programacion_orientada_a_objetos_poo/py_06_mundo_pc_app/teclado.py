from dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f"ID: {self.id_teclado}, Marca: {self.marca}, Tipo Entrada: {self.tipo_entrada}"


# Código principal
if __name__ == "__main__":
    teclado1 = Teclado("HP", "Bluetooth")
    print(teclado1)
    teclado2 = Teclado("Gamer", "USB")
