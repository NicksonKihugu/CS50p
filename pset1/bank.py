# Prompt user for a greeting
greeting = input("Greeting: ").lower().lstrip()

# Decision making
if greeting.startswith("hello"):
    print("$ 0")
elif greeting.startswith("h"):
    print("$ 20")
else:
    print("$ 100")