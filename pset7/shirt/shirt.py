import sys
from PIL import Image, ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few arguments!")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments!")

input_image = sys.argv[1]
output_image = sys.argv[2]
valid_exts = (".jpeg", ".png", ".jpg")

if not input_image.lower().endswith(valid_exts):
    sys.exit("Not a JPEG or PNG file!")
if not output_image.endswith(valid_exts):
    sys.exit("Not a JPEG or PNG file!")

if input_image.split(".")[-1].lower() != output_image.split(".")[-1].lower():
    sys.exit("Input and output have different extensions!")

try:
    shirt = Image.open("shirt.png")
    person = Image.open(input_image)
    person = ImageOps.fit(person, shirt.size)
    person.paste(shirt, shirt)
    person.save(output_image)
except FileNotFoundError:
    sys.exit("File does not exist")
