import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        a, b = generate_integer(level)
        correct = a + b
        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{a} + {b} = {correct}")

    print(f"Score: {score} out of 10")      


def get_level():
    while True:
        levels = [1, 2, 3]
        try:
            n = int(input("Level: "))
            if n in levels:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(1, 10), random.randint(1, 10) 
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)


if __name__ == "__main__":
    main()