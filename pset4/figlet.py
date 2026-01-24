from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        print("Invalid usage!")
        sys.exit(1)
    
    try:
        figlet.setFont(font=sys.argv[2])
    except Exception:
        print("Invalid usage!")
        sys.exit(1)
else:
    print("Invalid usage!")
    sys.exit(1)

text = input("Input: ")
print(figlet.renderText(text))
