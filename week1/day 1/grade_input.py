
students = {}
number = 0
total_score = 0
while True:
    entry = input("Enter name and score: ")
    if entry == "done":
        break
    else:
        name, score = entry.split()
        number += 1
        score = int(score)
        total_score += score
        students[name] = score


for name, score in sorted(students.items()):
    print(f"{name}: {score}")

print(f"average = {total_score / number :.1f}")
top = max(students, key=lambda x: students[x])
print(f"Top student = {top}: {students[top]}")
