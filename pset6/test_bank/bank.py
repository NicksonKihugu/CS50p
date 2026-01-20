def main():
    greeting = input("Greeting: ").strip().lower()
    amount_payable = value(greeting)
    print(amount_payable)


def value(greeting):
    pay = [0, 20, 100]
    if greeting.startswith("hello"):
        return pay[0]
    elif greeting.startswith("h"):
        return pay[1]
    else:
        return pay[2]


if __name__ == "__main__":
    main()