from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle(350,0)
paddle2 = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect collision with right paddle
    if ball.distance(paddle) < 50 and ball.xcor() > 330:
        ball.bouncehorz()

    # Detect collision with left paddle
    if ball.distance(paddle2) < 50 and ball.xcor() < -330:
        ball.bouncehorz()

    #Detection when paddle misses ball
    if ball.xcor() > 370:
        ball.reset()
        scoreboard.l_increase()
        scoreboard.update_Scoreboard()

    if ball.xcor() < -370:
        ball.reset()
        scoreboard.r_increase()
        scoreboard.update_Scoreboard()



screen.exitonclick()