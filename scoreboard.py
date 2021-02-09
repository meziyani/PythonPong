from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0

    def update_score(self):
        self.clear()
        self.goto(0, 250)
        self.write("Yani's Pong", font=("Arial", 24), align="center")
        self.goto(-310, 250)
        self.write(f"{self.lscore}", font=("Comic Sans", 48))
        self.goto(310, 250)
        self.write(f"{self.rscore}", font=("Comic Sans", 48))