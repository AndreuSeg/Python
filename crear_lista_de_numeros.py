# Numeros usuarios

# Opcion donde pones el maximo de numero que quieres
"""
lista = []
maximo = int(input("Cuantos numeros quieres poner de maximo: "))
sequencia = 0
numeros = 0
while sequencia < maximo:
    numeros = int(input("Introduce un numero: "))
    lista.append(numeros)
    sequencia += 1

print(lista)
max_lista = max(lista)
min_lista = min(lista)
print("El numero mas grande es: {} y el mas pequeño es {}".format(max_lista, min_lista))
"""

# Numeros separados por comas
lista_2 = []
numeros_introducidos_2 = (input("Introduce nuemeros separados por comas: "))
numeros_2 = numeros_introducidos_2.split(",")
for numeros in numeros_2:
    lista_2.append(int(numeros)) # Convertir los str en int y meterlos en la lista
print(lista_2)
max_lista_2 = max(lista_2)
min_lista_2 = min(lista_2)
print("El numero mas grande es: {} y el mas pequeño es {}".format(max_lista_2, min_lista_2))
