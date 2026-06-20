
def convert_time(hours, minutes):
    return hours + minutes / 60


def main():
    time = input("What time is it? ").strip()
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if 7 <= convert_time(hours, minutes) <= 8:
        print("breakfast")
    elif 12 <= convert_time(hours, minutes) <= 13:
        print("lunch")
    elif 18 <= convert_time(hours, minutes) <= 19:
        print("dinner")    
    




main()





