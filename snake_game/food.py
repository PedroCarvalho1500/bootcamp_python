import random
from turtle import Turtle


def random_color(): return (random.random(),random.random(),random.random())

def generate_random_food_pos():
    return (random.randint(-280, 280),random.randint(-280, 280))



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color(random_color())
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.goto(generate_random_food_pos())
        

    def refresh(self):
        self.goto(generate_random_food_pos())
        self.color(random_color())



if __name__ == '__main__':
    pass