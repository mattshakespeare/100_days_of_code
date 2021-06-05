from timmy_turtle import Turtle
from turtle import Screen

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.starting_postion()
colour = tim.generate_random_colour()
tim.paint_line(colour)

screen.exitonclick()