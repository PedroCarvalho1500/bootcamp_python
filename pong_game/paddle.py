import random
from turtle import Turtle, Screen
import time


WIDTH = 20
HEIGHT = 100
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

paddles = []

class Paddle(Turtle):
    def __init__(self, positions = ()):
        super().__init__()
        super().penup()
        self.positions = positions
        self.create_paddle()
        
    def r_go_up(self):
        new_y = paddles[0].ycor() + 20
        
        if(new_y < 380 or new_y > -380):
            paddles[0].goto(paddles[0].xcor(), new_y)
        
    def r_go_down(self):
        new_y = paddles[0].ycor() - 20
        paddles[0].goto(paddles[0].xcor(), new_y)
        
        
    def l_go_up(self):
        new_y = paddles[1].ycor() + 20
        paddles[1].goto(paddles[1].xcor(), new_y)
        
    def l_go_down(self):
        new_y = paddles[1].ycor() - 20
        paddles[1].goto(paddles[1].xcor(), new_y)
        
    def create_paddle(self):
        self.add_segment()
    
    def add_segment(self):
        new_paddle = Turtle()
        new_paddle.shape('square')
        new_paddle.color('white')
        new_paddle.penup()
        new_paddle.shapesize(stretch_wid=5, stretch_len=1)
          
        new_paddle.goto(self.positions)
        paddles.append(new_paddle)



        
if __name__ == '__main__':
    pass