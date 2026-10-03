"""Display film records and search for a film by its identifier."""


def get_records():
    """Return the film records used by the program."""
    return [
        ["FM01", "Stealth", 135, 80],
        ["FM02", "Supernova", 90, 15],
        ["FM03", "Robin Hood", 100, 85],
        ["FM04", "Rollerball", 70, 26],
        ["FM05", "Rust", 85, 20],
    ]


def display_list(data):
    """Display all film records in a table."""
    print(f"{'ID':<10}{'Title':<20}{'Budget':<12}{'Box Office'}")
    print("-" * 54)
    for film_id, title, budget, box_office in data:
        print(f"{film_id:<10}{title:<20}{budget:<12}{box_office}")


def search_by_film_id(data):
    """Ask for a film ID and display the matching title and budget loss."""
    requested_id = input("Enter film id: ").strip().upper()
    for film_id, title, budget, box_office in data:
        if film_id == requested_id:
            print(f"Film matching the given id: {title}")
            print(f"Budget loss for film {film_id}: {budget - box_office}")
            return
    print(f"No matching film for {requested_id}")


def main():
    """Display the film list and run one search."""
    records = get_records()
    display_list(records)
    search_by_film_id(records)


if __name__ == "__main__":
    main()
