def main():
    plate = input("PLate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    checks = [letters_begin, max_chars, num_mid, has_punct]
    for check in checks:
        if not check(s):
            return False
    return True


def letters_begin(s):
    return s[:2].isalpha()


def max_chars(s):
    return len(s) <= 6


def num_mid(s):
    found_digit = False

    for char in s:
        if char.isdigit():
            if not found_digit and char == '0':
                return False
            found_digit = True
        elif found_digit and char.isalpha():
            return False
    return True


def has_punct(s):
    for char in s:
        if not char.isalnum():
            return True
    return False


if __name__ == "__main__":
    main()