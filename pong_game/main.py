import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from paddle import paddles
from scoreboard import ScoreBoard



if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("PONG")
    screen.bgcolor('black')
    screen.tracer(n=3)
    r_paddle = Paddle((360,0))
    l_paddle = Paddle((-360,0))
    screen.update()
    ball = Ball((0,0))
    scoreboard = ScoreBoard()
    
    
    
    screen.listen()
    
    screen.onkey(key="Up", fun=lambda: r_paddle.r_go_up())
    screen.onkey(key="Down", fun=lambda: r_paddle.r_go_down())
    
    screen.onkey(key="w", fun=lambda: l_paddle.l_go_up())
    screen.onkey(key="s", fun=lambda: l_paddle.l_go_down())
    
    game_is_on = True
    
    while(game_is_on):
        screen.update()
        ball.ball_go_forward()
        time.sleep(ball.ball_speed)
        
        #DETECT COLLISION WITH WALL
        if((ball.ball.ycor() > 290 or ball.ball.ycor() < -290) and (ball.ball.xcor() <= 390 and ball.ball.xcor() >= -390)): 
            ball.bounce()
        
        #DETECT COLLISION WITH R_PADDLE OR L_PADDLE
        if(((ball.ball.distance(paddles[0]) < 50) and (ball.ball.xcor() > 340)) or ((ball.ball.distance(paddles[1]) < 50) and (ball.ball.xcor() < -340))): 
            ball.bounce_paddle()
            ball.increase_speed()
            screen.update()
        
        #RIGHT PADDLE MISSES
        elif(ball.ball.xcor() > 390):
            #input("HIT THE CORNER")
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            ball.reset_game()
        
        #LEFT PADDLE MISSES
        elif(ball.ball.xcor() < -390):
            #input("HIT THE CORNER")
            scoreboard.r_point()
            scoreboard.update_scoreboard()
            ball.reset_game()
             

    
    
    screen.exitonclick()