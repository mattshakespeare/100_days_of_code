from tim_turtle import Turtle
from screen import Screen

tim = Turtle()
screen = Screen()


screen.on_key('w', tim.move_forward)
screen.on_key('s', tim.move_backwards)
screen.on_key('a', tim.turn_left)
screen.on_key('d', tim.turn_right)
screen.on_key('c', screen.clear_screen)

screen.listen_for_key()

screen.exit_screen()
