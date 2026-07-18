
    

def main():
    text = input("Enter text: ").lower()
    print(shorten(text))


def shorten(text):
    result = ""   
    for character in text:
        if character not in ["a", "e", "i", "o", "u"]:
            result += character
    return result


if __name__ == "__main__":
    main()
