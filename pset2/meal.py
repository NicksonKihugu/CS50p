def main():
    time = input("What time is it? ")
    float_time = convert(time)
 
    if 7.00 <= float_time <= 8.00:
        print("Breakfast time")
    elif 12.00 <= float_time <= 13.00:
        print("lunch time")
    elif 18.00 <= float_time <= 19.00:
        print("dinner time")


def convert(t):
    hours, minutes = t.split(":")
    h = float(hours)
    m = float(minutes) / 60

    return h + m


if __name__ == "__main__":
    main()
