def main():
    dollars = float(input("How much was the meal? "))
    percent = float(input("What percentage would you like to tip? "))
    tip = find_tip(dollars, percent)
    print(f"Leave $ {tip:.2f}")


def find_tip(x, y):
    return x * (y / 100)


main()