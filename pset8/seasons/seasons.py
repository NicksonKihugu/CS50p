from datetime import date
import inflect
import re
import sys

p = inflect.engine()


def main():
    birth_date = get_date(input("Date of birth: "))
    
    year, month, day = birth_date.split("-")
    date_of_birth = date(int(year), int(month), int(day))
    
    current_date = date.today()
    difference = current_date - date_of_birth
    
    # finding total minutes between the two dates
    total_minutes = int(difference.total_seconds() / 60)
    
    # converting the minutes to words
    output = p.number_to_words(total_minutes, andword="")
    print(f"{output} minutes")


def get_date(s):
    pattern = r"^(\d{4})-(\d{2}-(\d{2}))$"
    matches = re.search(pattern, s)

    if matches:
        return s
    else:
        sys.exit("Invalid date format")


if __name__ == "__main__":
    main()