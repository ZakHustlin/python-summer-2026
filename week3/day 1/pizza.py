import csv
import sys
from tabulate import tabulate
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
filename = sys.argv[1]
try:
    with open(filename) as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            rows.append(row)
        print(tabulate(rows, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")
