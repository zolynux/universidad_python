class Aritmetica:
    def __init__(self, operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f"Resultado de la suma: {resultado}")

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f"Resultado de la resta: {resultado}")

    def multiplicar(self):
        resultado = self._operando1 * self._operando2
        print(f"Resultado de la multiplicación: {resultado}")

    def dividir(self):
        resultado = self._operando1 / self._operando2
        print(f"Resultado de la división: {resultado}")

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2


# Programa principal
if __name__ == "__main__":
    print("*** Encapsulamiento de clase Aritmética ***")
    aritmetica1 = Aritmetica(5, 7)
    print("Primer objeto")
    print(f"Valor operando1 del objeto aritmética1: {aritmetica1.operando1}")
    print(f"Valor operando2 del objeto aritmética1: {aritmetica1.operando2}")
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.operando1 = 9
    aritmetica1._operando2 = 15
    print(f"Valor operando1 del objeto aritmética1: {aritmetica1.operando1}")
    print(f"Valor operando2 del objeto aritmética1: {aritmetica1.operando2}")

    # Segundo objeto
    aritmetica2 = Aritmetica(12, 16)
    print("Primer objeto")
    print(f"Valor operando1 del objeto aritmética2: {aritmetica2.operando1}")
    print(f"Valor operando2 del objeto aritmética2: {aritmetica2.operando2}")
    print()
    aritmetica2.sumar()
    aritmetica2.restar()
