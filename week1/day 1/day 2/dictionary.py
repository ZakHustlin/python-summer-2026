
dictionary = {}
while True:
    items = input("What would you like to add to the dictionary?: ").split()
    if items[0] == "quit":
        break
   
    if items[0] == "add":
        if items[1] in dictionary:
            dictionary[items[1]] += int(items[2])
        else:
            dictionary[items[1]] = int(items[2])
    elif items[0] == "remove":
        if items[1] in dictionary:
                del dictionary[items[1]]
        else:
            print(f"{items[1]} is not in the dictionary.")
    elif items[0] == "show":
        ranked = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        for key, value in ranked:
                print(f"{key}: {value}")

