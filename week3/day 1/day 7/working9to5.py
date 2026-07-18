import re



def main():
    print(convert(input("Hours: ")))


def convert(s):
    parts = s.split(" to ")
    start = time_to_24(parts[0])
    end = time_to_24(parts[1])
    return f"{start} to {end}"

def time_to_24(t):
    match = re.search(r"([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)", t)
    if match:
        hour = int(match.group(1))
        minutes = int(match.group(2)) if match.group(2) else 0
        period = match.group(3)
        if period == "AM" and hour == 12:
            hour = 0
        elif period == "PM" and hour != 12:
            hour += 12
        return f"{hour}:{minutes:02d}"


if __name__ == "__main__":
    main()
