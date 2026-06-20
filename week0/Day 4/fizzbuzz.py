def triage(heart_rate, oxygen_sat):
    if heart_rate > 120 and oxygen_sat < 90:
        return "Critical"
    elif heart_rate < 50:
        return "Urgent"
    elif heart_rate > 100 or oxygen_sat < 95:
        return "Urgent"
    
    else:
        return "Stable"
    
def main():
    heart_rate = int(input("Enter heart rate: "))
    oxygen_sat = int(input("Enter oxygen saturation: "))
    print(triage(heart_rate, oxygen_sat))

main()