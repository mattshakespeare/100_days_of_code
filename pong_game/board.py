import turtle

BOARD_WIDTH = 800
BOARD_HEIGHT = 600
BOARD_COLOUR = 'black'
TITLE = 'Pong'

class Board():
    
    def __init__(self):
        self.board = turtle.Screen()
        self.board.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.board.bgcolor(BOARD_COLOUR)
        self.board.title(TITLE)
    
    def listen_for_key(self):
        self.board.listen()
        
    def on_key(self, func, key):
        self.board.onkey(func, key)
    
    def update_screen(self):
        self.board.update()
    
    def exit_screen(self):
        self.board.exitonclick()
    
    def turn_off_tracer(self):
        self.board.tracer(0)
    