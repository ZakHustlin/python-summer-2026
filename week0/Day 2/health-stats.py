name = input("What is your name?: ")
age = int(input("What is your age?: "))
weight = float(input("What is your weight in kg?: "))
height = float(input("What is your height in cm?: "))

def calculate_bmi(weight, height):
    height_m = height / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

bmi = calculate_bmi(weight, height)

def healthy_weight_range(height):
    height_m = height / 100 
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 25 * (height_m ** 2)
    return min_weight, max_weight

min_weight, max_weight = healthy_weight_range(height)

def daily_water(weight):
    water_intake = weight * 0.033  # Approximate daily water intake in liters
    return water_intake

water_intake = daily_water(weight)

def display_health_report(name, age, weight, height, bmi, min_weight, max_weight, water_intake):
    print(f"Health report for {name} (age: {age}):")
    print("=" * 32)
    print(f"Weight: {weight} kg")
    print(f"Height: {height} cm")
    print(f"BMI: {bmi:.2f}")
    print(f"Healthy weight range: {min_weight:.2f} - {max_weight:.2f} kg")
    print(f"Daily water intake: {water_intake:.2f} liters")

display_health_report(name, age, weight, height, bmi, min_weight, max_weight, water_intake)