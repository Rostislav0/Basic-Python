import turtle
from random import randint

turtle.Screen().bgcolor('black')
def rc():
    return turtle.color(f"#{randint(10, 99)}{randint(10, 99)}{randint(10, 99)}")


length = 40
turtle.setheading(0)
turtle.speed(100)
turtle.pensize(5)
turtle.shape('turtle')
for _ in range(150):
    for _ in range(4):
        rc()
        turtle.forward(length)
        turtle.right(90)
    for _ in range(4):
        rc()
        turtle.forward(length)
        turtle.left(90)
    turtle.left(180)
    for _ in range(4):
        rc()
        turtle.forward(length)
        turtle.right(90)
    for _ in range(4):
        rc()
        turtle.forward(length)
        turtle.left(90)

    length += 6
