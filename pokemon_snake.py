import random
import readchar
import os

POS_X = 0
POS_Y = 1
VIDA_POKEMON = 20
vida_actual_pokemon = VIDA_POKEMON
VIDA_PIKACHU = 50
vida_pikachu = VIDA_PIKACHU
VIDA_CHARMANDER = 45
vida_charmander = VIDA_CHARMANDER
VIDA_BULVASAUR = 55
vida_bulvasaur = VIDA_BULVASAUR
VIDA_EEVEE = 60
vida_eevee = VIDA_EEVEE
VIDA_PIDGEY = 30
vida_pidgey =VIDA_PIDGEY
VIDA_JIGGLYPUFF = 40
vida_jigglypuff = VIDA_JIGGLYPUFF
VIDA_MAGIKARP = 5
vida_magikarp =VIDA_MAGIKARP

TAMAÑA_BARRA_VIDA = 30

walls_definition ="""\
██  ████████  ████  ███████████████
██  ██████    ████  ███████████████
██  ████████             ██      ██
██      ██████████       ██  ██  ██
██      ████     ██████  ██  ██  ██
██        ████     ████  ██  ██  ██
████████    ██        █  ██  ██  ██
█████████   ███████      ██  ██  ██
██████████                   ██  ██
██████████████               ██  ██
          ████           ████      
████████  ████                  ███
████████  ████                  ███
███         ██████  ███████   █████
███  ████  ███████  ███████████████
███  ████                         █
██   █████████████  ███████████████\
"""

endgame = False
my_position = [2, 1]
pokemon_masters = random.randint(2, 10)
masters_on_map = []

walls_definition = [list(row) for row in walls_definition.split("\n")]
MAP_WIDTH = len(walls_definition[0])
MAP_HEIGHT = len(walls_definition)

#Choose a pokemon
chosen_pokemon = input("Choose a Pokemon.\n 1) Pikachu\n 2) Bulvasaur \n 3) Charmander\n")
if chosen_pokemon == "1":
    chosen_pokemon = "Pikachu"
elif chosen_pokemon == "2":
    chosen_pokemon = "Bulvasaur"
elif chosen_pokemon == "3":
    chosen_pokemon = "Charmander"

#ubiacate masters on the map
while len(masters_on_map) < pokemon_masters:
    new_master = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
    if new_master not in masters_on_map and new_master != my_position and walls_definition[new_master[POS_Y]][new_master[POS_X]] != "█":
        masters_on_map.append(new_master)

#mail loop
while not endgame:
    os.system("cls")

    print("+" + "-" * MAP_WIDTH * 2 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            draw_point = "  "
            master_in_cell = None

            for master in masters_on_map:
                if master[POS_X] == coordinate_x and master[POS_Y] == coordinate_y:
                    draw_point = " !"
                    master_in_cell = master
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                draw_point = " *"
                if master_in_cell:
                    os.system("cls")
                    print("¡Has iniciado un Combate Pokemon!")
                    pokemon_opponent = 2

                    if pokemon_opponent == 1:
                        pokemon_name = "Pikachu"
                        print("Tu oponente es: {}".format(pokemon_name))
                        while vida_actual_pokemon > 0 and vida_pikachu > 0:
                            os.system("cls")
                            # Turno del contrario
                            print("Turno de {}".format(pokemon_name))
                            pokemon_attack = random.randint(1, 3)
                            if pokemon_attack == 1:  # Bola Voltio
                                critic_damage = random.randint(7, 15)
                                print("Pikachu ataca con Bola Voltio\n"
                                      "Hace {} de daño".format(critic_damage))
                                vida_actual_pokemon -= critic_damage
                            elif pokemon_attack == 2:  # impactrueno
                                critic_damage = random.randint(10, 12)
                                print("Pikachu ataca con impactrueno\n"
                                      "Hace {} de daño".format(critic_damage))
                                vida_actual_pokemon -= critic_damage
                            else:  # Onda Trueno
                                critic_damage = random.randint(4, 18)
                                print("Pikachu ataca con Onda Trueno\n"
                                      "Hace {} de daño".format(critic_damage))
                                vida_actual_pokemon -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_pikachu * TAMAÑA_BARRA_VIDA / VIDA_PIKACHU)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_pikachu, VIDA_PIKACHU))

                            if 0 >= vida_actual_pokemon < vida_pikachu:
                                os.system("cls")
                                print("{} gana".format(pokemon_name))
                                print("Has perdido")
                                endgame = True
                                break

                            input("ENTER para continuar")
                            os.system("cls")

                            # Tu turno
                            print("Turno de {}".format(chosen_pokemon))
                            my_attack = None
                            while my_attack != "1" and my_attack != "2" and my_attack != "3":
                                my_attack = input("¿Que ataque vas a realizar?\n"
                                                  "1) Placaje\n"
                                                  "2) Embestida\n"
                                                  "3) Patada\n")
                                if my_attack == "1":
                                    critic_damage = random.randint(4, 16)
                                    print("Mi {} ataca con Placaje\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_pikachu -= critic_damage
                                elif my_attack == "2":
                                    critic_damage = random.randint(4, 20)
                                    print("Mi {} ataca con Embestida\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_pikachu -= critic_damage
                                elif my_attack == "3":
                                    critic_damage = random.randint(4, 19)
                                    print("Mi {} ataca con Patada\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_pikachu -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_pikachu * TAMAÑA_BARRA_VIDA / VIDA_PIKACHU)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_pikachu, VIDA_PIKACHU))

                            input("ENTER para continuar")
                            os.system("cls")
                        if 0 >= vida_actual_pokemon < vida_pikachu:
                            print("{} gana".format(pokemon_name))
                            print("Has perdido")
                            endgame = True
                            break

                        else:
                            print("{} gana".format(chosen_pokemon))
                            masters_on_map.remove(master_in_cell)
                            vida_pikachu = VIDA_PIKACHU
                            vida_actual_pokemon = VIDA_POKEMON
                            input("Cerrar")
                        os.system("cls")

                    elif pokemon_opponent == 2:
                        os.system("cls")
                        pokemon_name = "Charmander"
                        print("Tu oponente es: {}".format(pokemon_name))
                        while vida_actual_pokemon > 0 and vida_charmander > 0:
                            os.system("cls")
                            # Turno del contrario
                            print("Turno de {}".format(pokemon_name))
                            pokemon_attack = random.randint(1, 3)
                            if pokemon_attack == 1:  # Giro fuego
                                critic_damage = random.randint(9, 15)
                                print("{} ataca con Giro fuego\n"
                                      "Hace {} de daño".format(pokemon_name,critic_damage))
                                vida_actual_pokemon -= critic_damage
                            elif pokemon_attack == 2:  # Lanzallamas
                                critic_damage = random.randint(3, 16)
                                print("{} ataca con Lanzallamas\n"
                                      "Hace {} de daño".format(pokemon_name,critic_damage))
                                vida_actual_pokemon -= critic_damage
                            else:  # Arañazo
                                critic_damage = random.randint(4, 18)
                                print("{} ataca con Arañazo\n"
                                      "Hace {} de daño".format(pokemon_name,critic_damage))
                                vida_actual_pokemon -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                              " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                              vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_charmander * TAMAÑA_BARRA_VIDA / VIDA_CHARMANDER)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                              " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                              vida_charmander, VIDA_CHARMANDER))


                            if 0 > vida_actual_pokemon < vida_charmander:
                                input(" ")
                                print("{} gana".format(pokemon_name))
                                print("Has perdido")
                                endgame =True
                                break


                            input("ENTER para continuar")
                            os.system("cls")

                            # Tu turno
                            print("Turno de {}".format(chosen_pokemon))
                            my_attack = None
                            while my_attack != "1" and my_attack != "2" and my_attack != "3":
                                my_attack = input("¿Que ataque vas a realizar?\n"
                                                  "1) Placaje\n"
                                                  "2) Embestida\n"
                                                  "3) Patada\n")
                                if my_attack == "1":
                                    critic_damage = random.randint(4, 16)
                                    print("Mi {} ataca con Placaje\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_charmander -= critic_damage
                                elif my_attack == "2":
                                    critic_damage = random.randint(4, 20)
                                    print("Mi {} ataca con Embestida\n"
                                          "Hace {} de daño".format(chosen_pokemon,critic_damage))
                                    vida_charmander -= critic_damage
                                elif my_attack == "3":
                                    critic_damage = random.randint(4, 19)
                                    print("Mi {} ataca con Patada\n"
                                          "Hace {} de daño".format(chosen_pokemon,critic_damage))
                                    vida_charmander -= critic_damage

                                barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                                print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                       " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                       vida_actual_pokemon, VIDA_POKEMON))
                                barra_vida_enemigo = int(vida_charmander * TAMAÑA_BARRA_VIDA / VIDA_CHARMANDER)
                                print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                    " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                    vida_charmander, VIDA_CHARMANDER))

                                input("ENTER para continuar")
                                os.system("cls")
                            if 0 >= vida_actual_pokemon < vida_charmander:
                                print("{} gana".format(pokemon_name))
                                print("Has perdido")
                                endgame = True
                                break

                        else:

                            print("{} gana".format(chosen_pokemon))
                            masters_on_map.remove(master_in_cell)
                            vida_charmander = VIDA_CHARMANDER
                            vida_actual_pokemon = VIDA_POKEMON
                            input("Cerrar")

                        os.system("cls")

                    elif pokemon_opponent == 3:
                        pokemon_name = "Bulvasaur"
                        print("Tu oponente es: {}".format(pokemon_name))
                        while vida_actual_pokemon > 0 and vida_bulvasaur > 0:
                            os.system("cls")
                            # Turno del contrario
                            print("Turno de {}".format(pokemon_name))
                            pokemon_attack = random.randint(1, 3)
                            if pokemon_attack == 1: # Hoja afilada
                                critic_damage = random.randint(8, 13)
                                print("{} ataca con Hoja Afilada\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage
                            elif pokemon_attack == 2:  # polvo veneno
                                critic_damage = random.randint(10, 13)
                                print("{} ataca con Polvo Veneno\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage
                            else:  # Doble Filo
                                critic_damage = random.randint(3, 18)
                                print("{} ataca con Doble Filo\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_bulvasaur * TAMAÑA_BARRA_VIDA / VIDA_BULVASAUR)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_bulvasaur, VIDA_BULVASAUR))

                            if 0 >= vida_actual_pokemon < vida_bulvasaur:
                                print("{} gana".format(pokemon_name))
                                print("Has perdido")
                                endgame = True
                                break

                            input("ENTER para continuar")
                            os.system("cls")

                            # Tu turno
                            print("Turno de {}".format(chosen_pokemon))
                            my_attack = None
                            while my_attack != "1" and my_attack != "2" and my_attack != "3":
                                my_attack = input("¿Que ataque vas a realizar?\n"
                                                  "1) Placaje\n"
                                                  "2) Embestida\n"
                                                  "3) Patada\n")
                                if my_attack == "1":
                                    critic_damage = random.randint(4, 16)
                                    print("Mi {} ataca con Placaje\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_bulvasaur -= critic_damage
                                elif my_attack == "2":
                                    critic_damage = random.randint(4, 20)
                                    print("Mi {} ataca con Embestida\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_bulvasaur -= critic_damage
                                elif my_attack == "3":
                                    critic_damage = random.randint(4, 19)
                                    print("Mi {} ataca con Patada\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_bulvasaur -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_bulvasaur * TAMAÑA_BARRA_VIDA / VIDA_BULVASAUR)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_bulvasaur, VIDA_BULVASAUR))

                            input("ENTER para continuar")
                            os.system("cls")
                        if 0 >= vida_actual_pokemon < vida_bulvasaur:
                            print("{} gana".format(pokemon_name))
                            print("Has perdido")
                            endgame = True
                            break

                        else:
                            print("{} gana".format(chosen_pokemon))
                            masters_on_map.remove(master_in_cell)
                            vida_bulvasaur = VIDA_BULVASAUR
                            vida_actual_pokemon = VIDA_POKEMON
                            input("Cerrar")
                        os.system("cls")

                    elif pokemon_opponent == 4:
                        pokemon_name = "Eevee"
                        print("Tu oponente es: {}".format(pokemon_name))
                        while vida_actual_pokemon > 0 and vida_eevee > 0:
                            os.system("cls")
                            # Turno del contrario
                            print("Turno de {}".format(pokemon_name))
                            pokemon_attack = random.randint(1, 3)
                            if pokemon_attack == 1:  # Ataque Arena
                                critic_damage = random.randint(7, 15)
                                print("{} ataca con Ataque arena\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage
                            elif pokemon_attack == 2:  # Latigo
                                critic_damage = random.randint(3, 12)
                                print("{} ataca con Latigo\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage
                            else:  # Mordisco
                                critic_damage = random.randint(4, 13)
                                print("{} ataca con Mordisco\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_eevee * TAMAÑA_BARRA_VIDA / VIDA_EEVEE)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_eevee, VIDA_EEVEE))

                            if 0 >= vida_actual_pokemon < vida_eevee:
                                print("{} gana".format(pokemon_name))
                                print("Has perdido")
                                endgame = True
                                break

                            input("ENTER para continuar")
                            os.system("cls")

                            # Tu turno
                            print("Turno de {}".format(chosen_pokemon))
                            my_attack = None
                            while my_attack != "1" and my_attack != "2" and my_attack != "3":
                                my_attack = input("¿Que ataque vas a realizar?\n"
                                                  "1) Placaje\n"
                                                  "2) Embestida\n"
                                                  "3) Patada\n")
                                if my_attack == "1":
                                    critic_damage = random.randint(4, 16)
                                    print("Mi {} ataca con Placaje\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_eevee -= critic_damage
                                elif my_attack == "2":
                                    critic_damage = random.randint(4, 20)
                                    print("Mi {} ataca con Embestida\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_eevee -= critic_damage
                                elif my_attack == "3":
                                    critic_damage = random.randint(4, 19)
                                    print("Mi {} ataca con Patada\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_eevee -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_eevee * TAMAÑA_BARRA_VIDA / VIDA_EEVEE)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_eevee, VIDA_EEVEE))

                            input("ENTER para continuar")
                            os.system("cls")

                        if 0 >= vida_actual_pokemon < vida_eevee:
                            print("{} gana".format(pokemon_name))
                            print("Has perdido")
                            endgame = True
                            break

                        else:
                            print("{} gana".format(chosen_pokemon))
                            masters_on_map.remove(master_in_cell)
                            vida_eevee = VIDA_EEVEE
                            vida_actual_pokemon = VIDA_POKEMON
                            input("Cerrar")
                        os.system("cls")

                    elif pokemon_opponent == 5:
                        pokemon_name = "Pidgey"
                        print("Tu oponente es: {}".format(pokemon_name))
                        while vida_actual_pokemon > 0 and vida_pidgey > 0:
                            os.system("cls")
                            # Turno del contrario
                            print("Turno de {}".format(pokemon_name))
                            pokemon_attack = random.randint(1, 3)
                            if pokemon_attack == 1:  # Tornado
                                critic_damage = random.randint(7, 12)
                                print("{} ataca con Tornado\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage
                            elif pokemon_attack == 2:  # viento Afin
                                critic_damage = random.randint(6, 12)
                                print("{} ataca con Viento Afin\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage
                            else:  # Remolino
                                critic_damage = random.randint(4, 10)
                                print("{} ataca con Remolino\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_pidgey * TAMAÑA_BARRA_VIDA / VIDA_PIDGEY)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_pidgey, VIDA_PIDGEY))

                            if 0 >= vida_actual_pokemon < vida_pidgey:
                                print("{} gana".format(pokemon_name))
                                print("Has perdido")
                                endgame = True
                                break

                            input("ENTER para continuar")
                            os.system("cls")

                            # Tu turno
                            print("Turno de {}".format(chosen_pokemon))
                            my_attack = None
                            while my_attack != "1" and my_attack != "2" and my_attack != "3":
                                my_attack = input("¿Que ataque vas a realizar?\n"
                                                  "1) Placaje\n"
                                                  "2) Embestida\n"
                                                  "3) Patada\n")
                                if my_attack == "1":
                                    critic_damage = random.randint(4, 16)
                                    print("Mi {} ataca con Placaje\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_pidgey -= critic_damage
                                elif my_attack == "2":
                                    critic_damage = random.randint(4, 20)
                                    print("Mi {} ataca con Embestida\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_pidgey -= critic_damage
                                elif my_attack == "3":
                                    critic_damage = random.randint(4, 19)
                                    print("Mi {} ataca con Patada\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_pidgey -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_pidgey * TAMAÑA_BARRA_VIDA / VIDA_PIDGEY)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_pidgey, VIDA_PIDGEY))

                            input("ENTER para continuar")
                            os.system("cls")
                        if 0 >= vida_actual_pokemon < vida_pidgey:
                            print("{} gana".format(pokemon_name))
                            print("Has perdido")
                            endgame = True
                            break

                        else:
                            print("{} gana".format(chosen_pokemon))
                            masters_on_map.remove(master_in_cell)
                            vida_pidgey = VIDA_PIDGEY
                            vida_actual_pokemon = VIDA_POKEMON
                            input("Cerrar")
                        os.system("cls")

                    elif pokemon_opponent == 6:
                        pokemon_name = "Jigglypuff"
                        print("Tu oponente es: {}".format(pokemon_name))
                        while vida_actual_pokemon > 0 and vida_jigglypuff > 0:
                            os.system("cls")
                            # Turno del contrario
                            print("Turno de {}".format(pokemon_name))
                            pokemon_attack = random.randint(1, 3)
                            if pokemon_attack == 1:  # Giro Bola
                                critic_damage = random.randint(7, 10)
                                print("{} ataca con Giro Vola\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage
                            elif pokemon_attack == 2:  # Destructor
                                critic_damage = random.randint(10, 12)
                                print("{} ataca con Destrcutor\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage
                            else:  # Descanso
                                critic_damage = random.randint(4, 9)
                                print("{} ataca con Descanso\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_jigglypuff * TAMAÑA_BARRA_VIDA / VIDA_JIGGLYPUFF)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_jigglypuff, VIDA_JIGGLYPUFF))

                            if 0 >= vida_actual_pokemon < vida_jigglypuff:
                                print("{} gana".format(pokemon_name))
                                print("Has perdido")
                                endgame = True
                                break

                            input("ENTER para continuar")
                            os.system("cls")

                            # Tu turno
                            print("Turno de {}".format(chosen_pokemon))
                            my_attack = None
                            while my_attack != "1" and my_attack != "2" and my_attack != "3":
                                my_attack = input("¿Que ataque vas a realizar?\n"
                                                  "1) Placaje\n"
                                                  "2) Embestida\n"
                                                  "3) Patada\n")
                                if my_attack == "1":
                                    critic_damage = random.randint(4, 16)
                                    print("Mi {} ataca con Placaje\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_jigglypuff -= critic_damage
                                elif my_attack == "2":
                                    critic_damage = random.randint(4, 20)
                                    print("Mi {} ataca con Embestida\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_jigglypuff -= critic_damage
                                elif my_attack == "3":
                                    critic_damage = random.randint(4, 19)
                                    print("Mi {} ataca con Patada\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_jigglypuff -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_jigglypuff * TAMAÑA_BARRA_VIDA / VIDA_JIGGLYPUFF)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_jigglypuff, VIDA_JIGGLYPUFF))

                            input("ENTER para continuar")
                            os.system("cls")
                        if 0 >= vida_actual_pokemon < vida_jigglypuff:
                            print("{} gana".format(pokemon_name))
                            print("Has perdido")
                            endgame = True
                            break

                        else:
                            print("{} gana".format(chosen_pokemon))
                            masters_on_map.remove(master_in_cell)
                            vida_jigglypuff = VIDA_JIGGLYPUFF
                            vida_actual_pokemon = VIDA_POKEMON
                            input("Cerrar")
                        os.system("cls")

                    elif pokemon_opponent == 7:
                        pokemon_name = "Magikarp"
                        print("Tu oponente es: {}".format(pokemon_name))
                        while vida_actual_pokemon > 0 and vida_magikarp > 0:
                            os.system("cls")
                            # Tu turno
                            print("Turno de {}".format(chosen_pokemon))
                            my_attack = None
                            while my_attack != "1" and my_attack != "2" and my_attack != "3":
                                my_attack = input("¿Que ataque vas a realizar?\n"
                                                  "1) Placaje\n"
                                                  "2) Embestida\n"
                                                  "3) Patada\n")
                                if my_attack == "1":
                                    critic_damage = random.randint(4, 16)
                                    print("Mi {} ataca con Placaje\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_magikarp -= critic_damage
                                elif my_attack == "2":
                                    critic_damage = random.randint(4, 20)
                                    print("Mi {} ataca con Embestida\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_magikarp -= critic_damage
                                elif my_attack == "3":
                                    critic_damage = random.randint(4, 19)
                                    print("Mi {} ataca con Patada\n"
                                          "Hace {} de daño".format(chosen_pokemon, critic_damage))
                                    vida_magikarp -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_magikarp * TAMAÑA_BARRA_VIDA / VIDA_MAGIKARP)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_magikarp, VIDA_MAGIKARP))

                            input("ENTER para continuar")
                            os.system("cls")

                            if 0 >= vida_magikarp < vida_actual_pokemon:
                                print("{} Pierde".format(pokemon_name))
                                print("Has ganado")
                                masters_on_map.remove(master_in_cell)
                                vida_magikarp = VIDA_MAGIKARP
                                vida_actual_pokemon = VIDA_POKEMON
                                input("Cerrar")
                            os.system("cls")

                            # Turno del contrario
                            print("Turno de {}".format(pokemon_name))
                            pokemon_attack = 1
                            if pokemon_attack == 1: # Salpicadura
                                critic_damage = 1000
                                print("{} ataca con Salpicadura\n"
                                      "Hace {} de daño".format(pokemon_name, critic_damage))
                                vida_actual_pokemon -= critic_damage

                            barra_vida_pokemon = int(vida_actual_pokemon * TAMAÑA_BARRA_VIDA / VIDA_POKEMON)
                            print("Mi {}: | {}{} | ({}/{})".format(chosen_pokemon, "█" * barra_vida_pokemon,
                                                                   " " * (TAMAÑA_BARRA_VIDA - barra_vida_pokemon),
                                                                   vida_actual_pokemon, VIDA_POKEMON))
                            barra_vida_enemigo = int(vida_magikarp * TAMAÑA_BARRA_VIDA / VIDA_MAGIKARP)
                            print("{}: | {}{} | ({}/{})".format(pokemon_name, "█" * barra_vida_enemigo,
                                                                " " * (TAMAÑA_BARRA_VIDA - barra_vida_enemigo),
                                                                vida_magikarp, VIDA_MAGIKARP))

                            input("ENTER para continuar")
                            os.system("cls")

                        if 0 >= vida_actual_pokemon < vida_magikarp:
                            print("{} gana".format(pokemon_name))
                            print("Has perdido")
                            endgame = True
                            break

                        else:
                            print("{} gana".format(chosen_pokemon))
                            masters_on_map.remove(master_in_cell)
                            vida_magikarp= VIDA_MAGIKARP
                            vida_actual_pokemon = VIDA_POKEMON
                            input("Cerrar")
                        os.system("cls")

                    if len(masters_on_map) == 0:
                        endgame = True
                    os.system("cls")

            if walls_definition[coordinate_y][coordinate_x] == "█":
                draw_point = "██"

            print("{}".format(draw_point), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 2 + "+")

#character movement
    direction = readchar.readchar().decode()
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q":
        break
    if new_position:
        if walls_definition[new_position[POS_Y]][new_position[POS_X]] != "█":
            my_position = new_position
os.system("cls")
if endgame:
    if len(masters_on_map) == 0:
        print("¡¡¡¡ LO HAS CONSEGUIDO !!!!\n"
              "¡¡¡¡ DERROTASTE A TODOS LOS MAESTROS !!!!\n")
        input("ENTER")
        input("ENTER")
        input("Enter")
        input("ahora largate me molestas")
        exit()
    elif len(masters_on_map) > 0:
        print("NO PUEDES CONTINUAR\n"
              "FUISTE DERROTADO")
        exit()
