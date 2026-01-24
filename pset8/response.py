import validators


def main():
    response = input("What's your email address? ")
    
    if valid_email(response):
        print("Valid")
    else:
        print("Invalid")


def valid_email(email):
    return validators.email(email)


if __name__ == "__main__":
    main()