import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    matches = re.search(pattern, s, re.IGNORECASE)
    if not matches:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = matches.groups()
    
    if m1 is None:
        m1 = 00
    if m2 is None:
        m2 = 00
    
    h1, h2 = int(h1), int(h2)
    m1, m2 = int(m1), int(m2)

    if not 1 <= h1 <= 12 and 1 <= h2 <= 12:
        raise ValueError
    if not 1 <= m1 < 60 and 1 <= m2 < 60:
        raise ValueError

    return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"


def to_24(h, m, p):
    if p == "AM" and h == 12:
        h = 0
    elif p == "PM" and h != 12:
        h += 12

    return f"{h:02}:{m:02}"


if __name__ == "__main__":
    main()