import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

filename = sys.argv[1]
try:    
    with open(f"{filename}") as f:
        count = 0
        for row in f:
            row = row.strip()
            if row == "":
                pass
            elif row.startswith("#"):
                pass
            else:
                count += 1
    print(count)
except FileNotFoundError:
    sys.exit("File not found")



