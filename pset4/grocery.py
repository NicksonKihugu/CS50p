def main():
    # Initialise an empty dictionary
    grocery_list = {}

    while True:
        try:
            item = input().upper()
            # if item in grocery_list increase tally by one
            # else if it's not initialize its tally to one
            grocery_list[item] = grocery_list.get(item, 0)+1
        except EOFError:
            print()
            print_list(grocery_list)
            break
        except ValueError:
            pass


def print_list(item_list):
    # sorted function returns a sorted list or dict
    for item in sorted(item_list):
        count = item_list[item]
        print(f"{count} {item}")


if __name__ == "__main__":
    main()
