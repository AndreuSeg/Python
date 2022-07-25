def string_larga(palabra, *args):
    if args:
        lista_strings = [palabra]
        for i in args:
            lista_strings.append(i)
        return lista_strings
    return palabra


def main():
    print(("La string mas grande de {} es: {}".format(string_larga("¿Hola", "que", "tal", "estas?"),
                                                      max(string_larga("¿Hola", "que", "tal", "estas?")))))


if __name__ == "__main__":
    main()
