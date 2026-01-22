import csv
import sys


def main():
    if len(sys.argv) < 3:
        print("Too few arguments!")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments!")
        sys.exit()

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        print("Not a CSV file!")
        sys.exit()
    
    convert(sys.argv[1], sys.argv[2])


def convert(before, after):
    try:
        with open(before) as file, open(after, "w") as f:
            reader = csv.DictReader(file)
            fieldnames = ["First name", "Last name", "House"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                first, last = row["name"].split(", ")
                writer.writerow({
                    "First name": first,
                    "Last name": last,
                    "House": row['house']
                })
                
    except FileNotFoundError:
        print("File not found!")
        sys.exit()


if __name__ == "__main__":
    main()
