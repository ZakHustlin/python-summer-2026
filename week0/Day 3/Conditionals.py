name = input("What is your name? ")

match name:
    case "harry" | "hermione" | "ron":
        print("Hello member of gryffindor!")
    case _:
        print("Hello, stranger!")