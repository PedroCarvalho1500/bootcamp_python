import random
from turtle import Turtle, Screen
from paddle import Paddle
import time


WIDTH = 20
HEIGHT = 100
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class ScoreBoard(Turtle):
    def __init__(self, positions = ()):
        super().__init__()
        super().penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
   
    def l_point(self): 
        self.l_score+=1

    def r_point(self): 
        self.r_score+=1
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,220)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        
        self.goto(100,220)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))
        
if __name__ == '__main__':
    pass