def is_armstrong_number(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return n == total

def main():
    # Example: 371 = 3^3 + 7^3 + 1^3

    try:
        num = int(input("Please insert an int: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")


if __name__ == "__main__":
    main()