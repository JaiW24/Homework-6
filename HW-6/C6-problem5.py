def isPrime(n):
    found = False

    for i in range(2, n):
        if n % i == 0:
            found = True

    return found


def main():
    n = int(input("Enter an integer: "))

    found = isPrime(n)

    if n <= 1:
        print(n, "is not prime.")

    elif found:
        print(n, "is not prime.")

    else:
        print(n, "is prime.")


main()