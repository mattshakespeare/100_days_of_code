from turtle import Turtle

SHAPE = 'square'
COLOUR = 'white'
WIDTH = 5
HEIGHT = 1

class Paddle(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.pu()
        self.shape(SHAPE)
        self.color(COLOUR)
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.goto(x_pos, y_pos)
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
        