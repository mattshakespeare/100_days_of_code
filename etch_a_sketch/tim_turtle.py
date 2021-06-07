import turtle

class Turtle:
    
    def __init__(self):
        self.tim = turtle.Turtle()
        
    def move_forward(self):
        self.tim.fd(5)
    
    def move_backwards(self):
        self.tim.bk(5)
    
    def turn_left(self):
        self.tim.lt(5)
    
    def turn_right(self):
        self.tim.rt(5)