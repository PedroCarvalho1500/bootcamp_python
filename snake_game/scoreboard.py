from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier', 18, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,270)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT,font=FONT)
        
        

    def increase_score(self):
        self.score+=1
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,0)
        self.write(f"GAME OVER!!!", True, align=ALIGNMENT,font=FONT)


if __name__ == '__main__':
    pass