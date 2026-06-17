name = input("What is your name? ")
print(f"Hello, {name}!")
age = int(input("How old are you? "))
print(f"In 10 years you will be {age + 10}!")


height = float(input("Height in metres? "))
weight = float(input("Weight in kg? "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.1f}")

