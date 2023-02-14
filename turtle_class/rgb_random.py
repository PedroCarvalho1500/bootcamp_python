import random
from turtle import Screen, Turtle
import math




directions = {
    "forward": lambda turtle,step: turtle.forward(random.randint(10,100)),
    "backward": lambda turtle,step: turtle.backward(random.randint(10,100)),
    "right": lambda turtle,step: turtle.right(random.randint(0,360)),
    "left": lambda turtle,step: turtle.right(random.randint(0,360)),  
}
    
    


last_key = ""
key = ""

def change_pen_color(turtle = Turtle()):
    #print(random.random())
    colors = (random.random(),random.random(),random.random())
    turtle.pencolor(colors)


def random_walk(num,turtle = Turtle()):
    global last_key, key
    change_pen_color(turtle)
    
    while(key == last_key):
        key, value = random.choice(list(directions.items()))
        
    directions[key](turtle,num)
    last_key = key
    





if __name__ == '__main__':
    timmy_the_turtle = Turtle()
    screen = Screen()
    #screen.bgcolor('gray32')
    timmy_the_turtle.shape('turtle')
    timmy_the_turtle.shapesize(2, 2, 3)
    timmy_the_turtle.color('red')
    timmy_the_turtle.speed(10)
    timmy_the_turtle.pensize(3)
    
    
    change_pen_color(timmy_the_turtle)
    
    
    for i in range(200): 
        random_walk(i,timmy_the_turtle)

    
    screen.exitonclick()