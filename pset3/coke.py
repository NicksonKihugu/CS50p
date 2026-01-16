amount_due = 50
while True:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert coin: "))

    if coin in [25, 10, 5]:
        amount_due -= coin
        if amount_due != 0:
            continue
        else:
            break
if amount_due == 0:
    print("Change owed: 0")
