def main():
    get_fuel("Fraction: ")


def get_fuel(prompt):
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            percentage = int(x) / int(y) * 100
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(f"{round(percentage)}%")


if __name__ == "__main__":
    main()