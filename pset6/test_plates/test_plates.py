from plates import letters_begin, max_chars, num_mid, has_punct


def main():
    test_letters_begin()
    test_max_chars()
    test_num_mid()
    test_has_punct()
    

def test_letters_begin():
    assert letters_begin("CS50")
    assert not letters_begin("1AB")


def test_max_chars():
    assert max_chars("NN1234")
    assert not max_chars("NN12345")


def test_num_mid():
    assert num_mid("CS50")
    assert not num_mid("N1CK")


def test_has_punct():
    assert has_punct("CS50)")
    assert has_punct("C-S50")
    assert not has_punct("CS50")


if __name__ == "__main__":
    main()