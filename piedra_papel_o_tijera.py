import os
import random
os.system('cls')
# Piedra papel o tijera

print("Vamos a jugar!")
while True:
    user = int(input("Pulsa 1 para piedra, 2 para papel, 3 para tijera "))
    maquina = random.randint(1, 3) # 1: Piedra 2: Papel 3: Tijera
    if (user == 1 and maquina == 1) or (user == 2 and maquina == 2) or (user == 3 and maquina == 3):
        if user == 1:
            print("Has sacado piedra")
        elif user == 2:
            print("Has sacado papel")
        elif user == 3:
            print("Has sacado tijera")
        if maquina == 1:
            print("La maquina ha sacado piedra")
        elif maquina == 2:
            print("La maquina ha sacado papel")
        elif maquina == 3:
            print("La maquina ha sacado tijera")
        print("Empate")
        print("Vuelvelo a intentar")
        break
    elif (user == 1 and maquina == 2) or (user == 2 and maquina == 3) or (user == 3 and maquina == 1):
        if user == 1:
            print("Has sacado piedra")
        elif user == 2:
            print("Has sacado papel")
        elif user == 3:
            print("Has sacado tijera")
        if maquina == 1:
            print("La maquina ha sacado piedra")
        elif maquina == 2:
            print("La maquina ha sacado papel")
        elif maquina == 3:
            print("La maquina ha sacado tijera")
        print("Has perdido")
        print("Vuelvelo a intentar")
        break
    elif (user == 1 and maquina == 3) or (user == 2 and maquina == 1) or (user == 3 and maquina == 2):
        if user == 1:
            print("Has sacado piedra")
        elif user == 2:
            print("Has sacado papel")
        elif user == 3:
            print("Has sacado tijera")
        if maquina == 1:
            print("La maquina ha sacado piedra")
        elif maquina == 2:
            print("La maquina ha sacado papel")
        elif maquina == 3:
            print("La maquina ha sacado tijera")
        print("Has ganado")
        print("Enhorabuena!")
        break
