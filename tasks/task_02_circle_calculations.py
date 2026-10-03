"""Calculate the area and perimeter of a circle from a user-entered radius."""

import math


def main():
    """Read a radius and display the circle measurements."""
    radius = float(input("Please enter the radius of the circle: "))
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


if __name__ == "__main__":
    main()
