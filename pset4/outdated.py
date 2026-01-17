months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_input = input("Date: ").strip()

    try:
        m, d, y = map(int, date_input.split('/'))
        if not (1 <= m <= 12 and 1 <= d <= 31):
            raise ValueError
        break

    except ValueError:
        try:
            if "," not in date_input:
                raise ValueError

            parts = date_input.replace(",", "").split()
            m = months.index(parts[0].title()) + 1
            d = int(parts[1])
            y = int(parts[2])

            if not (1 <= m <= 12 and 1 <= d <= 31):
                raise ValueError
            break

        except (ValueError, IndexError):
            continue

    except EOFError:
        break

print(f"{y:04}-{m:02}-{d:02}")

