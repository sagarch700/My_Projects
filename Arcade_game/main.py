from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("My arcade game")
screen.tracer(0)

#paddle

# paddle = Turtle()
# paddle.shape("square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color("white")
# paddle.penup()
# paddle.goto(370, 0)

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Event listner
screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Ball Collison with the wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect when rpaddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.lpoint_increase()

    # Detetct when lpadde misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rpoint_increase()

screen.exitonclick()