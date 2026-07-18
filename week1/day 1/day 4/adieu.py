
names = []

while True:
    try:
        item = input("Enter a name or names: ")
        names.append(item)
       
    except EOFError:
        if len(names) == 1:
            result = names[0]

        if len(names) == 2:
            result = " and ".join(names)
    

        if len(names) >= 3:
            result = ", ".join(names[:-1]) + ", and " + names[-1]
    
        print(f"Adieu, adieu, to {result}")
        break



    