import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)

    um_list = []
    for item in matches:
        um_list.append(item)

    count = len(um_list)

    return count


if __name__ == "__main__":
    main()