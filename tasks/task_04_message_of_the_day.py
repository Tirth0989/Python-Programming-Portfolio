"""Display a different message for each day of the week."""


def main():
    """Read a day number and display the matching message."""
    day = int(input("Enter a number (1-7): "))

    if day == 1:
        print("Motivation Monday")
    elif day == 2:
        print("Terrific Tuesday")
    elif day == 3:
        print("Wonderful Wednesday")
    elif day == 4:
        print("Thoughtful Thursday")
    elif day == 5:
        print("Good Friday")
    elif day == 6:
        print("Relaxing Saturday")
    elif day == 7:
        print("Sunny Sunday")
    else:
        print("Mysterious day")


if __name__ == "__main__":
    main()
