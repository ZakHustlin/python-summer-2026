secret = 7
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print(f"Too low, you have {max_attempts - attempts} attempts left. ")
    else:
        print(f"Too high, you have {max_attempts - attempts} attempts left. ")

if guess != secret:
    print(f"Out of attempts. The number was {secret}.")