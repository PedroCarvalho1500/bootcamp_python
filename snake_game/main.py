import random
from turtle import Turtle, Screen, fd, rt
import time
from scoreboard import ScoreBoard
from snake import Snake
from food import Food



if __name__ == '__main__':
    
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("My Snake Game")
    screen.tracer(0)
    screen.bgcolor('black')
    snake = Snake()
    food = Food()
    score = ScoreBoard()
    screen.listen()
    
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.snake_move()

        if(snake.head.distance(food) < 15):
            food.refresh()
            score.increase_score()
            screen.update()
            snake.extend_snake()
            
            
        if(snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298):
            game_is_on = False
            score.game_over()
            
        for segment in snake.segments[1:]:
            if(snake.head.distance(segment) < 10):
                game_is_on = False
                score.game_over()    
        
        # for segment in snake.segments:
        #     if segment == snake.head:
        #         pass
            
        #     elif(snake.head.distance(segment) < 10):
        #         game_is_on = False
        #         score.game_over()
            
            

    screen.exitonclick()
    