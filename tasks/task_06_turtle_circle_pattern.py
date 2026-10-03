"""Draw a coloured circle pattern and overlapping square using Turtle."""

import turtle

RADIUS = 10
DIAMETER = RADIUS * 2


def read_circle_count():
    """Return an integer from 2 through 6 entered by the user."""
    while True:
        try:
            count = int(input("Enter a number (2-6 inclusive): "))
            if 2 <= count <= 6:
                return count
        except ValueError:
            pass
        print("Invalid input. Please enter an integer between 2 and 6.")


def draw_circle(pen, x, y, colour):
    """Draw one filled circle centred at the supplied coordinates."""
    pen.penup()
    pen.goto(x, y - RADIUS)
    pen.pendown()
    pen.fillcolor(colour)
    pen.begin_fill()
    pen.circle(RADIUS)
    pen.end_fill()


def draw_square(pen, top_left_x, top_left_y, side):
    """Draw a square extending right and down from its top-left corner."""
    pen.penup()
    pen.goto(top_left_x, top_left_y)
    pen.setheading(0)
    pen.pendown()
    pen.pencolor("black")
    for _ in range(4):
        pen.forward(side)
        pen.right(90)


def main():
    """Read the pattern size and display the completed drawing."""
    count = read_circle_count()
    side = count * DIAMETER
    top_left_x = -side
    top_left_y = 0

    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.speed(0)

    for index in range(count):
        draw_circle(pen, top_left_x + index * DIAMETER, top_left_y, "blue")
        draw_circle(pen, top_left_x, top_left_y - index * DIAMETER, "yellow")
        draw_circle(
            pen,
            top_left_x + index * DIAMETER,
            top_left_y - index * DIAMETER,
            "red",
        )

    draw_square(pen, top_left_x, top_left_y, side)
    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
