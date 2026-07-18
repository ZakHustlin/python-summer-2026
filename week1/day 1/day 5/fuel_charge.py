

def main():
    while True:
        x = input("Enter x/y: ").split("/")
        print(gauge(convert(x)))


def convert(fraction):
    
    try:
        numerator = int(fraction[0])
        denominator = int(fraction[1])
    except (ValueError, ZeroDivisionError):
        raise ValueError
         
    else:
        fraction = numerator / denominator
        return round(fraction * 100)

def gauge(percentage):
    percent = percentage
    if percent == 100:
        return "F"
    elif percent == 0:
        return "E"
    else:
        return f"{percent}%"
        

if __name__ == "__main__":
    main()
