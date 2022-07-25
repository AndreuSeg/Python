def seguro_o_no():
    x = input("¿Estas seguro? ")
    if x == "S" or x == "s":
        seguro = True
    else:
        seguro = False
    return seguro


def main():
    seguro_o_no()


if __name__ == "__main__":
    main()
