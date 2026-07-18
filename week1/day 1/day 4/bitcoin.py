import sys
import requests
if len(sys.argv) < 2:
        sys.exit("Usage: python bitcoin.py <amount>")
try:
    amount = float(sys.argv[1])

except ValueError:
    print("That is not a number")
    sys.exit("Usage: python bitcoin.py <amount>")
   
response =  requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=724f715ed6920bb12338737bfb9ef710352104aca1f49dc766259b4f605b54ab")
data = response.json()
price = data["data"]["priceUsd"]
print(f"${(float(price) * amount):,.4f}")