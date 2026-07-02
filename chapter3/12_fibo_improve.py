def fibonacci(n):

    if n in [0, 1]: return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def main():
    try:
        n = int(input("Please insert a non-negative integer: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return

    fib_number = fibonacci(n)

    print(f"The {n}th Fibonacci number is {fib_number}")


if __name__ == "__main__":
    main()