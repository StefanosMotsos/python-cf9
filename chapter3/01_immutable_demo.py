def print_id(variable_name: str, variable):
    """
    Prints the id of the given variable.
    Args:
        variable_name (str): The name of the variable as a string.
        variable: The variable whose id is to be printed.
    """
    print(f"id({variable_name}) = {id(variable)}")

def main():
    a = 10
    b = 10

    print_id("a", a)
    print_id("b", b)

    str1 = "CF9"
    str2 = "CF9"

    print_id("str1", str1)
    print_id("str2", str2)

if __name__ == '__main__':
    main()