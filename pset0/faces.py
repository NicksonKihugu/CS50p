def main():
    text = input()
    convert(text)


def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    print(string)


main()
