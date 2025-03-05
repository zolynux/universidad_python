class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erroneo ancho: {ancho}")
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo alto: {alto}")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
        print(f"Valor erroneo alto: {alto}")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erroneo ancho: {ancho}")

    def __str__(self):
        return f"FiguraGeometrica [ Alto: {self.alto}, Ancho: {self.ancho} ]"

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
