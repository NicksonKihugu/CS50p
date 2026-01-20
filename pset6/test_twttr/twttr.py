def main():
    text = input("Word: ")
    mod_text = shorten(text)
    print(mod_text)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    non_vowels = []

    for char in word:
        if char not in vowels:
            non_vowels.append(char)

    new_word = "".join(non_vowels)
    return new_word


if __name__ == "__main__":
    main()