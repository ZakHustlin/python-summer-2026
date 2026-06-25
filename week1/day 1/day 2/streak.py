
count = 0
current_streak = 0
longest_streak = 0
previous = None

while count < 10:
    integer = input("Enter a number: ")
    if previous == None:
        previous = float(integer)
        count += 1
        continue
    else:
        count += 1
        if float(integer) > previous:
            previous = float(integer)
            current_streak += 1
            continue
        if float(integer) <= previous:
            if current_streak > longest_streak:
                longest_streak = current_streak
            
            current_streak = 1
            previous = float(integer)
            continue
if current_streak > longest_streak:
    longest_streak = current_streak
print(f"Longest streak = {longest_streak}")


    