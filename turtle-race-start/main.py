import random
from turtle import Turtle, Screen



names_and_colors = {
    "timmy": 'red',
    "tommy": 'yellow',
    "johnny": 'blue',
    "cashy": 'purple',
    "mandy": 'green',
    "janny": 'orange'
}

turtles = []

class ModelTurtle:
    def __init__(self, name, posx, posy, color):
        self.name = name
        self.color = color
        self.x = posx
        self.y = posy
        
        self.name = Turtle()
        self.name.shape('turtle')
        self.name.penup()

        
        self.name.goto(self.x,self.y)
        self.name.shapesize(2, 2, 2)
        self.name.color(self.color)
        self.name.speed(10)
        self.name.pencolor(self.color)
        
        self.listeners()

    def move_forward(self,number):
        self.name.forward(number)

    def get_x_coord(self):
        return self.name.xcor()

    def get_color(self):
        return self.name.pencolor()


    def listeners(self):
       global screen
       screen.listen()
       screen.onkey(key="w", fun=lambda:self.move_forward())

    def change_pen_color(self):
        self.name.pencolor(random_color())



def random_color(): return (random.random(),random.random(),random.random())

   


if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=2000,height=700)
    bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Choose a color: ").strip().lower()
    y = -70
    is_race_on = False
    print(f'color: {bet}')
    
    for name,color in names_and_colors.items():
        turtles.append(ModelTurtle(name,-930, y, color))
        y+=60
        
    if bet:
        is_race_on = True
    
    while(is_race_on):
        screen.bgcolor(random_color())
        for turtle in turtles:
            if(turtle.get_x_coord() > 920):
                is_race_on = False
                if(bet == turtle.get_color().lower()):
                    print(f'Congratulations!!! You have won! The {turtle.get_color()} turtle is the winner!')
                else:
                    print(f'You have Lost! The {turtle.get_color()} turtle is the winner!')
                
                
            else:
                random_movement_number = random.randint(0,15)
                turtle.move_forward(random_movement_number)
    
    screen.exitonclick()
    screen.mainloop()