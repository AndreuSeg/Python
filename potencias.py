def potencias(num, *args):
    if args:
        result = [num]
        for n in args:
            result.append(n)
            result = num ** n
        return result
    elif not args:
        num = num ** 2
        return num


def main():
    print(potencias(2, 5))


if __name__ == "__main__":
    main()
