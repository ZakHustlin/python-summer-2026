def convert():
    emoticon = input("Enter an emoticon: ")
    return emoticon.replace(":)", "🙂").replace(":(", "🙁").replace(":D", "😃").replace(":'(", "😢")

print(convert())