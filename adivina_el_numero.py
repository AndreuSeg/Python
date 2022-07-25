import random
"""
Adivina el numero
"""

print("Adivina el numero!\n")

x = random.randint(1, 10)

y = int(input("Adivina el numero entre 1 y 10: "))

if y < 10 or y > 1:
    print("Has escrito un numero invalido.")

if y == x:
    print("Has acertado el numero! Muy bien")

print("El numero ganador era: {}".format(x))
