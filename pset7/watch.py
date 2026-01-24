import re


def main():
    HTML = input("HTML: ")
    parse(HTML)


def parse(s):
    matches = re.search(
        r"^(.+)?(https?://)(www\.)?(youtube\.com/embed/xvFZjo5PgG0)(.+)$", s, re.IGNORECASE)
    if matches:
        protocol = matches.group(2)
        url = matches.group(4)
    print(f"url: {protocol}{url}")


if __name__ == "__main__":
    main()