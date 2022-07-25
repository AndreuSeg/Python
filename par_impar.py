def par_impar(num):
    if num % 2 == 0:
        es_par = True
        if es_par:
            print(num)
            return es_par
    else:
        es_par = False
        if not es_par:
            print(num)
            return es_par


def main():
    print(par_impar(110))


if __name__ == "__main__":
    main()
