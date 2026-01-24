import re


def main():
    print(validate(input("IPv4 address:")))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if not matches:
        return False
    
    return all(0 <= int(group) <= 255 for group in matches.groups())


if __name__ == "__main__":
    main()