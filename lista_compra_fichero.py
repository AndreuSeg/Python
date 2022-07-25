import time
SALIDA = "SALIR"


def pregutar(product):
    producto = input("Introduce un producto: [{}] para salir: ".format(SALIDA))
    return producto


def archivo(lista):
    name = input("Como quieres que se llame el archivo .txt: ")
    a = open(name, "w")
    a.write("\n".join(lista))
    a.close()
    return a


def main():
    lista_compra = ["Pan", "Leche", "Galletas", "Arroz", "Pollo", "Cebolla"]
    print("La lista de productos que puedes comprar:\n{}".format("\n".join(lista_compra)))
    lista_compra_user = []
    input_user = pregutar(product=lista_compra)
    while input_user != SALIDA:
        if input_user in lista_compra:
            lista_compra_user.append(input_user)
            print("Tu lista de la compra es:\n{}".format("\n".join(lista_compra_user)))
            input_user = pregutar(product=lista_compra)
        else:
            print("No esta en nuestra lista principal")
            print("La lista de productos que puedes comprar:\n{}".format("\n".join(lista_compra)))
            input_user = pregutar(product=lista_compra)
    crear_archivo = archivo(lista=lista_compra)


if __name__ == "__main__":
    main()
