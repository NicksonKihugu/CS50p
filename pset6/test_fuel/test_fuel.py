from fuel import convert, gauge


def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50"


if __name__ == "__main__":
    main()