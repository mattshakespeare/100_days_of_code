from timmy_turtle import Turtle
from turtle import Screen

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.starting_postion()

for i in range(10):
    for i in range(10):
        colour = tim.generate_random_colour()
        tim.paint_dot(colour)
    tim.next_line()

screen.exitonclick()