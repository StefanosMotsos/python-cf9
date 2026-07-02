def compare_integers(a, b):
    if a == b:
        print("The numbers are equal")
    elif a > b:
        print("The first number is greater than the second number")
    else:
        print("The second number is greater than the first number")

def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number")

    compare_integers(a, b)

    # 1. Ternary operator (simple example)
    result = "positive" if a > 0 else "negative"
    print(result)

    # 2. Ternary operator (extended example)
    result2 = (
        "The numbers are equal" if a == b else
        "The first number is greater than the second number" if a > b else
        "The second number is greater than the first number"
    )
    print(result2)

if __name__ == "__main__":
    main()