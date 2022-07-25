# Como elegir un movil

"""
Moviles:
    iphone ultima gen
    iphone 2nda mano
    xiaomi 100 €
    xiamoi 800 €
"""

texto = "Vamos a elegir un nuevo movil"
print(texto + "\n" + ("-" * len(texto)) + "\n")

dinero = int(input("¿Cuanto dinero tienes? "))
teconologia = input("¿Te gusta la teconologia? ")
if dinero >= 200 and (teconologia == "S" or teconologia == "s"):
    print("Te deberias comprar el xiaomi de ultima generación.")
elif dinero >= 200 and (teconologia == "N" or teconologia == "n"):
    print("Te deberias comprar el iphone de ultima generación.")
elif dinero <= 200 and (teconologia == "S" or teconologia == "s"):
    print("Te deberias comprar el xiaomi de bajo rendimiento.")
elif dinero <= 200 and (teconologia == "N" or teconologia == "n"):
    print("Te deberias comprar el iphone de segunda mano.")
