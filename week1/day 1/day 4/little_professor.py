import random


def main():
    score = 0
    
    level = get_level()
    for _ in range(10):
        wrong = 0
        a = generate_number(level)
        b = generate_number(level)
        answer = a + b
        while True:
            try:
                
                guess = int(input(f"What is the answer to {a} + {b}: "))
                if guess == answer:
                    print("Correct")
                    score += 1
                    break
                if guess != answer:
                    print("EEE")
                    wrong += 1
            except ValueError:
                wrong += 1
            if wrong == 3:
                print(f"{a} + {b} = {answer}")
                break
    
    print(f"Score: {score}/10")



def get_level():
    while True:
        try:
            level = int(input("Pick a level: 1, 2, or 3: "))
            if level not in [1, 2, 3]:
                print("That is not a level")
                continue
            return level
        except ValueError:
            continue

def generate_number(level):
    if level == 1:
        x = random.randint(0, 9)
        return x
    elif level == 2:
        x = random.randint(0, 99)
        return x
    elif level == 3:
        x = random.randint(0, 999)  
        return x




if __name__ == "__main__":
    main()