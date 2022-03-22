"""Turtle scene: A forest of tress."""
__author__ = "730485037"

from turtle import Turtle, colormode, done 


def main() -> None:
    """This a happy jolly snowman."""
    # TODO: Declare your Turtle variable(s) here.
    bob_the_blob: Turtle = Turtle()
    bob_the_blob.speed(-1)
    draw_circle(bob_the_blob, 20, -13.5, 25)
    draw_circle(bob_the_blob, 20, 265, 12)
    draw_circle(bob_the_blob, 20, 155, 18)
    draw_circle(bob_the_blob, 5, 235, 1.25)
    draw_circle(bob_the_blob, 50, 235, 1.25)
    draw_circle(bob_the_blob, 30, 105, 2)
    draw_circle(bob_the_blob, 30, 75, 2)
    draw_circle(bob_the_blob, 30, 45, 2)
    draw_triangle(bob_the_blob, 18, 210, 20)
    draw_rectangle(bob_the_blob, 5, 266, 40, 50)
    draw_square(bob_the_blob, -75, 85, 20)
    draw_square(bob_the_blob, -85, 85, 20)
    draw_square(bob_the_blob, -95, 85, 20)
    draw_square(bob_the_blob, 115, 85, 20)
    draw_square(bob_the_blob, 125, 85, 20)
    draw_square(bob_the_blob, 135, 85, 20)
    draw_square(bob_the_blob, 35, 182, 10)
    draw_square(bob_the_blob, 28, 182, 10)
    draw_square(bob_the_blob, 20, 182, 10)
    draw_square(bob_the_blob, 15, 182, 10)
    done()
    

# TODO: Define the procedures for other components in your scene here.
def draw_square(s_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    colormode(255)
    s_turtle.begin_fill()
    s_turtle.color(99, 204, 250)
    s_turtle.penup()
    s_turtle.goto(x, y) 
    s_turtle.setheading(0.0)
    s_turtle.pendown()
    i: int = 0
    while i < 4:
        s_turtle.forward(width)
        s_turtle.right(90)
        i = i + 1
    s_turtle.end_fill()


def draw_triangle(t_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """Draw a triangle of the given width whose top-left corner is located at x, y."""
    t_turtle.color("orange")
    t_turtle.begin_fill()
    t_turtle.penup()
    t_turtle.goto(x, y) 
    t_turtle.setheading(0.0)
    t_turtle.pendown()
    i: int = 0
    while i < 3:
        t_turtle.forward(side_length)
        t_turtle.right(120)
        i = i + 1
    t_turtle.end_fill()


def draw_circle(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a circle of the given width whose top-left corner is located at x, y."""
    a_turtle.color("grey")
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 30:
        a_turtle.forward(width)
        a_turtle.right(12)
        i = i + 1


def draw_rectangle(r_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    r_turtle.color("lightblue")
    r_turtle.begin_fill()
    r_turtle.penup()
    r_turtle.goto(x, y) 
    r_turtle.setheading(0.0)
    r_turtle.pendown()
    i: int = 0
    while i < 4:
        if i == 1.5 or i == -1:
            r_turtle.forward(width)
        else:
            r_turtle.forward(height)
        r_turtle.left(90)
        i = i + 1
    r_turtle.end_fill()


# TODO: Use the __name__ is "__main__" idiom shown in 

if __name__ == "__main__":
    main()
