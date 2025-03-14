class Aritmetica:
    # Python Solamente toma el ultimo constructor
    # def __init__(self, operando1):
    #     self.operando1 = operando1

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f"Resultado de la suma: {resultado}")

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f"Resultado de la resta: {resultado}")

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f"Resultado de la multiplicación: {resultado}")

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f"Resultado de la división: {resultado}")


# Programa principal
if __name__ == "__main__":
    print("*** Ejemplo clase Aritmética ***")
    # Primer objeto
    print("Primer objeto")
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    # Segundo objeto
    print()
    print("Segundo objeto")
    aritmetica2 = Aritmetica(12, 16)
    aritmetica2.sumar()
    aritmetica2.restar()
    # Tercer Objeto
    print("Tercer Objeto")
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    aritmetica3.sumar()
    # Cuarto objeto
    print("Cuarto objeto")
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()
    # Quinto objeto
    print("Quinto objeto")
    aritmetica5 = Aritmetica(operando2=4, operando1=3)
    aritmetica5.sumar()
