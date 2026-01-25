from seasons import get_date


def main():
    test_get_date()


def test_get_date():
    assert get_date("2006-06-18")


if __name__ == "__main__":
    main()