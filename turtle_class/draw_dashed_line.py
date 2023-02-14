from turtle import Screen, Turtle

if __name__ == '__main__':
    timmy_the_turtle = Turtle()
    screen = Screen()
    timmy_the_turtle.shape('turtle')
    timmy_the_turtle.shapesize(2, 2, 3)
    timmy_the_turtle.color('red')
    timmy_the_turtle.pencolor('blue')
    
    # for _ in range(20):
    #     timmy_the_turtle.forward(10)
    #     timmy_the_turtle.pencolor('white')
    #     timmy_the_turtle.forward(10)
    #     timmy_the_turtle.pencolor('blue')
        
    for _ in range(15):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()
    
    
    screen.exitonclick()