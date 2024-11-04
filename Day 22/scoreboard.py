from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.score_r = 0
        self.score_l = 0
        self.goto(0,265)
        self.write(f"score: {self.score_l} : {self.score_r} ", align="center" , font=("Courier", 24 ,"normal"))
        self.hideturtle()

    def update_l(self):
        self.clear()
        self.score_l += 1
        self.write(f" left player: {self.score_l} | right player: {self.score_r}", align="center" , font=("Courier", 24 ,"normal"))

    def update_r(self):
        self.clear()
        self.score_r += 1
        self.write(f" left player: {self.score_l} | right player: {self.score_r}", align="center" , font=("Courier", 24 ,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24 ,"normal"))

    def score_max(self):
        if self.score_l == 3  or  self.score_r == 3:
            return 3
