def main(calc):
    resultado = calc * 2
    return resultado


if __name__ == "__main__":
    print("Bienvenidos a mi primera funcion")
    print("Vamos a multiplicarlo todo por 2")
    resultado_1 = (main(calc=int(input("Escribe un numero: "))))
    resultado_2 = (main(calc=int(input("Escribe otro numero: "))))
    resultado_3 = (main(calc=int(input("Escribe otro numero: "))))
    print("El resulatdo de la multiplicacion del primer nuemero es: {}, del segundo {} y del tercero {}"
          .format(resultado_1, resultado_2, resultado_3))
