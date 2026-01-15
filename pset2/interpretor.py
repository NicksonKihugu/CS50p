# Prompt user for an arithmetic expression
def main():
    exp = input("Expression: ")
    x, y, z = exp.split(" ")
    ans = calculate(exp)
    print(f"{ans:.1f}")


def calculate(e):
    a, b, c = e.split(" ")
    if b == '+':
        return int(a) + int(c)
    elif b == '-':
        return int(a) - int(c)
    elif b == '*':
        return int(a) * int(c)
    elif b == '/':
        return int(a) / int(c)


main()