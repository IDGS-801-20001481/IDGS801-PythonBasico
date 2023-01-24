
class OperasBas:

    
    #propiedades de clase
    n1 = 0
    n2 = 0
    res = 0
    #Constructor de clase
    def __init__(self, a, b) :
        self.n1 = a
        self.n1 = b
    # Metodos de clase o metodos de acceso
    def suma(self):
        self.res = self.n1 + self.n2

    def resta(self):
        self.res = self.n1 - self.n2

    def main():
        obj = OperasBas(3,2)
        obj.suma