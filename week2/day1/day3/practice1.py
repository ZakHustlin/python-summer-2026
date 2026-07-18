count = 1
with open("names.txt") as f:
    for line in f:
        line = line.strip()
        print(f"{count}. {line}")
        count += 1
    
