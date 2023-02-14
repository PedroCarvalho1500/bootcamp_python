from turtle import Screen, Turtle

if __name__ == '__main__':
    timmy_the_turtle = Turtle()
    screen = Screen()
    #screen.bgcolor('gray32')
    timmy_the_turtle.shape('turtle')
    timmy_the_turtle.shapesize(2, 2, 3)
    timmy_the_turtle.color('red')
    timmy_the_turtle.pencolor('blue')
    
    
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
    
    
    screen.exitonclick()