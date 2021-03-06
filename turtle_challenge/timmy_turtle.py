import turtle
import colorgram
import random

class Turtle:
    
    def __init__(self):
        self.tim = turtle.Turtle()
        
    def generate_random_colour(self):
        colours = colorgram.extract('images.jpg', 40)
        colour_list = []
        for colour in colours:
            r = colour.rgb.r
            g = colour.rgb.g
            b = colour.rgb.b
            new_colour = (r,g,b)
            colour_list.append(new_colour)
        
        random_colour = random.choice(colour_list)
        
        return random_colour
        
    def starting_postion(self):
        self.tim.pu()
        self.tim.sety(-200)
        self.tim.setx(-200)
    
    def paint_line_of_dots(self, colour):
        self.tim.dot(30, colour)
        self.tim.fd(50)
    
    def next_line(self):
        y_coordinate = self.tim.ycor()
        self.tim.sety(y_coordinate + 50)
        self.tim.setx(-200)
        
        