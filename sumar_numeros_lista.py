def sumar_lista(num, *args):
    if args:
        result = None
        nums = [num]
        for n in args:
            nums.append(n)
            result = sum(nums)
        return result


def main():
    print(sumar_lista(10, 40, 50))


if __name__ == "__main__":
    main()
