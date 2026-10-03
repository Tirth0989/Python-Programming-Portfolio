"""Display film records and the total number of films."""


def main():
    """Print a numbered table containing each film and its box office."""
    films = [
        ["FM01", "Stealth", 135, 80],
        ["FM02", "Supernova", 90, 15],
        ["FM03", "Robin Hood", 100, 85],
        ["FM04", "Rollerball", 70, 26],
        ["FM05", "Rust", 85, 20],
    ]

    print(f"{'No.':<5}{'Film Title':<20}{'Box Office ($M)'}")
    print("-" * 40)
    for number, record in enumerate(films, start=1):
        print(f"{number:<5}{record[1]:<20}{record[3]}")

    print(f"\nTotal number of films: {len(films)}")


if __name__ == "__main__":
    main()
