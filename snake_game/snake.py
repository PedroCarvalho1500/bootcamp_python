import random
from turtle import Turtle, Screen
import time


STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
        
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        
    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)
            # new_square = Turtle()
            # new_square.shape('square')
            # new_square.color('white')
            # new_square.penup()
            # new_square.goto(i)
            # self.segments.append(new_square)
    
    def get_head(self):
        return self.heading()
        
    def snake_move(self):
        for seg_num in range(len(self.segments) - 1 , 0 , -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            
        self.segments[0].forward(MOVE_DISTANCE)
    
    def add_segment(self, position = ()):
        new_square = Turtle()
        new_square.shape('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)
    
    def extend_snake(self):
        self.add_segment((self.segments[-1].position()))



        
if __name__ == '__main__':
    pass