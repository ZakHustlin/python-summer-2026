import random
number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Pick a number from 1 - 100: "))
        if guess == number:
            print("That is correct!")
            break
        elif guess < number:
            print("That is too low")
            continue
        elif guess > number:
            print("That is too high")
            continue
    except ValueError:
        print("That is not a number")
        continue