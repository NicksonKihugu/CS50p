def main():
    camel = input("camelCase: ")
    camel = snake_case(camel)
    print(f"snake_case: {camel}")


def snake_case(text):
    # Initialize an empty string
    result = ""
    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char
    return result


main()