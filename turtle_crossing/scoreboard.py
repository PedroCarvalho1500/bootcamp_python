from turtle import Turtle


FONT = ("Courier", 24, "bold")
POSITIONS = (-200,250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        super().penup()
        self.hideturtle()
        self.color("black")
        self.current_level = 0
        self.update_scoreboard()
        
   
    def update_scoreboard(self):
        self.clear()
        self.goto(POSITIONS)
        self.write(f"Level: {self.current_level}", align="center", font=FONT)
        
        
    def increment_level(self):
        self.current_level+=1
        self.update_scoreboard()
        
        
    def game_over(self):
        self.goto(30,0)
        self.write(f"GAME OVER!!!", align="center", font=FONT)
        
if __name__ == '__main__':
    pass
