from twttr import shorten


def main():
    test_shorten()


def test_shorten():
    assert shorten("twttr")
    assert shorten("sl")


if __name__ == "__main__":
    main()