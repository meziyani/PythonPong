from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.random_speed()

    def move(self):

        self.goto(self.xcor()+self.movex,self.ycor()+ self.movey)

    def bounce_x(self):
        self.movex = -self.movex

    def bounce_y(self):
        self.movey = -self.movey

    def reset_position(self):
        self.movex = -self.movex
        self.goto(0,0)

    def random_speed(self):
        speed = random.randint(7, 15)
        self.movex = speed
        self.movey = speed