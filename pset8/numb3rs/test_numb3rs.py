from numb3rs import validate


def main():
    test_validate()


def test_validate():
    test_cases = [
        ("192.168.1.1", True),
        ("255.255.255.255", True),
        ("0.0.0.0", True),
        ("1.2.3.4.5", False),
        ("257.3.2.1", False),
        ("999.134.0.1", False)
    ]
    for ip, expected in test_cases:
        assert validate(ip) == expected


if __name__ == "__main__":
    main()