# Las Listas si son mutables

nombres = ["Juan", "Mario", "Laura"]
numeros = [1, 2,3]
datos = [1, 2, .5, "Mario", True]

nombres[0] = "Roberto" # Sustitucion de nombre por el indice

# Como recorrer los elementos en la lista
print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

nombres.append("Dario") # Las listas si nos permiten agregar elementos nuevos
print(nombres)
nombres.insert(2,"Laura") # Remplasa el elemnto segun el indice
print(nombres)

nombres.extend(["checha","teofilo"])
print(nombres)

nombres.remove("checha")
print(nombres)
nombres.pop() # Nos ayuda a eliminar el ultimo elemento
print(nombres)

n = ["Juan"]
n2 = n*5
print(n2)
print(nombres)

del nombres[0] # Elimina algun elemento de la lista
print(nombres)