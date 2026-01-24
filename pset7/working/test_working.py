from working import convert, to_24


def main():
    test_convert()
    test_to_24_am()
    test_to_24_pm()


def test_convert():
    assert convert("9:00 AM to 5:00 PM") 
    assert convert("4:00 AM to 5:00 AM")
    assert convert("10:30 AM to 00:00 AM")


def test_to_24_am():
    assert to_24(9, 0, "AM") == "09:00"
    assert to_24(12, 0, "AM") == "00:00"


def test_to_24_pm():
    assert to_24(1, 0, "PM") == "13:00"
    assert to_24(12, 30, "PM") == "12:30"


if __name__ == "__main__":
    main()