def process_chars():
    ch = input("Please insert a character: ")
    while ch != "#":
        print(ch, ":", ord(ch))
        ch = input("Please insert a character: ")

def process_chars2():
    while True:
        ch = input("Please insert a character: ")
        if ch == "#":
            break
        print(ch, ":", ord(ch))

def main():
    process_chars()
    process_chars2()

if __name__ == "__main__":
    main()