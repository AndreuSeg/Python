# Buscar

frase = input("Introduce una frase: ")

espacios = 0
comas = 0
puntos = 0

for letra in frase:
    if letra == " ":
        espacios += 1
    elif letra == ",":
        comas += 1
    elif letra == ".":
        puntos += 1
print("Espacios: {} | Comas: {} | Puntos: {}".format(espacios, comas, puntos))
