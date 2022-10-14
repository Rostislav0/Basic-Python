import turtle


def rectangle(*args):
    turtle.forward(args[1])
    turtle.left(90)
    turtle.forward(args[0])
    turtle.left(90)
    turtle.forward(args[1])
    turtle.left(90)
    turtle.forward(args[0])


def triangle(*args):
    for _ in range(3):
        turtle.forward(args[0])
        turtle.left(120)


def square(*args):
    for _ in range(3):
        turtle.left(20)
        for _ in range(4):
            turtle.forward(args[0])
            turtle.left(90)


def square2(*args):
    for _ in range(4):
        turtle.forward(args[0])
        turtle.left(90)
    turtle.forward(args[0] / 2)
    turtle.left(90)
    turtle.forward(args[0])
    turtle.backward(args[0] / 2)
    turtle.left(90)
    turtle.backward(args[0] / 2)
    turtle.forward(args[0])
    turtle.backward(args[0] / 2)
    turtle.left(45)
    turtle.backward(args[0] / 2)
    turtle.forward(args[0])
    turtle.backward(args[0] / 2)
    turtle.left(90)
    turtle.backward(args[0] / 2)
    turtle.forward(args[0])
    turtle.left(90)
    turtle.backward(args[0] / 2)
    for _ in range(4):
        turtle.forward(args[0])
        turtle.left(90)


def hexagon(*args):
    for _ in range(6):
        turtle.forward(args[0])
        turtle.left(60)


turtle.shape('turtle')
turtle.speed(2)
turtle.color('red')
funcs = {triangle: 150, hexagon: 120, square: 100, rectangle: 130, square2: 123}
for i in funcs:
    i()
    turtle.clear()
    turtle.setheading(0)
    turtle.setpos(0, 0)
