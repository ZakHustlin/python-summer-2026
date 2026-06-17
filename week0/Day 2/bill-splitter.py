name = input("What is your name? ")
price = float(input("What is the price of the meal? "))
people = int(input("How many people are splitting the bill? "))
tip = float(input("What percentage would you like to tip? "))






def calculate_tip(total, percentage):
    return total * (percentage / 100)

def calculate_split(total, num_people):
    return total / num_people

def display_summary(name, total, tip, each_pays):
    print(f"Total bill: ${total:.2f}")
    print(f"Tip amount: ${tip:.2f}")
    print(f"Each person pays: ${each_pays:.2f}")


tip_amount = calculate_tip(price, tip)
total_bill = price + tip_amount
each_person_pays = calculate_split(total_bill, people)
print(f"Hi {name}, Here's your bill breakdown: ")
display_summary(name, total_bill, tip_amount, each_person_pays)