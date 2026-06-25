total = 0

while True:
    price = input("Enter item price or 'done': ")
    if price.lower() == "done":
        break
    try:
        price = float(price)    
    except ValueError:
        print("invalid input")
        continue
    if price < 0:
        print("Invalid price")
        continue
    total = total + price
    print(f"Current total: £{total:.2f}")
        
print(f"Total: £{total:.2f}")