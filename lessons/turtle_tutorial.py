from turtle import Turtle, colormode, done
bob: Turtle = Turtle()
i: int = 0

iide_length: int = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

side_length = side_length * 0.97
done()