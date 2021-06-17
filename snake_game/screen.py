import turtle

class Screen:
    
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Snake')
    
    def exit_screen(self):
        self.screen.exitonclick()
    
    def turn_off_tracer(self):
        self.screen.tracer(0)
        
    def update_screen(self):
        self.screen.update()
    
    def listen_to_key(self):
        self.screen.listen()
        
    def on_key(self, func, key):
        self.screen.onkey(func, key)
        
    
    