from um import count


def main():
    test_count()


def test_count():
    assert count("um")
    assert count("um yummy um")
    assert not count("yummy")


if __name__ == "__main__":
    main()