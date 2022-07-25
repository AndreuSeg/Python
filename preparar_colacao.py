"""
Preparación de colacao
"""

print("Me voy a la cocina")
print("Abro la nevera\n")

hay_leche = input("¿Hay leche? (S/N): ")
hay_colacao = input("¿Hay colacao? (S/N) ")

if hay_leche != "S" or hay_colacao != "S":
    print("Voy al super a comprar...")
    if hay_leche != "S":
        print("Compro leche...")
    if hay_colacao != "S":
        print("Compro colacao...")

print("Sacamos la leche")
print("Sacamos el colacao")
print("Metemos la leche en un vaso")
print("Metemos el colacao en el vaso con la leche")
print("Mezclamos la leche y el colacao.")
