from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

# Paddle movements
screen.listen()
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

scoreboard.update_score()

while game_is_on:
    time.sleep(0.03)

    # Left point

    if ball.xcor() > 350:
        scoreboard.lscore = scoreboard.lscore+1
        scoreboard.update_score()
        ball.reset_position()
    # Right point

    if ball.xcor() < -350:
        scoreboard.rscore = scoreboard.rscore + 1
        scoreboard.update_score()
        ball.reset_position()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Hits paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.movex * 1.1
        ball.movey * 1.1
        ball.bounce_x()


    ball.move()
    screen.update()

screen.exitonclick()