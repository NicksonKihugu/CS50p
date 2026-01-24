items = {
    "Apple": 130,
    "Avocado California": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Nectarine": 60,
    "Orange": 80,
    "Pear": 100,
    "Peach": 60,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80
}

item = input("Item: ").title()
if item in items:
    print(f"Calories: {items[item]}")
else:
    pass
