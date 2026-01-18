import requests
import sys

#  Check command-line arguments
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

#  Convert to float
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

#  Get Bitcoin price
response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price",
    params={"ids": "bitcoin", "vs_currencies": "usd"}
)

data = response.json()
price = data["bitcoin"]["usd"]


#  Calculate and print
total = bitcoins * price
print(f"${total:,.4f}")


