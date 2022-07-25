def fibonacci(n):
    sequence = [0, 1]
    for i in range(1, n - 1):
        sequence.append(sequence[i - 1] + sequence[i])
    return sequence


def main():
    print(fibonacci(int(input("¿Cuantos saltos quieres dar? "))))


if __name__ == "__main__":
    main()
