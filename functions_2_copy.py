def medir_palabras(iterable, *args):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)


def main():
    print(medir_palabras("¿Hola que tal estas?"))
    print(medir_palabras("¿", "Hola", "que", "tal", "estas", "?"))


if __name__ == "__main__":
    main()
