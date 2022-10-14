import turtle
import random
turtle.speed(3)
for _ in range(10):
    turtle.color(['red', 'black', 'green', 'blue', 'pink', 'yellow', 'violet'][random.randint(0, 6)])
    for _ in range(2):
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(60)
    turtle.left(30)
