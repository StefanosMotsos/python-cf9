def is_square(length: int, width: int) -> bool:
    """ Check if rectangle is square..."""
    return length == width

def main():

    try:

        length = int(input("Give me the length of the rectangle: "))
        width = int(input("Give me the width of the rectangle: "))
    except ValueError:
        print("Please enter a number")
        return

    if is_square(length, width):
        print("The rectangle is square!")
    else:
        print("The rectangle is not square!")



if __name__ == '__main__':
    main()