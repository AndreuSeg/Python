def main(potencia, potenciador):
    num_1 = potencia ** potenciador
    return num_1


def num2(potencia, potenciador):
    num_2 = potencia ** potenciador
    return num_2


if __name__ == "__main__":
    result = (main(potencia=int(input("Introduce un numero: ")), potenciador=int(input("¿Por que numero quieres elevarlo? "))))
    result_2 = (num2(potencia=int(input("Introduce un numero: ")), potenciador=int(input("¿Por que numero quieres elevarlo? "))))
    print("El primero conjunto de numeros son: {}\nY el segundo conjunto son: {}".format(result, result_2))
