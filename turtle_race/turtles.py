import turtle
import random


class Turtle:
    
    def __init__(self, colour, position):
        self.turtle = turtle.Turtle()
        self.turtle.pu()
        self.turtle.shape('turtle')
        self.turtle.color(colour)
        self.turtle.goto(position)
    
    def move_forward(self):
        self.turtle.fd(random.randint(5, 50))
    
    def check_position(self):
        return self.turtle.pos()
    
    def colour(self):
        return self.turtle.color()