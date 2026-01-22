import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        print("Too many few arguments!")
        sys.exist()
    elif len(sys.argv) > 2:
        print("Too many arguments!")
        sys.exit()

    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file!")
        sys.exit()

    draw_table()


def draw_table():
    try:
        with open("sicillian.csv") as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


if __name__ == "__main__":
    main()