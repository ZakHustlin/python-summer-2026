months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input("Enter a date: ")
    if date[0].isalpha():
        parts = date.split()
        parts[0] = str(months[parts[0]]).zfill(2)
        parts[1] = parts[1].strip(",").zfill(2)
        parts[2] = parts[2].zfill(2)
        print(f"{parts[2]}-{parts[0]}-{parts[1]}")
        break
        
    else:
        parts = date.split("/")  
        parts[0] = parts[0].zfill(2)
        parts[1] = parts[1].zfill(2)
        print(f"{parts[2]}-{parts[0]}-{parts[1]}")
        break
