import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        super().hideturtle()
        #super().penup()
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE


    def generate_random_positions(self):
        return (random.randint(280,400),random.randint(-250,250))
    
    def create_car(self):
        number_generated = random.randint(1,6)
        if(number_generated == 1):
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(90)
            new_car.goto(self.generate_random_positions())
            new_car.shapesize(stretch_wid=2, stretch_len=1)
            self.all_cars.append(new_car)
        
    def move_car(self):
        for i in self.all_cars: 
            #input(f"ARRAY CARS: {self.all_cars}")
            print(f"SELF CAR SPEED: {self.car_speed}")
            new_x = i.xcor() - self.car_speed
            i.goto(new_x, i.ycor())
         
    def level_up(self):
        self.car_speed += MOVE_INCREMENT