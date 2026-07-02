def main():
    n = int(input("Please insert an int: "))

    a = 0
    b = 1

    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp + b

    # Print the nth Fibonacci number
    print(f"The {n}th Fibonacci number is {b}")

# If this script is being run directly (as opposed to being imported as a module),
# call the main function
if __name__ == "__main__":
    main()