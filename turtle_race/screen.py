import turtle

class Screen:
    
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(width=1000, height=500)
    
    def exit_screen(self):
        self.screen.exitonclick()
    
    def text_input(self):
        user_bet = self.screen.textinput('Turtle Race', 'Place your bets, pick a colour.')
        return user_bet
        
    