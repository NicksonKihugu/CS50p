import sys


def main():
    validate_argc()
    number_lines = line_count(sys.argv[1])
    print(f"{number_lines}")


def validate_argc():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()

    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit()


def line_count(filename):
    count = 0
    try:
        with open(filename) as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#") or line == "":
                    continue
                count += 1
        return count
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


if __name__ == "__main__":
    main()