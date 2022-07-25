import readchar
import os
import random
os.system('cls')

# Constantes de mi posicion
POS_X = 0
POS_Y = 1

# Mi posicion
my_position = [11, 2]
tail_len = 0
tail = []

# Numero de obstaculos
NUMBER_OF_OBSTACLES = 1
map_objects = []

obstacles_definition = """\
#########   ############
### ######     #########
###  ###### ############
###    ####  ###########
###### ####       ######
######  ########  ######
######            ######
########   #############
######### ##############
########        ########\
"""

obstacles_definition = [list(row) for row in obstacles_definition.split("\n")]
# Mapa
MAP_WIDTH = len(obstacles_definition[0])
MAP_HEIGHT = len(obstacles_definition)

end_game = False
died = False
# Empiezo while
while not end_game:
    os.system('cls')
    # Generar obstaculos aleatorios no repetidos y que no estan en mi posicion
    while len(map_objects) < NUMBER_OF_OBSTACLES:
        new_position = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]
        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)
    # Dibujar mapa
    print("+" + "-" * (MAP_WIDTH * 3) + "+")
    for coordenate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordenate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == coordenate_x and map_object[POS_Y] == coordenate_y:
                    char_to_draw = "O"
                    object_in_cell = map_object
            for tail_piece in tail:
                if tail_piece[POS_X] == coordenate_x and tail_piece[POS_Y] == coordenate_y:
                    char_to_draw = "X"
                    tail_in_cell = tail_piece
            if my_position[POS_X] == coordenate_x and my_position[POS_Y] == coordenate_y:
                char_to_draw = "X"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_len += 1
                if tail_in_cell:
                    died = True
                    end_game = True
            if obstacles_definition[coordenate_y][coordenate_x] == "#":
                char_to_draw = "#"
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    # Moverte
    print("Puntuacion: {}".format(len(tail)))
    print("¿Donde quieres moverte: (WASD). Y si quieres salir del programa pulas [Q]")
    direction = readchar.readchar().decode()
    new_position_u = None
    if direction == "W" or direction == "w":
        if my_position[POS_Y] < 1:
            died = True
            end_game = True
        else:
            new_position_u = [my_position[POS_X], my_position[POS_Y] - 1]

    elif direction == "A" or direction == "a":
        if my_position[POS_X] < 1:
            died = True
            end_game = True
        else:
            new_position_u = [my_position[POS_X] - 1, my_position[POS_Y]]

    elif direction == "S" or direction == "s":
        if my_position[POS_Y] >= MAP_HEIGHT - 1:
            died = True
            end_game = True
        else:
            new_position_u = [my_position[POS_X], my_position[POS_Y] + 1]

    elif direction == "D" or direction == "d":
        if my_position[POS_X] >= MAP_WIDTH - 1:
            died = True
            end_game = True
        else:
            new_position_u = [my_position[POS_X] + 1, my_position[POS_Y]]

    elif direction == "Q" or direction == "q":
        end_game = True

    if new_position_u:
        if obstacles_definition[new_position_u[POS_Y]][new_position_u[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[0: tail_len]
            my_position = new_position_u

# Acabo while
if died:
    print("Has perdido")
