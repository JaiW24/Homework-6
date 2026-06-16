def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print("Iteration", i + 1, ":", x)


def main():
    k = float(input("Enter k value: "))
    x = float(input("Enter starting x value: "))
    n = int(input("Enter number of iterations: "))

    if x < 0 or x > 1:
        print("Error: x must be between 0 and 1.")
        return

    chaos(k, x, n)


main()