def validate_password(password):
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
        return True
    else:
        return False
    
def main():
    password = input("Enter the password to validate: ")
    if validate_password(password):
        print("Password is valid. ")
    else:
        print("Password is invalid. It must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")

main()
