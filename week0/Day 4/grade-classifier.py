

def classify(score):
    if 100 >= score >= 90:
        return "A*"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
    

def report(name, score):
    grade = classify(score)
    return f"{name}: {score} -> {grade}"

def main():
    name = input("What is your name? ")
    score = int(input("What is your score? "))
    print(report(name, score))

main()