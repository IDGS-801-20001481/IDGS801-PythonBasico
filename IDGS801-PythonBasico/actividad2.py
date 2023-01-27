class Calculator:
    def __init__(self):
        pass

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b
        

def main():
    calc = Calculator()
    while True:
        try:
            num1 = float(input("Numero 1: "))
            num2 = float(input("Numero 2: "))
            operation = input("Selecciona una Operacion): (1) Suma, (2) Resta, (3) Multuplicacion, (4) Division  ")   
            if operation == "1":
                print(calc.suma(num1, num2))
            elif operation == "2":
                print(calc.resta(num1, num2))
            elif operation == "3":
                print(calc.multiplicacion(num1, num2))
            elif operation == "4":
                print(calc.division(num1, num2))
            elif operation == "salir":
                break
            else:
                print("Operacion invalida")
        except ValueError:
            print("")

if __name__ == '__main__':
    main()
