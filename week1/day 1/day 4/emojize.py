import emoji
def main():
    s = input("Enter an emoji :code: sequence: ")

    print(emoji.emojize(s, language="alias"))

main()
