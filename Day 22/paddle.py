#file paddle.py
from turtle import Turtle

MOVE_DISTANCE = 20
UP=90
DOWN=270

class Paddle(Turtle):

    def __init__(self ,position):
        super().__init__() # Store the paddle instance
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
