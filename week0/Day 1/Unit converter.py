print("What would you like to convert?")
print("1. Miles to kilometres")
print("2. Kilograms to pounds")
print("3. Celsius to Fahrenheit")

unit = int(input("Enter 1, 2, or 3: "))
value = float(input("Enter the value: "))

if unit == 1:
    print(f"{value * 1.609344:.2f} kilometres")
if unit == 2:
    print(f"{value * 2.20462:.2f} pounds")
if unit == 3:
    print(f"{value * 9/5 + 32:.2f} Fahrenheit")