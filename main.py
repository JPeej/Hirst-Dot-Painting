from turtle import Turtle, Screen, ycor
from colors import color_list
from random import choice

# painter object is moved to somewhat center the painting
painter = Turtle()
painter.penup()
painter.speed('slow')
painter.hideturtle()
painter.setposition(-250, -200)

screen = Screen()
screen.colormode(255)

# dots are placed within a 10x10 grid with a random color chosen from the color_list
for _ in range(10):
    for _ in range(10):
        color = choice(color_list)
        painter.dot(20, color)
        painter.forward(50)
    next_y_pos = painter.ycor() + 50
    painter.setposition(-250, next_y_pos)

screen.exitonclick()


