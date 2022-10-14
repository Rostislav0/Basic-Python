import turtle
line = 10
turtle.speed(100)
turtle.pensize(2)
turtle.setheading(90)
turtle.forward(line)
n = 1
for _ in range(60):
    turtle.left(90)
    turtle.forward(line*n)
    n += 0.5
