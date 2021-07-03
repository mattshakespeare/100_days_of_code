import turtle

class Snake:
    
    def __init__(self):
        
        self.snake = []
        
        positions = [0,10,20]
        
        for position in positions:
            new_segment = turtle.Turtle()
            new_segment.shape('square')
            new_segment.pu()
            new_segment.color('white')
            new_segment.goto(position, 0)
            new_segment.shapesize(0.5)
            self.snake.append(new_segment)
        
    
    def move(self):
        
        for segment_num in range(len(self.snake) -1, 0, -1):
            new_x = self.snake[segment_num -1].xcor()
            new_y = self.snake[segment_num -1].ycor()
            self.snake[segment_num].goto(new_x, new_y)
        self.snake[0].fd(10)
        
    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
        
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
    
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
    
    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
    
    def check_food_collision(self, obj):
        if self.snake[0].distance(obj) < 10:
            return True
        else:
            return False
    
    def check_wall_collision(self):
        if self.snake[0].xcor() == 290 or self.snake[0].xcor() == -290 or self.snake[0].ycor() == 290 or self.snake[0].ycor() == -290:
            return True
        else:
            return False
    
    def extend(self):
        self.add_segment(self.snake[-1].position())
    
    def add_segment(self, position):
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.pu()
        new_segment.color('white')
        new_segment.goto(position)
        new_segment.shapesize(0.5)
        self.snake.append(new_segment)
        
    def check_snake_collision(self):
        for segment in self.snake[1:]:
            if self.snake[0].distance(segment) < 10:
                return True
            else:
                return False
            
            
        
        