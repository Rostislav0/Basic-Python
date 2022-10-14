import turtle


def hexagon_x6(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)
    turtle.right(120)
    for _ in range(5):
        turtle.forward(side)
        turtle.left(60)
    turtle.right(120)
    turtle.forward(side)
    turtle.setheading(0)
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)
    turtle.forward(side)
    turtle.left(60)
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)
    turtle.right(120)
    turtle.forward(side)
    turtle.left(60)
    for _ in range(5):
        turtle.forward(side)
        turtle.right(60)
    turtle.forward(side)
    turtle.left(180)
    turtle.forward(side)
    turtle.left(60)
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)


turtle.setpos(-200, 0)
turtle.clear()
hexagon_x6(100)
