# Prompt user for answer
answer = input("What's the answer to the question of life? ")
answer = answer.casefold()


# Decision making
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")