sentence = input("What is your sentence?: ").lower().split()
counts = {}
for word in sentence:
    if word in counts:
       counts[word] += 1
    else:
        counts[word] = 1

for word, count in sorted(counts.items()):
    print(f"{word}: {count}")
