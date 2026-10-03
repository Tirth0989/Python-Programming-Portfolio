"""Read, display, analyse, query, and back up supermarket sales records."""

from pathlib import Path


def read_data(filename):
    """Read comma-separated store records and return values in suitable types."""
    records = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = [part.strip() for part in line.split(",")]
                if len(parts) != 4:
                    print(f"Skipping invalid line: {line}")
                    continue

                try:
                    store_id = parts[0]
                    employees = int(parts[1])
                    suburb = parts[2]
                    sales = float(parts[3])
                    records.append([store_id, employees, suburb, sales])
                except ValueError:
                    print(f"Skipping line with invalid data types: {line}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")

    return records


def print_all_records(records):
    """Display store records in an aligned table."""
    if not records:
        print("No records to display.")
        return

    print(f"{'No.':<5}{'Store ID':<12}{'Employees':<12}{'Suburb':<18}{'Sales'}")
    print("-" * 65)
    for number, record in enumerate(records, start=1):
        store_id, employees, suburb, sales = record
        print(f"{number:<5}{store_id:<12}{employees:<12}{suburb:<18}${sales:.2f}")


def write_data(filename, records):
    """Write store records to a comma-separated backup file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for store_id, employees, suburb, sales in records:
                file.write(f"{store_id},{employees},{suburb},{sales}\n")
    except OSError as error:
        print(f"Error writing to file '{filename}': {error}")


def get_min_emp_stores(records):
    """Return every store with the minimum employee count."""
    if not records:
        return []

    minimum = min(record[1] for record in records)
    return [record for record in records if record[1] == minimum]


def count_employees(records):
    """Return total employees at stores with sales above $50,000."""
    return sum(record[1] for record in records if record[3] > 50_000)


def query_suburb_stats(records):
    """Display the total and average sales for a user-entered suburb."""
    suburb_input = input("Enter suburb name: ").strip()
    matching_records = [
        record for record in records if record[2].casefold() == suburb_input.casefold()
    ]

    if not matching_records:
        print(f"No record was found for suburb {suburb_input}")
        return

    total_sales = sum(record[3] for record in matching_records)
    average_sales = total_sales / len(matching_records)
    print(f"Total sale by {suburb_input}: ${total_sales:.2f}")
    print(f"Average sale by {suburb_input}: ${average_sales:.2f}")


def main():
    """Run the complete supermarket record-processing workflow."""
    directory = Path(__file__).resolve().parent
    records = read_data(directory / "data.txt")
    if not records:
        print("No data to process.")
        return

    print("\nSupermarket sale records:")
    print_all_records(records)
    write_data(directory / "backup.txt", records)

    print("\nStores with minimum number of employees:")
    print_all_records(get_min_emp_stores(records))

    employee_count = count_employees(records)
    print(f"\nTotal employees from stores with sales more than $50000: {employee_count}")

    print("\nQuery suburb sales statistics:")
    query_suburb_stats(records)


if __name__ == "__main__":
    main()
