from datetime import date
import sys
import inflect
p = inflect.engine()
def main():
    try:
        DOB = input("What is your DOB: ")
        current_date = date.today()
        formattedDOB = date.fromisoformat(DOB)
        final = convert(formattedDOB, current_date)
    except ValueError:
        sys.exit()

    print(f"You are {final} minutes old! ")


def convert(formattedDOB, current_date):
    difference = current_date - formattedDOB
    minutes = difference.days * 1440
    final = p.number_to_words(minutes, andword="")
    return final


if __name__ == "__main__":
    main()