SALIDA = "SALIR"


def pregutar():
    return input("Introduce un producto: [{}] para salir: ".format(SALIDA))


def guardar_a_lista(lista_compra, item_a_guardar):
    if item_a_guardar.capitalize() in [a.capitalize() for a in lista_compra]:
        print("El producto ya existe")
    else:
        lista_compra.append(item_a_guardar)


def archivo(lista_compra):
    name = input("Como quieres que se llame el archivo: ")
    with open(name + ".txt", "w") as doc:
        doc.write("\n".join(lista_compra))


def main():
    lista_compra = []
    input_user = pregutar()
    while input_user != SALIDA:
        guardar_a_lista(lista_compra, input_user)
        print("Tu lista de la compra es:\n{}".format("\n".join(lista_compra).capitalize()))
        input_user = pregutar()
    archivo(lista_compra)


if __name__ == "__main__":
    main()
