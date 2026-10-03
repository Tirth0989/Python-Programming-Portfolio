"""Determine whether a supermarket customer is eligible for a discount."""


def read_positive_float(prompt):
    """Prompt until the user enters a number greater than zero."""
    while True:
        try:
            value = float(input(prompt).replace("$", "").strip())
            if value > 0:
                return value
        except ValueError:
            pass
        print("Invalid. Please enter a number greater than zero.")


def read_positive_integer(prompt):
    """Prompt until the user enters an integer greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Invalid. Please enter an integer greater than zero.")


def read_yes_no(prompt):
    """Prompt until the user enters y or n."""
    while True:
        response = input(prompt).strip().lower()
        if response in {"y", "n"}:
            return response
        print("Invalid. Please enter 'y' or 'n'.")


def main():
    """Collect purchase details and display discount eligibility."""
    price = read_positive_float("Enter product price (>0): $")
    quantity = read_positive_integer("Enter quantity (>0): ")
    claimed = read_yes_no("Have you claimed the discount before (y/n): ")

    total = price * quantity
    print(f"\nTotal shopping amount: ${total:.2f}")
    print(f"Claimed discount: {claimed}")

    if total <= 500 and claimed == "n":
        print("You are eligible for a discount.")
    else:
        print("Sorry, you are not eligible for a discount.")


if __name__ == "__main__":
    main()
