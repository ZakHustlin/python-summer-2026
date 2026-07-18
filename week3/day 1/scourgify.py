import csv
import sys
if len(sys.argv) < 3:
    sys.exit("Too few arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file) as f:
        reader = csv.DictReader(f)
        with open(output_file, "w", newline="") as out:
                writer = csv.DictWriter(out, fieldnames=["first", "last", "house"])
                writer.writeheader()  # writes the column headers
                for row in reader:
                    parts = row["name"].split(", ")
                    writer.writerow({"first": parts[1], "last": parts[0], "house": row["house"]})  # writes one row
except FileNotFoundError:
     sys.exit("File not found")                    
