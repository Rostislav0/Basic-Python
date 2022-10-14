import turtle

turtle.shape('circle')
"""square (квадрат);
arrow (стрелка);
circle (круг);
turtle (черепашка);
triangle (треугольник);
classic (классическая стрелка)."""
turtle.forward(50)
turtle.right(45)

turtle.forward(50)
turtle.left(45)
print(turtle.heading())
turtle.forward(50)
turtle.setheading(45)
print(turtle.heading())
turtle.forward(50)

for _ in range(4):
    turtle.forward(150)
    turtle.left(90)
