tupla = (1,2,3) # Las tuplas no pueden cambiar su valor inicial y unico

print(tupla)
print(type(tupla))
tupla2 = (7, "Roberto" , True , 23.8 , 16+7j) # Las tuplas pueden recibir cualquier valor

print(tupla2)
print(tupla2[1]) # Podemos acceder a los elementos atraves de su indice
print(tupla2[4])
print(tupla2[-1]) # Podemos recorrer la tupla de forma inversa
print(tupla2[0:3]) # Nos sirve para imprimir en un rango de valores
print(tupla2[:3]) # El lenguaje asume que inicia desde el 0
print(tupla2[3:]) # El lenguaje asume que la impresion finaliza en el ultimo valor

a,b,c = tupla # Podemos asociar un elemento con una variable como si se tratara de un indice
print(a)
print(c)

tuplaN = tupla = tupla2 # Se pueden sumar las tuplas
print(tuplaN)

print(tupla.count(2)) # Cuenta los valores similares en la tupla