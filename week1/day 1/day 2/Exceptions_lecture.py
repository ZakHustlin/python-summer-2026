def main():
    x = get_int("what's x")
    print (f"x is {x}")

def get_int(prompt):    
    while True:
        try:    
            x = int(input(prompt))
        except ValueError:
            pass
        else:
            return x

main()