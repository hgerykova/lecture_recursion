def recursive_nth_fibo(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return recursive_nth_fibo(number - 1) + recursive_nth_fibo(number - 2)


def main():
    number = int(input("vlozte cisla:"))
    seq = []
    for num in range(number):
        seq.append(recursive_nth_fibo(num))
    print(seq)



if __name__ == "__main__":
    main()
