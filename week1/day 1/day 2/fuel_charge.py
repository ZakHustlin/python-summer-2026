
while True:
    x = input("Enter x/y: ").split("/")
    try:
        numerator = int(x[0])
        denominator = int(x[1])
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        fraction = numerator / denominator
        percentage = round(fraction * 100)
        if percentage == 100:
            print("F")
        elif percentage == 0:
            print("E")
        else:
            print(f"{percentage}%")
        break
        
