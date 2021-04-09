import turtle

painter = turtle.Turtle("turtle")
painter.shapesize(0.8, 0.8)
painter.speed(10)  # "fast"

painter.pencolor("blue")

for i in range(50):
    painter.forward(50 + i)
    painter.left(92)

painter.pencolor("red")

for i in range(50):
    painter.forward(100 + i)
    painter.left(92)

turtle.done()
