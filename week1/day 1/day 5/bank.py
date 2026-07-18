


def main():
    greeting = input("Give a greeting: ").lower().strip()
    print(value(greeting))


def value(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()