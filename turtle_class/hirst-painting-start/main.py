###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import random
import colorgram
from turtle import Screen, Turtle
import turtle as t

rgb_colors = []
t.colormode(255)
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

x = -300
y = -350
    
if __name__ == '__main__':
    tim = Turtle()
    screen = Screen()
    tim.shapesize(1, 1, 1)
    
    tim.color('white')
    tim.penup()
    tim.hideturtle()
    tim.speed("fastest")
    tim.setposition(x,y)

    i = 0
    
    for _ in range(100):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)
        
        i += 1
        if(i == 10):
            i = 0
            y+=60
            tim.setposition(x,y)

    screen.exitonclick()