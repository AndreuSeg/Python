SALIDA = "SALIR"
ARCHIVO = "prueba_compra"


def pregutar():
    return input("Introduce un producto: [{}] para salir: ".format(SALIDA))


def guardar_a_lista(lista_compra, item_a_guardar):
    if item_a_guardar.capitalize() in [a.capitalize() for a in lista_compra]:
        print("El producto ya existe")
    else:
        lista_compra.append(item_a_guardar)


def archivo(lista_compra):
    with open(ARCHIVO + ".txt", "w") as doc:
        doc.write("\n".join(lista_compra))


def main():
    lista_compra = []
    cargarlista = input("¿Quieres recuperar la lista de la compra [S/N]? ")
    if cargarlista == "S" or cargarlista == "s":
        try:
            with open(ARCHIVO + ".txt", "r") as doc:
                lista_compra = doc.read().split("\n")
        except FileNotFoundError:
            print("No se ha encontrado el archivo")
    else:
        pass
    input_user = pregutar()
    while input_user != SALIDA:
        guardar_a_lista(lista_compra, input_user)
        print("Tu lista de la compra es:\n{}".format("\n".join(lista_compra)))
        input_user = pregutar()
    archivo(lista_compra)


if __name__ == "__main__":
    main()
