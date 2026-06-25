phrase = input("Enter your string: ").lower()
current = ""
count = 0
result = ""
for character in phrase:
    if character == current:
        count +=1
        
    else:
        if current != "":
            result += f"{current}{count}"
        current = character
        count = 1
result += f"{current}{count}" 
print(result)
