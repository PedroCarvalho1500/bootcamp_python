import turtle as t
import random

tim = t.Turtle()
#t.colormode(255)


def random_color(): return (random.random(),random.random(),random.random())



def change_pen_color(turtle = t.Turtle()):
    turtle.pencolor(random_color())

########### Challenge 5 - Spirograph ########



if __name__ == '__main__':
    timmy = t.Turtle()
    screen = t.Screen()
    timmy.shape('turtle')
    timmy.shapesize(2, 2, 2)
    timmy.color('red')
    timmy.speed(15)
    timmy.pensize(2)

    
    
    for _ in range(72):
        change_pen_color(timmy)
        timmy.position()
        timmy.heading()
        timmy.circle(120, 360)
        timmy.position()
        timmy.heading()
        timmy.left(5)
    
    
    
    screen.exitonclick()