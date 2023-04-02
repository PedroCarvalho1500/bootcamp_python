from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        super().penup()
        self.create_turtle()

    def move_y(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def reset_turtle(self):
        self.clear()
        self.create_turtle()
        
    def create_turtle(self):
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shapesize(stretch_wid=1, stretch_len=1)