import inflect

p = inflect.engine()
names_list = []

while True:
    try:
        names = input("Name: ")
        names_list.append(names)
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(names_list)}")
