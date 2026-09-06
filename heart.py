import turtle
import math

def heart_x(k):
    return 15 * math.sin(k) ** 3

def heart_y(k):
    return (
        12 * math.cos(k)
        - 5 * math.cos(2*k)
        - 2 * math.cos(3*k)
        - math.cos(4*k)
    )

turtle.speed(-10)
turtle.bgcolor("black")

for i in range(6000):
    turtle.goto(heart_x(i) * 10, heart_y(i) * 10)
    turtle.color("red")
    turtle.goto(0, 0)

turtle.done()