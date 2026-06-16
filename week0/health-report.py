name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("Height in metres? "))
weight = float(input("Weight in kg? "))
water = float(input("How many cups of water do you drink on average? "))
sleep = float(input("How many hours of sleep do you get on average? "))
bmi = (weight / (height ** 2))
if bmi < 18.5:
    bmi_category = "underweight"
if 18.5 <= bmi < 25:
    bmi_category = "normal weight"
if 25 <= bmi:
    bmi_category = "overweight"
max_hr = 220 - age
lower = int(max_hr * 0.6)
upper = int(max_hr * 0.8)
sleep_diff = (8 - sleep)
water_diff = (8 - water)
print("=" * 32)
print(f"HEALTH REPORT FOR {name}!")
print("=" * 32)
print(f"BMI: {bmi:.1f} ({bmi_category})")
print(f"Maximum heart rate: {max_hr} bpm")
print(f"Target heart rate range: {lower}-{upper} bpm")
print(f"Sleep: {sleep} hrs ({sleep_diff:.1f} hrs below recommended 8)")
print(f"Water: {water} glasses ({water_diff:.1f} below recommended 8)")
print("=" * 32)