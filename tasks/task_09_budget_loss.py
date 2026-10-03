"""Calculate the total budget loss across a list of films."""


def get_records():
    """Return film records in ID, title, budget, and box-office format."""
    return [
        ["FM01", "Stealth", 135, 80],
        ["FM02", "Supernova", 90, 15],
        ["FM03", "Robin Hood", 100, 85],
        ["FM04", "Rollerball", 70, 26],
        ["FM05", "Rust", 85, 20],
    ]


def get_total_budget_loss(data):
    """Return the sum of budget minus box office for every loss-making film."""
    total_loss = 0
    for _, _, budget, box_office in data:
        if box_office < budget:
            total_loss += budget - box_office
    return total_loss


def main():
    """Calculate and display the total budget loss."""
    records = get_records()
    total_loss = get_total_budget_loss(records)
    print(f"Total budget loss of all films: {total_loss}")


if __name__ == "__main__":
    main()
