import random
import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard




if __name__ == '__main__':
    array_cars = []
    number_loop = 1
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    scoreboard = Scoreboard()
    turtle = Player()
    car_manager = CarManager()
    
    array_cars.append(car_manager)
    
    screen.listen()
    
    screen.onkey(key="Up", fun=lambda: turtle.move_y())
    
    #screen.tracer(1)
    
    game_is_on = True
    while game_is_on:
        car_manager.create_car()
        car_manager.move_car()
        
        for i in car_manager.all_cars:
            if(i.distance(turtle) < 20):
                game_is_on = False
                scoreboard.game_over()
                
        time.sleep(0.1)
        
        #number_generated = random.randint(0,6)
        
        #if(number_generated == 1):
        #    new_car = CarManager()
        #    array_cars.append(new_car)
            
        
        screen.update()
        
        if(turtle.ycor() >= FINISH_LINE_Y):
            screen.tracer(0)
            turtle.reset_turtle()
            car_manager.level_up()
            scoreboard.increment_level()
            
            
            
        number_loop+=1
    
    screen.exitonclick()