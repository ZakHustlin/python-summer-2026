


menu = {
    "spaghetti": 10,
    "pizza": 15,
    "bread": 5,
    "soup": 5,
    "steak": 20,
}
total = 0
while True:
    item = input("What do you want to eat: ")
    if item in menu:
        print(menu[item])
        total += menu[item]
    elif item == "done":
        print(f"Total: £{total:.2f}")
        break
    else:
        print("not found")
     
