import random
import time
import os
# Combate pokemon
os.system('cls')

# Datos pikachu
vida_total_p = 80
vida_p = 80
bola_voltio = 11
onda_trueno = 10
pociones_totales_p = 2
pociones_restantes_p = 2

# Datos Squirtle
vida_total_s = 90
vida_s = 90
placaje = 8
burbuja = 10
pistola_de_agua = 13
pociones_totales_s = 2
pociones_restantes_s = 2

# Otros datos
largo_barra = 20
porcentaje_vida_p = int(vida_p * largo_barra / vida_total_p)
porcentaje_vida_s = int(vida_s * largo_barra / vida_total_s)
pocion = 20

print("Info adicional:\nLas pociones restauran 20 de vida")
input("Enter para continuar")
os.system('cls')

while vida_p > 0 and vida_s > 0:
    # Turno Pikachu
    print("\nTurno de pikachu:")
    # Barra de vida
    porcentaje_vida_p = int(vida_p * largo_barra / vida_total_p)
    porcentaje_vida_s = int(vida_s * largo_barra / vida_total_s)
    print("La vida de pikachu es [{}{}] ({}/{})".format(("#" * porcentaje_vida_p),
                                                                 " " * (largo_barra - porcentaje_vida_p), vida_p, vida_total_p))
    print("La vida de squirtle es [{}{}] ({}/{})".format(("#" * porcentaje_vida_s),
                                                                 " " * (largo_barra - porcentaje_vida_s), vida_s, vida_total_s))
    ataque_pikachu = random.randint(1, 2)
    pocion_pikachu = random.randint(1, 3)
    if ataque_pikachu == 1 and (pocion_pikachu == 1 or pocion_pikachu == 2):
        # Bola voltio
        vida_s -= bola_voltio
        print("Has usado bola voltio:")
    elif ataque_pikachu == 2 and (pocion_pikachu == 1 or pocion_pikachu == 2):
        # Onda trueno
        vida_s -= onda_trueno
        print("Has usado onda trueno:")
    elif (ataque_pikachu == 1 or ataque_pikachu == 2) and pocion_pikachu == 3 and pociones_restantes_p > 0:
        vida_p += pocion
        pociones_restantes_p -= 1
        porcentaje_vida_p = int(vida_p * largo_barra / vida_total_p)
        print("Has utilizado una pocion. Restauras 20 ps")
        print("Te quedan {} pociones.".format(pociones_restantes_p))
        print("La vida de pikachu es [{}{}] ({}/{})".format(("#" * porcentaje_vida_p),
                                                           " " * (largo_barra - porcentaje_vida_p), vida_p, vida_total_p))
    else:
        print("Te has quedado sin pociones. Pierdes el turno")
    # Turno Squirtle
    ataque_escogido = None
    print("\nTurno de squirtle:")
    # Barra de vida
    porcentaje_vida_p = int(vida_p * largo_barra / vida_total_p)
    porcentaje_vida_s = int(vida_s * largo_barra / vida_total_s)
    print("La vida de pikachu es [{}{}] ({}/{})".format(("#" * porcentaje_vida_p),
                                                                 " " * (largo_barra - porcentaje_vida_p), vida_p, vida_total_p))
    print("La vida de squirtle es [{}{}] ({}/{})".format(("#" * porcentaje_vida_s),
                                                                 " " * (largo_barra - porcentaje_vida_s), vida_s, vida_total_s))
    print("Ataques:\n"
          "1. Placaje\n"
          "2. Burbuja\n"
          "3. Pistola de agua")
    while ataque_escogido != 1 and ataque_escogido != 2 and ataque_escogido != 3:
        ataque_escogido = int(input("Que ataque quieres usar: "))
        if ataque_escogido == 1:
            # Placaje
            vida_p -= placaje
            print("Has usado placaje:")
            input("\nEnter para continuar\n")
        elif ataque_escogido == 2:
            # Burbuja
            vida_p -= burbuja
            print("Has usado burbuja:")
            input("\nEnter para continuar")
        elif ataque_escogido == 3:
            # Pistola de agua
            vida_p -= pistola_de_agua
            print("Has usado pistola de agua:")
            input("\nEnter para continuar")
if vida_s > vida_p:
    print("La vida de pikachu es [{}{}] ({}/{})".format(("#" * porcentaje_vida_p),
                                                                 " " * (largo_barra - porcentaje_vida_p), vida_p, vida_total_p))
    print("La vida de squirtle es [{}{}] ({}/{})".format(("#" * porcentaje_vida_s),
                                                                 " " * (largo_barra - porcentaje_vida_s), vida_s, vida_total_s))
    print("Squirtle es el ganador!")
else:
    print("La vida de pikachu es [{}{}] ({}/{})".format(("#" * porcentaje_vida_p),
                                                                 " " * (largo_barra - porcentaje_vida_p), vida_p, vida_total_p))
    print("La vida de squirtle es [{}{}] ({}/{})".format(("#" * porcentaje_vida_s),
                                                                 " " * (largo_barra - porcentaje_vida_s), vida_s, vida_total_s))
    print("Pikachu es el ganador!")
