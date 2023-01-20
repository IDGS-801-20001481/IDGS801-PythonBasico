# Hacer un programa via teclado y imprimir la tabla de multiplicar del numero

numero = int(input("Ingresa el numero de la tabla"))

for x in range(1,11):
    print(numero , "x" , x , " = " ,(numero * x))
