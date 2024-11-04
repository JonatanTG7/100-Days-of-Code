#file main.py
import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

MOVE_DISTANCE = 20
UP=90
DOWN=270
X_POS = 350
Y_POS = 0

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")

screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard()
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
count_points = 0
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    #Detect collision with ball
    if ball.ycor() > 289 or ball.ycor() < -289:
        ball.bounce_y()

    if ball.xcor() > 400  or ball.xcor() < -400:
        if ball.xcor() > 400:
            scoreboard.update_r()
            ball.reset()
        elif ball.xcor() < -400:
            scoreboard.update_l()
            ball.reset()
        if scoreboard.score_max() == 3:
            game_is_on = False
            scoreboard.game_over()


    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()





screen.exitonclick()
