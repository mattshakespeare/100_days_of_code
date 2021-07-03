from board import Board
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

board = Board()
board.turn_off_tracer()
right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = ScoreBoard()

board.listen_for_key()
board.on_key(right_paddle.up, 'Up')
board.on_key(right_paddle.down, 'Down')
board.on_key(left_paddle.up, 'w')
board.on_key(left_paddle.down, 'a')
game_on = True

while game_on:
    
    time.sleep(0.1)
    board.update_screen()
    ball.move_ball()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.speed_up()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()
    
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.l_point()
        
    
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.r_point()
    

board.exit_screen()