import random
from turtle import Turtle, Screen
from paddle import Paddle
import time


WIDTH = 20
HEIGHT = 100
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Ball(Turtle):
    def __init__(self, positions = ()):
        super().__init__()
        super().penup()
        
        self.positions = positions
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.08
        
    def ball_go_forward(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)
            
    def bounce(self):
        self.y_move*= -1
    
    def bounce_paddle(self):
        self.x_move*=-1
        self.ball_speed * 0.9
    
        
    def create_ball(self):
        self.add_ball()
    
    def add_ball(self):
        self.ball = Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
          
        self.ball.goto(self.positions)

    def reset_game(self):
        self.penup()
        self.ball.goto((0,0))
        self.bounce_paddle()
        self.ball_speed = 0.08

    def increase_speed(self):
        self.ball_speed-=0.01

        
if __name__ == '__main__':
    pass