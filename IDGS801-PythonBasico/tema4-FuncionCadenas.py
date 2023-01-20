
cadena = "Universidad Tecnologica De Leon"

print(cadena)
print(cadena.lower())  # Minusculas
print(cadena.upper())  # Mayusculas
print(cadena.title())  #capitaliza
print(cadena.find("de")) 
print(cadena.count("a")) # Cuenta el numero de letra que hay en el String
textoFinal = cadena.replace("a","4") # Lo usamos para remplasar los elemntos en una cadena

print(textoFinal)
cadenaNueva = cadena.split(" ") # Separa los elementos por el elemento que seleccionemos, y los convierte en una lista
print(cadenaNueva)