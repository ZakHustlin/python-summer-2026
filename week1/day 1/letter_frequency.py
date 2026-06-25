sentence = input("What is your sentence: ").lower()
letters = {}
for character in sentence:
        if character.isalpha():
            if character in letters:
                letters[character] += 1
            else:
                 letters[character] =   1

for character, count in sorted(letters.items(), key=lambda x: x[1], reverse=True):
    print(f"{character}: {count}")

