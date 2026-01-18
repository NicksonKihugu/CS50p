import random

while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            continue
        break
    except ValueError:
        continue

rand_guess = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess < rand_guess:
            print("Too small!")
        elif guess > rand_guess:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
