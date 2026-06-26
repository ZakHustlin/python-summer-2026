grocery_list = []
while True:
    
    try:
        entry = input("Enter your item: ").upper()
        grocery_list.append(entry)
        continue
        
    except EOFError:
        ranked = sorted(grocery_list)
        for entry in ranked:
            print(entry)
        break