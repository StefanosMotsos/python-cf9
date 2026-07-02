from functools import reduce

n = int(input("Give an int to calc facto: "))

result = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"{n}! = {result}")


# Modified lambda function to print intermediate results
def print_and_multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

result = reduce(print_and_multiply, range(1, n + 1))

print(f"Final result: {result}")


# Use reduce with a lambda function that includes a print statement
result = reduce(lambda x, y: print(f"{x} * {y} = {x * y}") or x * y, range(1, n + 1))
print(f"Final result: {result}")