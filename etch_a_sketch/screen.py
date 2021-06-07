import turtle

class Screen:
    
    def __init__(self):
        self.screen = turtle.Screen()
        
    def exit_screen(self):
        self.screen.exitonclick()
    
    def on_key(self, input, func):
        self.screen.onkey(fun=func, key=input)
    
    def listen_for_key(self):
        self.screen.listen()
    
    def clear_screen(self):
        self.screen.reset()
    