

edad = int(input("¿Cuantos años tienes? "))
tipo_carnet = input("¿Digame el tipo de carnet "
                    "(E para estudiantes / P para pensionistas / F para familia numerosa / N de nada)? ")

if (25 <= edad <= 35 and (tipo_carnet == "E" or tipo_carnet == "e"))\
        or edad <= 10\
        or (edad >= 65 and (tipo_carnet == "P" or tipo_carnet == "p"))\
        or (tipo_carnet == "F" or tipo_carnet == "f"):
    print("Se te aplica el descuento. ")
else:
    print("No se te aplica el descuento. ")
