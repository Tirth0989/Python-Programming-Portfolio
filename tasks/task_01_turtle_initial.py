"""Draw the first letter of a family name using Python Turtle."""

import turtle


def main():
    """Draw a stylised letter P and keep the window open."""
    pen = turtle.Turtle()

    pen.left(90)
    pen.forward(190)
    pen.backward(100)

    pen.right(90)
    pen.circle(50, 180)

    pen.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
