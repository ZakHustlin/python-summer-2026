total = 0
integers = 0
while integers < 10:
    try:
        number = int(input("Enter a number: "))
        if number >= 0:
            total += number
            integers += 1
        else:
            print("Skipped")
            
    except ValueError:
        print("That is not a number")  

if integers == 10:
    print(f"Sum is {total}")
    print(f"Average is {total / 10}")

