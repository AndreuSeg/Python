# Tabla de multiplicar

numero = int(input("Introduce un numero: "))

for n in range(1, 11):
    if n % 2 == 0:
        print("{} x {} = {}".format(numero, n, numero * n))
