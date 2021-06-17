from screen import Screen
from snake import Snake
from food import Food
from scorboard import Scoreboard
import time


screen = Screen()
screen.turn_off_tracer()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update_screen()
game_on = True

screen.listen_to_key()
screen.on_key(snake.up, 'Up')
screen.on_key(snake.down, 'Down')
screen.on_key(snake.left, 'Left')
screen.on_key(snake.right, 'Right')

while game_on:
    
    screen.update_screen()
    time.sleep(0.1)
    snake.move()
    refresh = snake.check_food_collision(food)
    if refresh:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    wall_collision = snake.check_wall_collision()
    if wall_collision:
        break
    
    snake_collision = snake.check_snake_collision()
    if snake_collision:
        break

scoreboard.game_over()
        

screen.exit_screen()