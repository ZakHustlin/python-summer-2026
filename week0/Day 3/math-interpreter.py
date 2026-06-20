equation = (input("Enter an equation: ")).split()
x, operator, y = equation
if operator == "+":
    print(int(x) + int(y))
elif operator == "-":
    print(int(x) - int(y))
elif operator == "*":
    print(int(x) * int(y))
elif operator == "/":
    print(int(x) // int(y))
else:
    print("Invalid operator")

