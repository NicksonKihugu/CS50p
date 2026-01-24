def main():
    string = input("Input: ")
    omit_vowel(string)


def omit_vowel(prompt):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    non_vowels = []

    for char in prompt:
        if char not in vowels:
            non_vowels.append(char)
    
    mod_prompt = "".join(non_vowels)
    print(mod_prompt)


if __name__ == "__main__":
    main()
