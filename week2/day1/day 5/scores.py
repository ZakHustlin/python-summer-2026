import csv

with open("scores.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        grade = int(row["score"])
        if grade > 75:
            print(f"{row['name']}: {row['score']}")
        
