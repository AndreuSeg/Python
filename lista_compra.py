import os
# Lista de la compra
os.system('cls')
lista_compra = []

texto = "Lista de la compra"
print(texto + "\n" + "-" * len(texto) + "\n")

input_user = None
while True:
    input_user = input("¿Que desea comprar? (Q para salir) y (B para borrar) ")
    input_user = input_user.capitalize()
    if input_user == "Q" or input_user == "q":
        break
    elif input_user == "B" or input_user == "b":
        input_user_2 = input("¿Que quieres borrar? ")
        input_user_2 = input_user_2.capitalize()
        if input_user_2 in lista_compra:
            lista_compra.remove(input_user_2)
            print("Se ha borrado de la lista. ")
            print("De momento la lista es esta:\n{}".format(lista_compra))
        else:
            print("{} no esta en la lista.".format(input_user_2))
    elif input_user in lista_compra:
        print("{} ya esta añadido a la lista".format(input_user))
    else:
        confirmacion = input("¿Seguro que quieres añadir {} a la lista de la compra (S/N) ".format(input_user))
        if confirmacion == "S" or confirmacion == "s":
            lista_compra.append(input_user)
            print("{} se ha añadido a la lista de compra.".format(input_user))
            print("De momento la lista es esta:\n{}".format(lista_compra))
        else:
            pass
print("La lista final es:")
print(lista_compra)

# Tambien podria ser esto en vez del primer while
"""
while input_user != "Q" or input_user != "q":
    input_user = input("¿Que desea comprar? (Q para salir) ")
    if input_user == "Q" or input_user == "q":
        print("La lista final es:")
        print(lista_compra)
        exit()
"""
