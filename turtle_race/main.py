from turtles import Turtle
from screen import Screen

screen = Screen()

tim = Turtle(colour='purple', position= (-450, -150))
tony = Turtle(colour='green', position= (-450, -100))
tabby = Turtle(colour='yellow', position= (-450, -50))
toby = Turtle(colour='black', position= (-450, 0))
tom = Turtle(colour='pink', position= (-450, 50))
ted = Turtle(colour='orange', position= (-450, 100))
terry = Turtle(colour='blue', position= (-450, 150))

turtle_tuple = (tim,tony,tabby,toby,tom,ted,terry)

user = screen.text_input()

race = True

while race:
    
    for turtle in turtle_tuple:
        turtle.move_forward()
    
    for turtle in turtle_tuple:
        position = turtle.check_position()
        if position[0] >= 450:
            winning_turtle = turtle.colour()
            race = False
            break
            
if winning_turtle[0] == user:
    print(f'{winning_turtle[0]}, your turtle won congratulations.')
else:
    print(f'Unlucky, the winner was {winning_turtle[0]}')
    
screen.exit_screen()



