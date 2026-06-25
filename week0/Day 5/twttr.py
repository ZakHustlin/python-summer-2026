text = input("Enter text: ").lower()
result = ""
for character in text:
    if character not in ["a", "e", "i", "o", "u"]:
        result += character
print(result)
    