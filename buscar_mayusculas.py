# Buscar letras mayusculas y minusculas

frase = input("Escribe una frase que contenga mayusculas y minusculas: ")

mayus = 0
minus = 0

for letra in frase:
    if letra == letra.upper():
        mayus += 1
    elif letra == letra.lower():
        minus += 1
print("Hay {} mayusculas y {} minusculas.".format(mayus, minus))
