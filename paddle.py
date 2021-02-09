from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.penup()
        self.goto(x, 0)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)