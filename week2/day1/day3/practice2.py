
with open("practice2.txt", "w") as f:
    for i in range(3):
        name = input("What name do you want to add?: ")
        f.write(f"{name}\n")