phrase = input("camelCase: ")

for c in phrase:
    if c.isupper():
        print(f"_{c.lower()}", end="")
    else:
        print(c, end="")
              
