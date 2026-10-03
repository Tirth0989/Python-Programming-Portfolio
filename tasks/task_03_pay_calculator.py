"""Calculate weekday, weekend, and total pay amounts."""


def main():
    """Read work details and display a two-column payment summary."""
    weekday_hours = float(input("Enter hours worked on weekdays: "))
    weekend_hours = float(input("Enter hours worked on weekends: "))
    weekday_rate = float(input("Enter weekday hourly pay rate: $"))

    weekend_rate = weekday_rate * 2
    weekday_pay = weekday_hours * weekday_rate
    weekend_pay = weekend_hours * weekend_rate
    total_pay = weekday_pay + weekend_pay

    print("\nPayment details:")
    print(f"{'Weekday pay amount:':<28}${weekday_pay:.2f}")
    print(f"{'Weekend pay amount:':<28}${weekend_pay:.2f}")
    print(f"{'Total:':<28}${total_pay:.2f}")


if __name__ == "__main__":
    main()
