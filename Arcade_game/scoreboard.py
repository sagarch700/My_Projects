from turtle import Turtle

ALIGNMENT = "center"
LPOSITION = (-100, 200)
RPOSITION = (100, 200)
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.upadte_scoreboard()

    def upadte_scoreboard(self):
        self.clear()
        self.goto(LPOSITION)
        self.write(self.lscore, align= ALIGNMENT, font= FONT)
        self.goto(RPOSITION)
        self.write(self.rscore, align= ALIGNMENT, font= FONT)

    def lpoint_increase(self):
        self.lscore += 1
        self.upadte_scoreboard()

    def rpoint_increase(self):
        self.rscore += 1
        self.upadte_scoreboard()

