print("Mi primer programa!\n")

n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce otro numero: "))
n3 = int(input("Introduce otro numero: "))

print("El numero mas pequeño entre {}, {} y {} es: {}".format(n1, n2, n3, max(n1, n2, n3)))
print("El numero mas grande entre {}, {} y {} es: {}".format(n1, n2, n3, min(n1, n2, n3)))
