# Test

texto = "Bienvenido al test para calcular lo virgen que eres"
print(texto + "\n" + ("-" * len(texto)) + "\n")

puntucion = 0.0
r1 = input("Pregunta 1. ¿Que campeon te gusta mas?\n"
           "    a) Darius\n"
           "    b) Garen\n"
           "    c) Tryndamere\n")
if r1 == "a" or r1 == "A":
    puntucion = puntucion + 1.0
elif r1 == "b" or r1 == "B":
    puntucion = puntucion + 1.0
elif r1 == "c" or r1 == "C":
    puntucion = puntucion + 1.0
else:
    print("Las opciones son a/a - b/B - c/C")
    exit()

r2 = input("Pregunta 2. ¿Que rol te gusta mas?\n"
           "    a) Top\n"
           "    b) Jungla\n"
           "    c) Mid\n"
           "    d) Adc\n"
           "    e) Support\n")
if r2 == "a" or r2 == "A":
    puntucion += 2.0
elif r2 == "b" or r2 == "B":
    puntucion += 0.0
elif r2 == "c" or r2 == "C":
    puntucion += 0.0
elif r2 == "d" or r2 == "D":
    puntucion += 0.0
elif r2 == "e" or r2 == "E":
    puntucion -= 1.0
else:
    print("Las opciones son a/a - b/B - c/C - d/D - e/E")
    exit()

print("Tu puntuación final es: {}".format(puntucion))
if puntucion > 2:
    print("Eres un virgen asqueroso. DUCHATE!!")
else:
    print("Eres normal.")
