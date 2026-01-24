def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    gauge(percent)


def convert(fraction):
    try:
        x, y = fraction.split('/')
        percentage = int(x) / int(y) * 100
    except (ValueError, ZeroDivisionError):
        raise ValueError
   
    return round(percentage)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}"


if __name__ == "__main__":
    main()