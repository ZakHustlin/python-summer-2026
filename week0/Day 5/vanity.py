def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    
    in_numbers = False
    letter_count = 0
    number_count = 0

    for char in s:
        if char.isalpha():
            letter_count += 1
            if in_numbers:
                return False
        elif char.isdigit():
            if number_count > 4:
                return False
            if not in_numbers and char == "0":
                return False
            in_numbers = True
            number_count += 1

        else:
            return False
    if letter_count < 2 or letter_count > 5:
        return False 
    return True
main()

